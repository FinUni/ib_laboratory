from typing import Optional
from typing import List


class Event:
    class Fields:
        TYPE = "type" # todo: добавь enum с допустимыми типами
        NAME = "name"
        DESCRIPTION = "description"
        VISITORS = "visitors"

        ALL = [
            "type",
            "name",
            "description",
            "visitors"
        ]

        ALLOWED_EVENT_TYPES = [ # todo: сочини allowed_event_types_from_bot
            "adm",
            "FinUn",
            "silent",
            "brainstorm",
            "presentation",
            "blocker", #todo: вспомни что ты тут несла пожалуйста и что ты придумала такое
            "lecture"
        ]

    def __init__(self, type: str, name: str, description: Optional[str], visitors: List[str]):
        assert isinstance(type, str)
        assert type in Event.Fields.ALLOWED_EVENT_TYPES, f"{type} not in {Event.Fields.ALLOWED_EVENT_TYPES}"
        assert isinstance(name, str)
        assert description is None or isinstance(description, str)
        assert isinstance(visitors, list)
        for visitor in visitors:
            assert isinstance(visitor, str)

    


e = Event(type="a", name="my_own_event", description=None, visitors=["me"])