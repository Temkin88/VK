import uuid

import requests
from bs4 import BeautifulSoup


def main():
    """

    """
    with requests.Session() as session:
        response = session.get(url="https://omicron.mail.ru/login/sys-oauth2/", allow_redirects=True)

        response = session.get(
            url="https://auth.vkteam.ru/chunks/login_form_mtls/", allow_redirects=False,
        )

        response = session.post(
            url="https://auth.vkteam.ru/login/api/check_password/", allow_redirects=False,
            json={
               "auth_type": "domain",
               "username": "a.zakhtarenko",
               "password": "9MrBXZ_PK3Zm!",
            }
        )

        # response = session.get(
        #     url=response.headers["location"],  # noqa
        # )
        #
        # response = session.get(
        #     url=response.url,
        #     allow_redirects=False,
        # )

        # response = session.get(
        #     url=response.headers["location"],  # noqa
        # )

        session.post(
            url="https://omicron.mail.ru/api/v2/apps/",
            headers={"Content-Type": "application/json"},
            json={"page": 1, "page_size": 100},
            cookies=session.cookies
        )

if __name__ == "__main__":
    main()