from pyvkteamsclient.client import DesktopClient


def keywords_iterator(full_keyword: str, step_count: int) -> iter:
    if step_count == 1:
        keywords = [full_keyword]
    else:
        limit_step = round(len(full_keyword) / step_count)
        keywords = [full_keyword[: limit_step * i] for i in range(1, step_count)]
        keywords.append(full_keyword[: len(full_keyword) - 2])
    return iter(keywords)


def user_in_search_result(search_result: dict, user: DesktopClient) -> bool:
    persons = search_result["results"]["persons"]
    return any(person["sn"] == user.uin for person in persons)
