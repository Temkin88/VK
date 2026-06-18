import re

import allure
import logging

from support.markers import SANDBOX
from imcommonsupplyclient import voip


logger = logging.getLogger(__name__)


def check_log_for_string(
    param_name: str,
    log: str,
):
    with allure.step(f"Проверяем наличие в логе записей о {param_name}"):
        search_result = re.search(f'("{param_name}":")([a-z0-9]*)"', log)
        assert search_result is not None, f"{param_name} должен присутствовать в логах"
        assert len(search_result.groups()) > 0, f"{param_name} должен быть не пустым"

        logger.info(f"Success: {param_name}")

        return True


@SANDBOX
@allure.id("250075")
@allure.label("layer", "voip_layer")
@allure.severity(allure.severity_level.MINOR)
@allure.suite("Звонки")
@allure.feature("Записи в логе")
@allure.title("Версии focus/janus в voip логе")
def test_focus_janus_hashes(get_voip_bots):
    """
    Проверка что с voip-логе записаны следующие параметры:
    - focus-commit-hash
    - focus-config-hash
    - janus-commit-hash
    - janus-config-hash
    """

    with allure.step("Получение VoIP-ботов"):
        bots = get_voip_bots(2)

        first_bot, second_bot = bots

    with allure.step("Сгенерировать ссылку на звонок с любого из клиентов"):
        call_link = first_bot.create_conference().conferenceUrl

    with allure.step("Зайти по ссылке в звонок двумя участниками"):
        calls = []
        for bot in bots:
            calls.append(bot.make_call_by_link(call_link=call_link, with_video=False))

        voip.cross_check_participants(calls=calls, participants=bots, microphone_on=True, camera_on=False)

    with allure.step("Завершить звонок на каждой стороне"):
        voip.bulk_hang_up(calls)

    with allure.step(
        "В VOIP-логах найти следующие параметры и убедиться, что они не пусты: focus-commit-hash, "
        "focus-config-hash, janus-commit-hash, janus-config-hash"
    ):
        log = first_bot.get_voip_log()

        assert all(
            check_log_for_string(param_name=param_name, log=log)
            for param_name in ["focus-commit-hash", "focus-config-hash", "janus-commit-hash", "janus-config-hash"]
        )
