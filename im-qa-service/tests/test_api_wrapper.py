import allure
import pytest

from web.project.v1.account import OutAccountModel
from web.project.api_wrapper import DesktopClient


account_dict = {
    "product": "myteam_onpremise",
    "type": "myteam_on_premise",
    "phone": None,
    "code": None,
    "uin": "autotest10@im-auto.hb.bizmrg.com",
    "password": "twelve",
    "api_url": "https://u-im-testing.v3.im-sandbox.devmail.ru"
}
account_dantic = OutAccountModel(**account_dict)


@pytest.fixture(scope="module")
@allure.title("Фикстура тестового аккаунта")
async def account():
    """
    Фикстура создания класса с тестовым аккаунтом
    """
    with allure.step("Создаем объект класса DesktopClient"):
        account = DesktopClient(**account_dantic.dict())
        await account.__aenter__()
    yield account
    with allure.step("Деструктор DesktopClient"):
        await account.wim_aim_endSession()
        await account.session.__aexit__()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Авторизация")
@allure.title("Проверяем работу обертки над API с аккаунтом от ICQ")
async def test_icq_client():
    """
    Проверяем работу обертки над API с аккаунтом от ICQ
    """
    acc_dict = {
        "type": "icq",
        "phone": "+9999202003203",
        "code": "402457",
        "uin": None,
        "password": None,
        "api_url": "https://u.icq.net"
    }
    acc_dantic = OutAccountModel(**acc_dict)
    async with DesktopClient(**acc_dantic.dict()) as client:
        assert client.phone


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Сообщения")
@allure.title("Проверка отправки реплая через API")
async def test_reply_message(account: DesktopClient):
    """
    Проверка отправки реплая через API
    """
    response = await account.reply_message(
        sn=account.uin,
        author_sn=account.uin,
        quote="Quote",
        text='Text'
    )

    assert isinstance(response, int) or response is None


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Сообщения")
@allure.title("Проверка отправки форварда через API")
async def test_forward_message(account: DesktopClient):
    """
    Проверка отправки форварда через API
    """
    response = await account.forward_message(
        sn=account.uin,
        old_sn=account.uin,
        author_sn=account.uin,
        quote="Quote",
        text='Text',
        msg_id=1
    )

    assert isinstance(response, int) or response is None


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Сообщения")
@allure.title("Проверка отправки обычного сообщения через API")
async def test_send_basic_message(account: DesktopClient):
    """
    Проверка отправки обычного сообщения через API
    """
    response = await account.send_basic_message(
        sn=account.uin,
        text='Text'
    )

    assert isinstance(response, int)


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Чаты")
@allure.title("Проверка удаления последних чатов через API")
async def test_delete_last_groups(account: DesktopClient):
    """
    Проверка удаления последних чатов через API
    """
    assert await account.delete_last_groups()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Чаты")
@allure.title("Проверка удаления последних черновиков через API")
async def test_delete_last_drafts(account: DesktopClient):
    """
    Проверка удаления последних черновиков через API
    """
    assert await account.delete_last_drafts(
        chat=account.uin
    )


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Статус")
@allure.title("Проверка удаления последнего статуса через API")
async def test_set_empty_status(account: DesktopClient):
    """
    Проверка удаления последнего статуса через API
    """
    response = await account.set_empty_status()
    assert isinstance(response, dict)


@pytest.mark.skip
@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Настройки приватности")
@allure.title("Проверка очистки blacklist через API")
async def test_clear_contacts_black_list(account: DesktopClient):
    """
    Проверка очистки blacklist через API
    """
    assert await account.clear_contacts_black_list()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Настройки приватности")
@allure.title("Проверка очистки deny_list через API")
async def test_clear_deny_list(account: DesktopClient):
    """
    Проверка очистки deny_list через API
    """
    assert await account.clear_deny_list()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Чаты")
@allure.title(
    "Проверка установки прочитанности "
    "на последние полученные сообщения через API"
)
async def test_read_last_msg(account: DesktopClient):
    """
    Проверка установки прочитанности на последние полученные сообщения через API
    """
    assert await account.read_last_msg()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Настройки приватности")
@allure.title("Проверка установки настроек приватности через API")
async def test_restore_privacy_settings(account: DesktopClient):
    """
    Проверка установки настроек приватности через API
    """
    assert await account.restore_privacy_settings()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Чаты")
@allure.title("Проверка получение stamp чата через API")
async def test_get_chat_stamp(account: DesktopClient):
    """
    Проверка получение stamp чата через API
    """
    assert (await account.get_chat_stamp(account.uin)) is None


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Чаты")
@allure.title("Проверка создания чата через API")
async def test_create_chat(account: DesktopClient):
    """
    Проверка создания чата через API
    """
    assert await account.create_chat(account.uin)


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Чаты")
@allure.title("Проверка редактирования чата через API")
async def test_mod_chat(account: DesktopClient):
    """
    Проверка редактирования чата через API
    """
    chatId = await account.create_chat(account.uin)

    response = await account.mod_chat(
        sn=chatId,
        name=2 * account.uin
    )

    assert isinstance(response, dict)


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Classmethods")
@allure.title("Проверка __str__ обертки API")
async def test__str__(account: DesktopClient):
    assert account.__str__()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Classmethods")
@allure.title("Проверка __repr__ обертки API")
async def test__repr__(account: DesktopClient):
    assert account.__repr__()


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Classmethods")
@allure.title("Проверка ctx_manager_sync обертки API")
async def test_ctx_manager_sync():
    with DesktopClient(**account_dantic.dict()) as ac:
        assert ac.uin


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Classmethods")
@allure.title("Проверка ctx_manager_async обертки API")
async def test_ctx_manager_async():
    async with DesktopClient(**account_dantic.dict()) as ac:
        assert ac.uin


@pytest.mark.anyio
@allure.suite("Тесты обертки над API ICQ/VK Teams")
@allure.feature("Classmethods")
@allure.title("Проверка ошибок ctx_manager_async обертки API")
async def test_ctx_manager_async_error():
    with pytest.raises(AssertionError):
        async with DesktopClient(**{}):
            pass
