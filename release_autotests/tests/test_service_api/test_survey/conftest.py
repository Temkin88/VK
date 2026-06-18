from __future__ import annotations
import allure
import pytest

import uuid
from random import randint
from urllib.parse import urlparse
from pyvkteamsclient.survey import MiniAppClient
from pyvkteamsclient.client import DesktopClient


@pytest.fixture(scope="session")
def survey_miniapp(ENV_PLATFORM, get_myteam_config, auth_account, session, main_api):
    if ENV_PLATFORM == "SAAS":
        return MiniAppClient(
            session=session,
            miniapps_api_url="https://miniapp-6142f594-cb8a-4989-9579-25d37b1d3f7b.miniapps.myteam.mail.ru",
            account=auth_account,
        )

    for miniapp in filter(
        lambda x: x["name"] == "Опросы",
        get_myteam_config.get("custom-miniapps", []),
    ):
        url = urlparse(miniapp["url"])

        return MiniAppClient(
            session=session,
            miniapps_api_url="{url.scheme}://{url.hostname}".format(url=url),
            account=auth_account,
        )
    else:
        pytest.skip("No Survey Pro miniapp")


@pytest.fixture(scope="session")
def survey_miniapp_another_domain(
    ENV_PLATFORM, get_myteam_config, session, imap_serv, accounts_data, main_api, binary_api, pytestconfig
):
    sandbox = pytestconfig.getoption("--sandbox")
    if ENV_PLATFORM == "SAAS":
        account = accounts_data[2]

        another_domain = DesktopClient(
            uin=account.get("uin") or account.get("username"),
            session=session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=125,
            env="SAAS",
            email_password=account["password"],
            email_url=imap_serv,
            polling=False,
        )
    elif sandbox == "imserver-19606-el7.v3.im-sandbox.devmail.ru":
        another_domain = DesktopClient(
            uin="pwd003@survey.clients",
            session=session,
            api_url=main_api,
            binary_api_url=binary_api,
            api_ver=125,
            env="SANDBOX",
            fix_otp="ONPREM",
        )
    else:
        pytest.skip("No Survey two domain")

    return MiniAppClient(
        session=session,
        miniapps_api_url="https://miniapp-6142f594-cb8a-4989-9579-25d37b1d3f7b.miniapps.myteam.mail.ru",
        account=another_domain,
    )


@pytest.fixture(scope="session")
def create_survey(
    survey_miniapp,
    photo_id,
):
    with allure.step("Создаем опрос"):
        response = survey_miniapp.internal_survey_create(
            sender_sn=survey_miniapp.account.uin,
            name=f"Test survey {uuid.uuid4().hex}",
            image=photo_id,
            flags=["nonanonymous"],
        )
        assert response["status"]["code"] == 20000, "Error status code"

    with allure.step("Проверяем что опрос создался"):
        survey_list = survey_miniapp.internal_survey_list(sender_sn=survey_miniapp.account.uin)
        assert any(
            response["results"]["surveyId"] in survey["surveyId"] for survey in survey_list["results"]["surveys"]
        )

    yield response

    with allure.step("Если опрос активен, тогда останавливаем опрос"):
        survey_action = survey_miniapp.account.rapi_survey_get(
            survey_id=response["results"]["surveyId"],
        )

        if survey_action["results"]["active"]:
            survey_miniapp.internal_survey_stop(
                sender_sn=survey_miniapp.account.uin,
                survey_id=response["results"]["surveyId"],
            )

    with allure.step("Удаляем опрос"):
        survey_miniapp.internal_survey_delete(
            sender_sn=survey_miniapp.account.uin,
            survey_id=response["results"]["surveyId"],
        )


@pytest.fixture(scope="session")
def survey_id(create_survey):
    return create_survey["results"]["surveyId"]


@pytest.fixture(scope="session")
def survey_start(
    survey_miniapp,
    survey_id,
    question_id,
):
    survey_miniapp.internal_survey_targets_add(
        sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
    )

    return survey_miniapp.internal_survey_start(
        sender_sn=survey_miniapp.account.uin,
        survey_id=survey_id,
        targets=[survey_miniapp.account.uin],
    )


@pytest.fixture(scope="session")
def create_questions_survey(
    survey_miniapp,
    survey_id,
):
    survey_action = survey_miniapp.account.rapi_survey_get(
        survey_id=survey_id,
    )

    if survey_action["results"]["active"]:
        survey_miniapp.internal_survey_stop(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
    with allure.step("Создаем вопрос"):
        response = survey_miniapp.internal_survey_questions_create(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            name="Какой язык программирования вы предпочитаете?",
            number=randint(1, 100),
            typeQuestion="single",
            flags=["many", "own_version"],
            values=[
                "C++",
                "Java",
                "Golang",
                "Python",
            ],
        )
    return response


@pytest.fixture(scope="session")
def question_id(create_questions_survey):
    return create_questions_survey["results"]["questionId"]


@pytest.fixture(scope="session")
def create_questions_all_types(
    survey_miniapp,
    photo_id,
):
    response = survey_miniapp.internal_survey_create(
        sender_sn=survey_miniapp.account.uin,
        name=f"Test survey {uuid.uuid4().hex}",
        image=photo_id,
        flags=["nonanonymous"],
    )
    survey_id = response["results"]["surveyId"]

    type_question = {
        "single": None,
        "scale": None,
        "open": None,
        "yesNo": None,
        "pleasure": None,
    }

    with allure.step("Пытаемся создать вопрос"):
        for question in type_question:
            params: dict[str, list[str] | int | str | dict[str, [int, str]]] = {
                "number": randint(1, 100),
                "typeQuestion": question,
                "flags": ["many", "own_version"],
                "values": None,
            }

            if question == "single":
                params["values"] = [
                    "C++",
                    "Java",
                    "Golang",
                    "Python",
                ]
            elif question == "scale":
                params["values"] = {
                    "min": [1, "Не нравится!"],
                    "max": [10, "Обожаю!"],
                }
            elif question == "open":
                params["values"] = "Your personal variant"
            elif question == "yesNo":
                params["values"] = False
            elif question == "pleasure":
                params["values"] = [
                    "!-_-! Совершенно удовлетворен",
                    "!-_-! Удовлетворен",
                    "!-_-! Не знаю",
                    "!-_-!  Не удовлетворен",
                    "!-_-! Абсолютно не удовлетворен",
                ]
            else:
                raise ValueError(f"Unknown survey question type: {question}")

            response = survey_miniapp.internal_survey_questions_create(
                sender_sn=survey_miniapp.account.uin,
                survey_id=survey_id,
                name="Какой язык программирования вы предпочитаете?",
                **params,
            )

            type_question[question] = response["results"]["questionId"]

    return survey_id, type_question


@pytest.fixture(scope="session")
def get_survey_vote(survey_miniapp, create_questions_all_types):
    survey_id, questions_all = create_questions_all_types

    response = survey_miniapp.account.rapi_survey_get(
        survey_id=survey_id,
    )
    results_active = response["results"]["active"]

    if not results_active:
        survey_miniapp.internal_survey_targets_add(
            sender_sn=survey_miniapp.account.uin, survey_id=survey_id, sn_list=[survey_miniapp.account.uin]
        )
        survey_miniapp.internal_survey_start(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
            forwarding=True,
            targets=[survey_miniapp.account.uin],
        )

    value = [1, 2, 3, "Your personal variant"]
    question_id = questions_all["single"]

    with allure.step("Пробуем проголосовать"):
        survey_miniapp.account.rapi_survey_vote(
            survey_id=survey_id,
            question_id=question_id,
            value=value,
        )

    return survey_id, question_id


@pytest.fixture(scope="function")  # noqa PT003
def check_action(survey_miniapp, survey_id):
    survey_action = survey_miniapp.account.rapi_survey_get(
        survey_id=survey_id,
    )

    if survey_action["results"]["active"]:
        survey_miniapp.internal_survey_stop(
            sender_sn=survey_miniapp.account.uin,
            survey_id=survey_id,
        )
