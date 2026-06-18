import allure
import pytest

from support.markers import VKTI, PRE_VKTI, SAAS, TARM, PRE_TARM, SANDBOX, PRE_SAAS


@pytest.fixture(scope="session")
def uploaded_image_id(auth_account, with_preview_file):
    with allure.step("Пытаемся загрузить файл"):
        file_id, _ = auth_account.upload_file(
            str(with_preview_file.absolute()),
        )

        yield file_id


@allure.id("38601")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("Превью файлов")
@allure.title("Получение превью файла по ID")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "preview_size",
    [
        192,
        194,
        400,
        600,
        800,
        "small",
        "medium",
        "large",
        "xlarge",
        "iphone",
        "iphone_retina",
        "mdpi",
        "hdpi",
        "xhdpi",
        "xxhdpi",
        "share",
    ],
)
def test_file_preview_max(
    auth_account,
    uploaded_image_id,
    preview_size,
):
    with allure.step("Делаем запрос превью"):
        auth_account.files_preview_max(
            file_id=uploaded_image_id,
            size=preview_size,
        )


@allure.id("75347")
@allure.label("layer", "api_layer")
@allure.severity(allure.severity_level.NORMAL)
@allure.suite("Файлы")
@allure.feature("Превью файлов")
@allure.title("Получение превью файла по ID")
@VKTI
@PRE_VKTI
@SAAS
@PRE_SAAS
@TARM
@PRE_TARM
@SANDBOX
@pytest.mark.parametrize(
    "preview_size",
    [
        192,
        194,
        400,
        600,
        800,
        "small",
        "medium",
        "large",
        "xlarge",
        "iphone",
        "iphone_retina",
        "mdpi",
        "hdpi",
        "xhdpi",
        "xxhdpi",
        "share",
    ],
)
def test_file_preview_ttl(
    auth_account,
    uploaded_image_id,
    preview_size,
):
    with allure.step("Получаем hash ttl файла"):
        file_info = auth_account.get_file_info(uploaded_image_id)
        hash_ttl_file = file_info["info"]["dlink"].split("get/")[1].split("/")[0]

    with allure.step("Делаем запрос превью ttl"):
        response = auth_account.files_preview_ttl(
            ttl_hash=hash_ttl_file,
            size=preview_size,
        )
        assert response.status_code == 200 or response.status_code == 204, "Response code error"
