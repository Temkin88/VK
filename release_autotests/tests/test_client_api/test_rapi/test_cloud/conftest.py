import pytest


@pytest.fixture(scope="session", autouse=True)
def is_cloud_enabled(save_to_cloud_enabled):
    if not save_to_cloud_enabled:
        pytest.skip("Cloud is disabled in this env")
