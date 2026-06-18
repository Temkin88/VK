from datetime import datetime


class EventFilter(object):
    def __init__(self):
        self.start: datetime = datetime.now()

    def __str__(self):
        return f"<EventFilter(start={self.start})>"

    def __repr__(self):
        return self.__str__()

    def start_point(self):
        self.start = datetime.now()

    def __call__(self, events: list[dict], *event_type: str):
        for event in events:
            if event["timestamp"] >= self.start:
                if not event_type:
                    yield event
                else:
                    if event["type"] in event_type:
                        yield event
