from __future__ import annotations

from urllib.parse import urlparse

import pytest

from pyvkteamsclient.survey import MiniAppClient


@pytest.fixture(scope="session")
def opponent_survey_miniapp(
    ENV_PLATFORM,
    get_myteam_config,
    opponent_account,
    session,
):
    for miniapp in filter(
        lambda x: x["name"] == "Опросы",
        get_myteam_config.get("custom-miniapps", []),
    ):
        url = urlparse(miniapp["url"])

        return MiniAppClient(
            session=session,
            miniapps_api_url="{url.scheme}://{url.hostname}".format(url=url),
            account=opponent_account,
        )
    else:
        pytest.skip("No Survey Pro miniapp")
