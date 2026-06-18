import pytest


VKTI = pytest.mark.VKTI
PRE_VKTI = pytest.mark.PRE_VKTI
SAAS = pytest.mark.SAAS
PRE_SAAS = pytest.mark.PRE_SAAS
TARM = pytest.mark.TARM
PRE_TARM = pytest.mark.PRE_TARM
SANDBOX = pytest.mark.SANDBOX
IDM = pytest.mark.IDM
SLA = pytest.mark.SLA
DLP = pytest.mark.DLP
ISOLATION = pytest.mark.ISOLATION

PRODUCT_FUNCTIONALITY = lambda *x: pytest.Mark(  # noqa: E731
    name="allure_label", args=(*x,), kwargs={"label_type": "product_functionality"}
)
