import pytest


@pytest.fixture(scope="session", autouse=True)
def is_bots_in_threads_enabled(bots_in_threads_enabled):
    if not bots_in_threads_enabled:
        pytest.skip("Bots in threads are disabled in this environment")
