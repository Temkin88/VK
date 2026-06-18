import allure
import pytest


@allure.title("Получение реакции для сообщения")
@pytest.fixture(
    params=[
        ["👍", "❤️", "🤣"],
    ]
)
def reactions_fixt(request):
    return request.param
