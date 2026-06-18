import uuid


from pyvkteamsclient.client import DesktopClient


def get_user_full_name(target, email) -> str:
    response = target.rapi_getUserInfo(sn=email)
    results = response["results"]

    return " ".join([results.get(element, "") for element in ["firstName", "lastName", "middleName"]])


def get_remote_sn_from_buddylist_event(events: list, chat_name: str) -> str | None:
    for event in events:
        for group in event["eventData"]["groups"]:
            for buddy in group["buddies"]:
                if buddy["friendly"] == chat_name:
                    return buddy["aimId"]
    return None


def get_remote_sn_from_histDlgState_events(events: list, chat_name: str) -> str | None:
    for event in events:
        for person in event["eventData"]["persons"]:
            if person["friendly"] == chat_name:
                return person["sn"]
    return None


def generate_uniq_chat_name(init_name: str) -> str:
    return init_name + "" + str(uuid.uuid4())[:6]


def find_chat_by_some_criterion(acc: DesktopClient, chat_name: str, criterions=None) -> str | None:
    if criterions is None:
        criterions = {}
    if "name" not in criterions:
        criterions["name"] = chat_name
    search_results = acc.rapi_search(chat_name)
    assert search_results["status"]["code"] == 20000, "Не удалось произвести поиск"
    if "chats" not in search_results["results"]:
        return None
    for chat in search_results["results"]["chats"]:
        found = True
        for key, value in criterions.items():
            if key not in chat and value:
                found = False
                break
            elif key not in chat and not value:
                continue
            elif chat[key] != value:
                found = False
                break
        if found:
            return chat["sn"]
    return None


def deep_search_key_in_collection(collection: dict | list, target_key: str, target_value) -> bool:
    """рекурсивно ищем ключ-значение во всем джейсоне"""
    result = False
    if isinstance(collection, list):
        for element in collection:
            if isinstance(element, dict | list):
                result = result or deep_search_key_in_collection(element, target_key, target_value)
    elif isinstance(collection, dict):
        for key in collection:
            if isinstance(collection[key], dict | list):
                result = result or deep_search_key_in_collection(collection[key], target_key, target_value)
            elif key == "isFederation" and collection[key] == target_value:
                result = True
    return result


def find_events_with_is_federation_true(events) -> list[str]:
    result = []
    for event in events:
        if deep_search_key_in_collection(event, "isFederation", True):
            result.append(event["type"])
    return result


def check_event_with_federation_list(event_types_with_is_federation_true_value):
    if not event_types_with_is_federation_true_value:
        return False
    return all(
        event_type in ["federation", "buddylist", "diff"]
        for event_type in event_types_with_is_federation_true_value
        if event_types_with_is_federation_true_value
    )
