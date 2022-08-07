from typing import Optional
from typing import Any
from typing import Dict

JsonDict = Dict[str, Any]

ALL = [
    "type",
    "name",
    "description",
    "visitors"
]

EVENT_TYPES = [  # todo: сочини allowed_event_types_from_bot
    "adm",
    "FinUn",
    "silent",
    "brainstorm",
    "presentation",
    "blocker",  # todo: вспомни что ты тут несла пожалуйста и что ты придумала такое
    "lecture"
]


def convert_string_description_to_jsondict(description: Optional[str]) -> Optional[JsonDict]:
    if not description:
        return None  # todo: parse description based on name? # todo:

    return {description_item[:description_item.find(" ")]: eval(description_item[:description_item.find(" ")])
            for description_item in description.split("\n")}


def convert_jsondict_description_to_string(description: Optional[JsonDict]) -> Optional[str]:
    return "\n".join(["--" + key + " " + str(description[key]) for key in description])
