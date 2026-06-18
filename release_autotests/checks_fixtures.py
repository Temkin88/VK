from typing import Optional

import pytest
import allure


@pytest.fixture
def check_event_send_message_event_exist(fetch_until_empty_answer_with_filter):
    def func(opponent_acc, msg_id=None, msg_text=None):
        with allure.step("Проверяем что сообщение доставлено получателю"):
            events = fetch_until_empty_answer_with_filter(opponent_acc, "histDlgState")
            for event in events:
                messages_list = (
                    event["eventData"]["tail"]["messages"]
                    if "tail" in event["eventData"] and "messages" in event["eventData"]["tail"]
                    else []
                )
                messages_list.extend(event["eventData"].get("messages", []))
                for msg in messages_list:
                    if msg_id is not None:
                        msg_ids = msg["msgId"]
                        if msg_id == msg_ids:
                            return True
                    if msg_text is not None:
                        msg_event_text = []
                        if "text" in msg:
                            msg_event_text = msg["text"]
                        elif "parts" in msg:
                            msg_event_text = [
                                part["captionedContent"]["caption"]
                                for part in msg["parts"]
                                if "captionedContent" in part
                            ]
                        if msg_text in msg_event_text:
                            return True
            return False

    return func


@pytest.fixture
def check_message_in_history():
    def func(
        acc,
        sn,
        msg_id: Optional[int | list[int]] = None,
        msg_text: Optional[str | list[str]] = None,
    ):
        msg_ids = [msg_id] if type(msg_id) is int else msg_id
        msg_texts = [msg_text] if type(msg_text) is str else msg_text
        found = False
        history = acc.rapi_getHistory(sn=sn)
        for msg in history["results"]["messages"]:
            # if msg_id is not None and msg_id in msg["msgId"]:
            if msg_id is not None and any(msg_id == int(msg["msgId"]) for msg_id in msg_ids):
                found = True
                break
            if msg_text is not None:
                if "parts" not in msg:
                    continue
                msg_texts_from_history = [part["text"] for part in msg["parts"] if "text" in part]
                if any(msg_text in msg_texts_from_history for msg_text in msg_texts):
                    found = True
                    break
        return found

    return func
