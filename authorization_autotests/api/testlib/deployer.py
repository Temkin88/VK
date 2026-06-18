import enum
import json
import os
import re
import shutil
from functools import partial
from typing import Any, Dict, Optional

import requests
from ..core.decorators import qacore_decorators
from ..core.exceptions import AutotestException, FrameworkException
from ..core.helpers import SingletonUniqueArgs, get_process_pid, load_yaml_file, merge_dicts, write_yaml_file
from ..core.logger import FMT_DEFAULT, FMT_FAIL, FMT_FATAL, FMT_OK, FMT_WARN, fmtstring, log

from ..core.service import ServiceControl
from ..core.steps_common import compare_two_items, sleep
from requests.models import Response
from const import DEPLOYER_PARAMS
from helpers import sleep_or_exit


class ClusterType(enum.Enum):
    """Cluster types from API /config/dbshards/list"""

    overlord = {"name": "overlord", "ftType": "Overlord", "api_info": "overlord", "can_switch_master": True}
    patroni = {"name": "patroni", "ftType": "Patroni", "api_info": "pg", "can_switch_master": True}
    etcd = {"name": "etcd", "ftType": "Etcd", "api_info": "etcd", "can_switch_master": False}
    orchestrator = {"name": "orchestrator", "ftType": "Orchestrator", "api_info": "mysql", "can_switch_master": True}
    orchestrator_itself = {
        "name": "orchestrator_itself",
        "ftType": "",
        "api_info": "orchestrator",
        "can_switch_master": False,
    }
    sentinel = {
        "name": "sentinel",
        "ftType": "Sentinel",
        "api_info": "sentinel",
        "can_switch_master": False,
    }
    election = {"name": "election", "no_info": True}
    # idk what this mean, skip too
    no_need = {"name": "no_need", "no_info": True}


class StorageType(enum.Enum):
    """Cluster types from API /config/storages/list"""

    cloud = {"storages": ["blobcloud", "cldst", "mailcloud"]}  # based at nginx
    crow = {"storages": ["crow_index"]}
    mescalito = {"storages": ["mescalito", "mescalito_metad"]}
    zepto = {"storages": ["zepto_del", "zepto_main", "zepto_metad", "zepto_opt", "zepto_search", "zepto_skel"]}


class Deployer(metaclass=SingletonUniqueArgs):
    """
    Interaction with any deployer

    Args:
        host: hostname or ip address
        port: api port of service

    """

    def __init__(self, host: str = "127.0.0.1", port: int = 8888):
        self.host = host
        self.port = int(port)
        self.cfg_file = DEPLOYER_PARAMS
        self.unit = ServiceControl(
            "deployer",
            pid_detector=partial(
                get_process_pid, binary="onpremise-deployer", full_comm=r".+onpremise-deployer_linux.+"
            ),
        )
        self.log_position = 0
        self.ssh_key = self._get_ssh_key()
        self.ssh_user = self._get_ssh_user()
        self.dbshards_list = self.config_dbshards_list()
        self.vkws_type = (
            "ku" if list(filter(lambda r: r["role"].startswith("monstor"), self.computes_list()["computes"])) else "ou"
        )

    @qacore_decorators
    def control_instance(
        self,
        cmd: str = "restart",
        expected_exitcode: int = 0,
        log_result: bool = True,
        check: bool = True,
    ) -> None:
        """CONTROL DEPLOYER INSTANCE"""
        if cmd not in ("start", "stop", "restart", "reload"):
            raise FrameworkException(f"Unsupported command: {cmd}")

        was_started = self.unit.is_started
        # log_position_before = os.stat(self.log_file).st_size
        getattr(self.unit, cmd)(expected_exitcode=expected_exitcode, log_result=log_result)

        if check and ((cmd == "start" and not was_started) or cmd == "restart"):
            # don't wat to add journalctl module right now, hope sleep is enough
            sleep(5, msg="Waiting for deployer boot")
        #     search_in_log(
        #         log_file=self.log_file,
        #         pattern=rf"DEPLOYER\[{self.unit.get_pids()[0]}\]:.+http server started on.+",
        #         retries=10,
        #         log_position=log_position_before,
        #         log_result=False,
        #     )

    @qacore_decorators
    def computes_list(self, expected_code: Optional[int] = 200) -> Dict:
        """DEPLOYER COMPUTES LIST"""
        response = self._request_api("/computes/list", expected_code=expected_code)
        resp_json = response.json()
        compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
        compare_two_items("content", "in", resp_json, desc="Check content field", log_result=False)
        compare_two_items(resp_json["status"], "==", expected_code, desc="Check response code", log_result=False)
        return resp_json["content"]

    @qacore_decorators
    def turn_compute(self, action: str, hostname: str = "hypervisor7", expected_code: Optional[int] = 200) -> None:
        """
        TURN COMPUTE

        Включение / отключение (плановое) одного из гипервизоров
        action - только значения disable/enable
        """
        if action not in ["disable", "enable"]:
            raise FrameworkException("Требуется параметр 'action' из списка разрешенных, получен: %s", action)
        log.info(f"{hostname} - {action}", extra=FMT_DEFAULT)
        if action == "disable":
            response = self._request_api(
                "/computes/disable/check", expected_code=expected_code, json={"compute": hostname}
            )
            log.debug(f"response check - {response.json()}", extra=FMT_DEFAULT)
            resp_json = response.json()
            compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
            compare_two_items(resp_json["status"], "==", expected_code, desc="Check response code", log_result=False)
        response = self._request_api(f"/computes/{action}", expected_code=expected_code, json={"compute": hostname})
        log.debug(f"response {action} - {response.json()}", extra=FMT_DEFAULT)
        resp_json = response.json()
        compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
        compare_two_items(resp_json["status"], "==", expected_code, desc="Check response code", log_result=False)

    @qacore_decorators
    def autoinstall(self) -> None:
        """
        AUTOINSTALL

        1-Запуск проверок и автоустановки
        2-Получение статуса о начале установки
        3-Добавить механизм пропуска автоустановки (если не требуется)
        """
        json_data = {
            "noop": True,
            "apply": True,
            "threshold": 0,
            "checkAgentToAgentConnectivity": True,
            "checkNodeToNodeConnectivity": True,
            "checkKernelFlag": True,
            "checkHash": True,
            "checkDockerVersion": True,
        }
        response = self._request_api("/tasks/autoInstall", expected_code=200, json=json_data, method="post")
        resp_json = response.json()
        compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
        compare_two_items(resp_json["status"], "==", 200, desc="Check response code", log_result=False)
        compare_two_items("content", "in", resp_json, desc="Check content field", log_result=False)
        content = resp_json.get("content")
        compare_two_items("checkResults", "in", content, desc="Check content field", log_result=False)
        check_results = content.get("checkResults")

        compare_two_items(
            "agentConnectivityCheckResults", "in", check_results, desc="Check content field", log_result=False
        )
        compare_two_items("checkDockerVersion", "in", check_results, desc="Check content field", log_result=False)
        compare_two_items("checkKernelFlag", "in", check_results, desc="Check content field", log_result=False)

        agent_connectivity_check_results = check_results.get("agentConnectivityCheckResults")
        check_docker_version = check_results.get("checkDockerVersion")
        check_kernel_flag = check_results.get("checkKernelFlag")
        compare_two_items(
            "status",
            "in",
            agent_connectivity_check_results,
            desc="Check status in agentConnectivityCheckResults field",
            log_result=False,
        )
        compare_two_items(
            "status", "in", check_docker_version, desc="Check status in checkDockerVersion field", log_result=False
        )
        compare_two_items(
            "status", "in", check_kernel_flag, desc="Check status in checkKernelFlag field", log_result=False
        )
        compare_two_items(
            agent_connectivity_check_results["status"],
            "==",
            "success",
            desc="Check success failed in agentConnectivityCheckResults",
            log_result=False,
        )
        compare_two_items(
            check_docker_version["status"],
            "==",
            "success",
            desc="Check success failed in checkDockerVersion",
            log_result=False,
        )
        compare_two_items(
            check_kernel_flag["status"],
            "==",
            "success",
            desc="Check success failed in checkKernelFlag",
            log_result=False,
        )

        resp_json = self.check_installation_status()
        compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
        compare_two_items(resp_json["status"], "==", 200, desc="Check response code", log_result=False)
        compare_two_items("content", "in", resp_json, desc="Check content field", log_result=False)
        content = resp_json.get("content")
        compare_two_items("autoInstallStage", "in", content, desc="Check autoInstallStage field", log_result=False)
        if not compare_two_items(
            content.get("autoInstallStage"),
            "==",
            "noop",
            desc="Check autoInstallStage status",
            log_result=False,
            raise_if_fail=False,
        ):
            compare_two_items(
                content.get("autoInstallStage"), "==", "apply", desc="Check autoInstallStage status", log_result=False
            )
        compare_two_items(
            content.get("autoInstallStarted"), "==", True, desc="Check autoInstallStarted", log_result=False
        )
        compare_two_items(content.get("allowAutoInstall"), "==", True, desc="Check allowAutoInstall", log_result=False)
        compare_two_items(content.get("allowStart"), "==", False, desc="Check allowStart", log_result=False)

    @qacore_decorators
    def check_installation_status(self) -> Dict:
        """
        CHECK INSTALLATION STATUS

        Получение статуса установки
        """
        response = self._request_api("/tasks/status", expected_code=200)
        resp_json = response.json()
        compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
        compare_two_items(resp_json["status"], "==", 200, desc="Check response code", log_result=False)
        return resp_json

    @qacore_decorators
    def config_dbshards_list(self, expected_code: Optional[int] = 200) -> Dict:
        """
        DEPLOYER DBSHARDS LIST

        Returns:
            # dbname: {info}
            addrbook: {
                overlord: true,
                clusters: {
                    1: {
                        members: [ "addrbook1", "addrbook2" ],
                        master: "addrbook1"
                    }
                }
            }

        """
        response = self._request_api("/config/dbshards/list", expected_code=expected_code)
        resp_json = response.json()
        compare_two_items("status", "in", resp_json, desc="Check status field", log_result=False)
        compare_two_items("content", "in", resp_json, desc="Check content field", log_result=False)
        if expected_code is not None:
            compare_two_items(resp_json["status"], "==", expected_code, desc="Check response code", log_result=False)
        if not resp_json["content"]:
            log.warning("Empty dbshards list returned", extra=FMT_WARN)

        return resp_json["content"]

    @qacore_decorators
    def tasks_apply(self, hypervisor_hostname: str, task: str, expected_code: Optional[int] = 200) -> Dict:
        """DEPLOYER TASKS APPLY"""
        response = self._request_api(
            "/tasks/apply",
            expected_code=expected_code,
            method="post",
            json={"taskName": task, "hostname": hypervisor_hostname},
            timeout=20,
        )
        resp_json = response.json()
        compare_two_items("status", "in", resp_json, desc=f"Check status field for {task}", log_result=False)
        compare_two_items(
            resp_json["status"], "==", expected_code, desc=f"Check response code for {task}", log_result=False
        )
        return resp_json

    @qacore_decorators
    def get_dbs_status(
        self,
        expected_code: Optional[int] = 200,
        raise_if_fail: bool = False,
        log_result: bool = True,
        check_dbname: Optional[str] = None,
    ) -> Dict:
        """
        DEPLOYER DATABASES STATUS

        Fetch info from deplyer for every dbname (role)

        Args:
            expected_code: code for all requested api
            raise_if_fail: change any DB warnings into fail and raise
            log_result: log db status
            check_dbname: define one db name for check

        Returns:
            add key "im_master" for all bases for unified checks if there is no errors
            {
                "attfiledb": { # dbname (role)
                    "attfiledb1": {"im_master": True, ... 'lsn': 1, 'master': True, 'replicationStatus': 'primary'}
                    "attfiledb2": {"im_master": False, ... 'lsn': 1, 'master': True, 'replicationStatus': 'primary'}
                }
            }

        """
        # don't use in self, we should get fresh db statuses
        shards_list = self.config_dbshards_list(expected_code=expected_code)
        result = {}
        dbs_check_passed = True

        # возможно в свежей версии ситуация получше, поэтому ошибки делейсенда игнорирую всегда
        # BUG: https://jira.vk.team/browse/WSTECH-158
        skip_db_fails = ["delaysend-queue-tar"]

        for dbname, dbcfg in shards_list.items():
            if check_dbname is not None and dbname != check_dbname:
                continue
            cluster_type = self._get_cluster_type(dbname, dbcfg)
            # deployer can't control databases with election type
            if cluster_type.value.get("no_info"):
                if log_result:
                    log.info(f"{dbname} {fmtstring('No info at deployer')}", extra=FMT_OK)
                    log.info("-" * 80)
                continue
            for cluster_id in dbcfg["clusters"]:
                # exclude for orchestrator itself
                if dbname == "orchestrator":
                    response = self._request_api(
                        f"/config/dbshards/{cluster_type.value.get('api_info')}/info", expected_code=expected_code
                    )
                else:
                    response = self._request_api(
                        f"/config/dbshards/{cluster_type.value.get('api_info')}/info",
                        expected_code=expected_code,
                        method="post",
                        json={"dbName": dbname, "dbShard": int(cluster_id), "ftType": cluster_type.value.get("ftType")},
                    )
                resp_json = response.json()
                if "status" not in resp_json or "content" not in resp_json:
                    raise AutotestException(f"Bad response from {response.url}: {response.text}")

                if expected_code is not None:
                    compare_two_items(
                        resp_json["status"],
                        "==",
                        expected_code,
                        desc=f"Check response code for {fmtstring(dbname)}",
                        log_result=False,
                    )

                master_found = False
                result[dbname] = {}
                if not resp_json["content"]:
                    log.warning(f"Empty response from dbshards info for {fmtstring(dbname)}", extra=FMT_WARN)
                else:
                    for dbpart_name, dbpart_cfg in resp_json["content"].items():
                        check_db_part = self._check_db_part(cluster_type, dbpart_cfg)
                        result[dbname][dbpart_name] = {**dbpart_cfg, **check_db_part}

                        if log_result and check_db_part["im_master"] is not None:
                            log.info(
                                f"{dbpart_name} is {fmtstring('leader') if check_db_part['im_master'] else 'follower'}",
                                extra=FMT_OK,
                            )
                        if master_found:
                            if check_db_part["im_master"]:
                                log.error(f"Double master detected for {dbname}", extra=FMT_FAIL)
                                dbs_check_passed = False
                        elif check_db_part["im_master"]:
                            master_found = True

                        if not check_db_part["db_ready"]:
                            if raise_if_fail and dbname not in skip_db_fails:
                                dbs_check_passed = False
                                log.error(f"{dbpart_name}: {check_db_part['check_msg']}", extra=FMT_FAIL)
                            elif log_result:
                                log.warning(f"{dbpart_name}: {check_db_part['check_msg']}", extra=FMT_WARN)

                # api_type == sentinel для редисов, информации о мастере не предоставляется
                if not master_found and cluster_type != ClusterType.sentinel:
                    if raise_if_fail and dbname not in skip_db_fails:
                        dbs_check_passed = False
                        log.error(f"{dbname} has no active leader", extra=FMT_FAIL)
                    elif log_result:
                        log.warning(f"{dbname} has no active leader", extra=FMT_WARN)

                if log_result:
                    log.info("-" * 80)

        if raise_if_fail and not dbs_check_passed:
            raise AutotestException("Databases aren't in healthy state")

        return result

    def _check_db_part(self, api_type: ClusterType, dbpart_cfg: dict) -> dict:
        # ключи подмешиваются в ответ деплоера, они не должны пересекаться с его ключами
        result = {"im_master": None, "check_msg": "", "db_ready": True}
        ignored_tnt_messages = [r"unexpected EOF when reading from socket", r"timed out"]
        bad_msg_detected = False
        if "respCode" in dbpart_cfg and dbpart_cfg["respCode"] != 200:  # noqa: PLR2004
            result["db_ready"] = False
            result["check_msg"] = f"respCode: {dbpart_cfg.get('respCode')}"
            return result
        if dbpart_cfg.get("error"):
            result["db_ready"] = False
            result["check_msg"] = dbpart_cfg["error"]
            return result

        # Способ определения есть ли мастер у каждого типа свой
        if api_type == ClusterType.overlord:
            result["im_master"] = "master" in dbpart_cfg
        if api_type == ClusterType.patroni:
            result["im_master"] = dbpart_cfg["member"]["role"] == "leader"
        if api_type == ClusterType.sentinel:
            result["im_master"] = dbpart_cfg["role"] == "master"
        if api_type == ClusterType.etcd:
            result["im_master"] = dbpart_cfg["leader"]
        if api_type == ClusterType.orchestrator:
            result["im_master"] = "overlordState" in dbpart_cfg and dbpart_cfg["overlordState"]["master"]
        if api_type == ClusterType.orchestrator_itself:
            result["im_master"] = dbpart_cfg["State"] == "Leader"

        # анализируем сообщения от баз, они у каждого типа свои и по своим уникальным ключам
        if "replicationStatus" in dbpart_cfg:
            # это для 1.5 тарантулов, пока не было кейса сломанного, но учитывая что их вот вот все спилят
            # то ветка становится не актуальной
            pass
        if "replicationStatus110" in dbpart_cfg:
            # без понятия зачем тут массив, но там всегда? один элемент
            for db_part_status in dbpart_cfg["replicationStatus110"][0].values():
                for direction in ("upstream", "downstream"):
                    if "message" not in db_part_status[direction]:
                        continue

                    if db_part_status[direction]["message"]:
                        bad_msg_detected = True

                    for ignored_message in ignored_tnt_messages:
                        if re.search(ignored_message, db_part_status[direction]["message"]):
                            bad_msg_detected = False
                            break

                    if bad_msg_detected:
                        result["db_ready"] = False
                        result["check_msg"] += f"{direction}: {db_part_status[direction]['message']} "

        return result

    @qacore_decorators
    def change_db_master(self, dbname: str, master: str, expected_code: Optional[int] = 200) -> Optional[Dict]:
        """
        CHANGE DB MASTER

        Args:
            dbname: addrbook # database name
            master: addrbook1 # desired role name for master
            expected_code: 200

        """
        dbcfg = self.dbshards_list.get(dbname)
        cluster_type = self._get_cluster_type(dbname, dbcfg)

        # master not changeable by deployer
        if not cluster_type or not cluster_type.value.get("can_switch_master"):
            return None

        try:
            response = self._request_api(
                "/config/dbshards/master",
                expected_code=expected_code,
                method="post",
                json={
                    "dbName": dbname,
                    "dbShard": 1,
                    "ftType": cluster_type.value.get("ftType"),
                    "members": dbcfg["clusters"]["1"]["members"],
                    "master": master,
                },
            )
        except Exception as exc:
            log.error(f"Cant change master to {dbname}/{master}, please check it: {exc}", extra=FMT_FATAL)
            raise

        resp_json = response.json()
        compare_two_items(
            "status", "in", resp_json, desc=f"Check status field for {fmtstring(dbname)}", log_result=False
        )
        compare_two_items(
            "content", "in", resp_json, desc=f"Check content field for {fmtstring(dbname)}", log_result=False
        )
        compare_two_items(
            resp_json["status"],
            "==",
            expected_code,
            desc=f"Check response code for {fmtstring(dbname)}",
            log_result=False,
        )
        if not resp_json["content"]["updated"]:
            log.warning(f"{dbname} not updated to new master: {master}", extra=FMT_WARN)
        return resp_json

    @qacore_decorators
    def update_config(
        self,
        cfg_update: Dict,
        cfg_file: Optional[str] = None,
        restart: bool = True,
        check: bool = True,
        log_merge: bool = True,
    ) -> None:
        """UPDATE DEPLOYER CONFIG"""
        if cfg_file is None:
            cfg_file = self.cfg_file

        if not os.path.isfile(f"{cfg_file}.original"):
            shutil.copyfile(cfg_file, f"{cfg_file}.original")

        config = load_yaml_file(f"{cfg_file}.original")

        if log_merge:
            log.info(f"Merge new {cfg_file} data:\n" + json.dumps(cfg_update, indent=4), extra=FMT_DEFAULT)

        write_yaml_file(yaml_data=merge_dicts(config, cfg_update), yaml_file=cfg_file)

        if restart:
            self.control_instance("restart", check=check, log_result=True)

    def read_config(self, cfg_file: Optional[str] = None) -> Dict:
        if cfg_file is None:
            cfg_file = self.cfg_file
        return load_yaml_file(cfg_file)

    def restore_config(self, cfg_file: Optional[str] = None) -> None:
        if cfg_file is None:
            cfg_file = self.cfg_file

        if os.path.isfile(f"{cfg_file}.original"):
            shutil.copyfile(f"{cfg_file}.original", cfg_file)

    def get_cluster_by_type(self, clustertype: ClusterType) -> Dict:
        """Возвращает список баз заданного типа"""
        shards_list = self.config_dbshards_list()
        result = {}
        for dbname, dbcfg in shards_list.items():
            # support one shard setup only
            if len(dbcfg["clusters"]) != 1:
                raise FrameworkException(
                    f"Several db shards detected, not supported setup: {fmtstring(dbname)} database"
                )

            if self._get_cluster_type(dbname, dbcfg) != clustertype:
                continue

            result[dbname] = dbcfg
        return result

    def get_storages_roles(self) -> Dict:
        """Возвращает имя стораджа и конфигурацию его ролей"""
        disk_get_url = "/computes/disk/get"
        storages_list_url = "/config/storages/list"
        mescalito_list_url = "/config/storages/mmetad/list"
        # {cloud_name: {"roles": {"role1": {"disks": [1,2]}, "role2":{"disks": [2,3]}} "type": StorageType}}
        result = {}
        # по неизвестной причине эта ошибка может возвращать пустой disksInfo, ретраим
        tries = 3
        for iteration in range(1, tries + 1):
            response = self._request_api(disk_get_url)
            resp_json = response.json()
            if (
                "content" in resp_json
                and "disksInfo" in resp_json["content"]
                and resp_json["content"]["disksInfo"] is not None
            ):
                break
            if sleep_or_exit(f"Bad response from {fmtstring(disk_get_url)}: {resp_json}", iteration, tries, sleep=1):
                continue

        compare_two_items(
            len(resp_json["content"]["disksInfo"]),
            ">",
            1,
            desc=f"Check disksInfo len for {disk_get_url}",
            log_result=False,
        )
        for cloud_name in resp_json["content"]["disksInfo"][0]["available_clouds"]:
            cloud_type = list(filter(lambda st: cloud_name in st.value["storages"], StorageType))
            if not cloud_type:
                raise FrameworkException(f"Unknown storage type: {cloud_name}")
            result[cloud_name] = {"roles": {}, "type": cloud_type[0]}
            response_c = self._request_api(storages_list_url, params={"storage": cloud_name})
            resp_c_json = response_c.json()
            compare_two_items(
                "content",
                "in",
                resp_c_json,
                desc=f"Check content field for {fmtstring(storages_list_url)}",
                log_result=False,
            )
            for pair in resp_c_json["content"]["pairs"].values():
                for disk in pair["disks"]:
                    if disk["hostname"] not in result[cloud_name]["roles"]:
                        result[cloud_name]["roles"][disk["hostname"]] = {"disks": []}
                    result[cloud_name]["roles"][disk["hostname"]]["disks"].append(disk["diskNumber"])

        # Данные по мескалито живут в отдельной апишке, я не смог найти откуда приходят имена, поэтому пока хардкод
        for cloud_name in StorageType.mescalito.value["storages"]:
            result[cloud_name] = {"roles": {}, "type": StorageType.mescalito}
            response_c = self._request_api(mescalito_list_url, params={"storage": cloud_name})
            resp_c_json = response_c.json()
            compare_two_items(
                "content",
                "in",
                resp_c_json,
                desc=f"Check content field for {fmtstring(storages_list_url)}",
                log_result=False,
            )
            # для унификации xtaz кладу в ключ disks, все мескалиты ходят ко всем xtaz, так что эта информация
            # дублируется
            for cluster_cfg in resp_c_json["content"]:
                for worker in cluster_cfg["workers"]:
                    if worker not in result[cloud_name]["roles"]:
                        result[cloud_name]["roles"][worker] = {"disks": []}
                    result[cloud_name]["roles"][worker]["disks"].extend(cluster_cfg["xtazClusters"])

        return result

    def _get_cluster_type(self, dbname: str, dbcfg: Dict) -> ClusterType:
        """
        Определяет тип API по ключу в настройках dbcfg

        Обрабатывает элементы из апи /config/dbshards/list
        """
        detected_cluster = None
        for cluster_type in ClusterType:
            if cluster_type.value["name"] in dbcfg:
                detected_cluster = cluster_type
                break

        if dbname == "orchestrator":
            detected_cluster = ClusterType.orchestrator_itself

        if not detected_cluster:
            raise FrameworkException(f"Unknown database: {dbname}: {dbcfg}")

        return detected_cluster

    def _request_api(
        self,
        path: str,
        tries: int = 3,
        method: str = "get",
        expected_code: Optional[int] = 200,
        timeout: int = 10,
        **kwargs: Any,
    ) -> Response:
        if not path.startswith("/"):
            path = f"/{path}"
        url = f"http://{self.host}:{self.port}/api/v1{path}"
        for iteration in range(1, tries + 1):
            response = None
            try:
                response = getattr(requests, method)(url, timeout=timeout, **kwargs)
            except Exception as exc:
                if sleep_or_exit(f"{url}\nПлохой ответ: {exc}", iteration, tries):
                    continue

            if response is None or not hasattr(response, "status_code"):  # noqa: SIM102
                if sleep_or_exit(f"Api doesn't respond for: {url}", iteration, tries):
                    continue

            if expected_code is None:
                break
            if compare_two_items(response.status_code, "==", expected_code, raise_if_fail=False, log_result=False):
                break

            if sleep_or_exit(
                f"{fmtstring(response.status_code, 'lred')} {fmtstring('NOT')} equal "
                f"{fmtstring(expected_code, 'lred')}, but expected equal",
                iteration,
                tries,
            ):
                continue
        return response

    # @qacore_decorators
    # def search_in_log(self, *args: Any, **kwargs: Any) -> list:
    #     """SEARCH IN DEPLOYER LOG"""
    #     if not args:  # only pattern is passed in the kwargs
    #         if "log_file" not in kwargs:
    #             return search_in_log(log_file=self.log_file, log_position=self.log_position, **kwargs)
    #     elif len(args) == 1:  # only pattern is passed in the args
    #         return search_in_log(log_file=self.log_file, pattern=args[0], log_position=self.log_position, **kwargs)

    #     return search_in_log(*args, log_position=self.log_position, **kwargs)

    # def store_log_position(self, log_file: Optional[str] = None) -> None:
    #     """Store log position for later searching"""
    #     if log_file is None:
    #         log_file = self.log_file

    #     if os.path.isfile(log_file):
    #         self.log_position = os.stat(log_file).st_size

    # def log_test_header(self, msg: str) -> None:
    #     """Write Log test header into log for autotest separate"""
    #     header_str = f"\n\n{'=' * 80}\n"
    #     footer_str = f"\n{'=' * 80}\n"

    #     with open(self.log_file, "a") as logfile_fh:
    #         logfile_fh.write(f"{header_str}{msg}{footer_str}")

    def _get_ssh_key(self) -> str:
        default_key_path = "/tmp/deployer.rsa"
        if os.path.isfile(default_key_path):
            return default_key_path

        deployer_params = self.read_config()
        if "sshKeys" not in deployer_params:
            raise FrameworkException(f"sshKeys not found in the {self.cfg_file}")

        default_key = list(filter(lambda item: item["default"], deployer_params["sshKeys"]))
        if len(default_key) != 1:
            raise FrameworkException(f"Can't find default key in the {self.cfg_file}")

        default_key_body = default_key[0]["keyBodyS"]
        if not default_key_body.endswith("\n"):
            default_key_body += "\n"

        with open(default_key_path, "w", encoding="utf-8") as kfh:
            kfh.write(default_key_body)
        os.chmod(default_key_path, 0o400)

        return default_key_path

    def _get_ssh_user(self) -> str:
        deployer_params = self.read_config()
        if "defaultSSHCredentials" not in deployer_params:
            raise FrameworkException(f"defaultSSHCredentials not found in the {self.cfg_file}")
        return deployer_params["defaultSSHCredentials"]["userName"]

    def __str__(self):
        return f"[{self.host}:{self.port}]"
