import datetime

import telebot
from typing import Union
from telebot import types
from telebot.types import Message
from google_calendar.calendar_api import GoogleCalendar
from typing import List
from shedule.constants import *
from typing import Dict, Any


JsonDict = Dict[str, Any]
SECONDS_IN_HOUR = 60 * 60

#todo: if not allowed text handeler
#todo: typing
#todo: auto resize buttons
#todo: actual remove session_info


bot = telebot.TeleBot('5585832399:AAGg18RRrtMF58x35moa1vSi-vbMc7RK17A')
LAST_UPDATED_TS = None


def send_notifications(chat_ids, text):
    for chat_id in chat_ids:
        bot.send_message(
            chat_id=chat_id,
            text=text
        )


def visualise(session_info):
    for field in REQUIRED_FIELDS:
        if not session_info.get(field):
            # todo: send_notifications(admins_chat_ids, text)
            assert False, "мы всё уронили, найс"

    return f"Тебя интересует {INTERNAL_TO_USER['event_type'][session_info['event_type']]} {session_info['date']} в {session_info['time']}"


def internal_to_user_transpose_by_type(requested_field: str):
    internal_to_user_by_type = INTERNAL_TO_USER[requested_field]
    user_to_internal = {internal_to_user_by_type[internal]: internal for internal in internal_to_user_by_type}

    return user_to_internal


def load_events(message, session_info):
    override = False
    date = session_info["date"]
    GoogleCalendar(date)

    command = get_next_step(session_info["interaction_type"], "SEND_SCHEDULE", False, session_info)
    eval(command)


def _create_buttons_with_names(internal_to_user_names: Union[JsonDict, List[str]]) -> List[types.KeyboardButton]:
    button_names = []
    if isinstance(internal_to_user_names, list):
        button_names = internal_to_user_names
    else:
        button_names = [types.KeyboardButton(internal_to_user_names[internal_name]) for internal_name in internal_to_user_names]
    buttons = button_names

    return buttons


def get_reply_markup_with_buttons(internal_to_user_names: Union[JsonDict, List[str]]):
    buttons = _create_buttons_with_names(internal_to_user_names=internal_to_user_names)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(*buttons)

    return markup


def get_possible_time(message, session_info):
    possible_time = []
    events = GoogleCalendar(session_info["date"])

    for time in TIME_BEGINNERS:
        possible_time.append(time)

    session_info["possible_time"] = possible_time
    get_field_send_message(message, requested_field="time", session_info=session_info)  # todo: get_next_step


def get_python_command(required_action: List[str], session_info) -> str:
    if len(required_action) == 1:
        if required_action[0] == "CHECK":
            return "check_event_info(message=message, session_info=session_info)"
        elif required_action[0] == "SEND_SCHEDULE":
            return f"load_events(message, session_info)"  # todo: refactor google calendar part
        elif required_action[0] == "POSSIBLE_TIME":
            return f"get_possible_time(message, session_info)"
    else:
        return f"""get_field_send_message(
            msg=message, 
            requested_field="{required_action[1]}", 
            session_info=session_info, 
            override=override
        )"""


def extract_next_step(interaction_type, last_action):
    override = (interaction_type == "get_schedule")
    for step_and_next_step in NEXT_STEP:
        if step_and_next_step[0] == [interaction_type, last_action]:
            return step_and_next_step[1], override
    return None, False



def get_next_step(interaction_type:str, last_action: str, override: bool = False, session_info: JsonDict = {}) -> str:
    if override:
        return "check_event_info()" # todo: норм параметры

    next_step, override = extract_next_step(interaction_type=interaction_type, last_action=last_action)

    while not override and len(next_step) > 1 and next_step[1] in session_info:
        next_step, override = extract_next_step(interaction_type=interaction_type, last_action=next_step[1])

    if override:
        session_info = {}
    return get_python_command(next_step, session_info)


def check_event_info(message, session_info):
    event_info = visualise(session_info)
    markup = get_reply_markup_with_buttons(["да", "нет"])

    bot.send_message(
        chat_id=message.chat.id,
        text=MESSAGE_TEXT["check"] + event_info,
        reply_markup=markup
    )
    bot.register_next_step_handler(message, work_with_check_info, session_info)


def update_calendar_event(session_info):
    print("congrats, event updated")
    pass


def work_with_check_info(message, session_info):
    telebot.types.ReplyKeyboardRemove()
    message_text = message.text
    if message_text == "да":
        update_calendar_event(session_info)# todo
    else:
        for field in REQUIRED_FIELDS:
            del session_info[field]
        bot.register_next_step_handler(message, get_field_send_message, "event_type", session_info)


def google_calendar_description_to_json(descr: str) -> JsonDict:
    descr = descr.split("\n")
    description = {}
    for element in descr:
        first_space_ind = descr.find(" ")
        description[:first_space_ind] = descr[first_space_ind + 1:]

    return  description


def session_info_to_event(session_info: JsonDict = None): # todo
    return ""


def update_lab_schedule_by_ruz():
    pass

def resolve_schedule_conflicts():
    all_events = GoogleCalendar()
    print(1)
    for event in all_events:
        event.description = google_calendar_description_to_json()

    time_to_events = {}
    for event in all_events:
        current_event_start_time = datetime.datetime(event["start"]["dateTime"]).timestamp()
        if current_event_start_time not in time_to_events:
            time_to_events[current_event_start_time] = []
        time_to_events[current_event_start_time].append(event)

    for time in time_to_events:
        events = time_to_events[time]
        events = events.sort(
            key=EVENT_TYPES_PRIORITY.get(event["description"].get("event_type"), 0),
            reverse=True
        )

        for i in range(1, len(events)):
            send_notifications(chat_ids=events[i]["description"].get("chat_ids"), text=MESSAGE_TEXT["cancel"])


@bot.message_handler(commands=['start'])
def main(message):
    resolve_schedule_conflicts()
    global LAST_UPDATED_TS

    timestamp_now = datetime.datetime.now().timestamp()

    if not LAST_UPDATED_TS or abs(timestamp_now - LAST_UPDATED_TS) > SECONDS_IN_HOUR:
        update_lab_schedule_by_ruz()
        resolve_schedule_conflicts()
        LAST_UPDATED_TS = timestamp_now

    msg = bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Выбери пункт из меню, который тебя интересует',
        reply_markup=get_reply_markup_with_buttons(internal_to_user_names=INTERNAL_TO_USER["interaction_type"]),
    )
    bot.register_next_step_handler(msg, save_field_to_session_info, "interaction_type")


def get_field_send_message(msg, requested_field, session_info, override=False):
    message_text = MESSAGE_TEXT[requested_field]

    if INTERNAL_TO_USER.get(requested_field) or session_info.get("possible_" + requested_field):
        internal_to_user_names = INTERNAL_TO_USER.get(requested_field) or session_info.get("possible_" + requested_field)
        markup = get_reply_markup_with_buttons(internal_to_user_names=internal_to_user_names)
        message = bot.send_message(
            chat_id=msg.chat.id,
            text=message_text,
            reply_markup=markup
        )
    else:
        message = bot.send_message(
            chat_id=msg.chat.id,
            text=message_text
        )
    bot.register_next_step_handler(message, save_field_to_session_info, requested_field, session_info, override)


def save_field_to_session_info(message: Message, requested_field: str, session_info: JsonDict = {}, override: bool = False):
    telebot.types.ReplyKeyboardRemove(selective=None)
    message_text = message.text
    session_info[requested_field] = message_text


    if INTERNAL_TO_USER.get(requested_field):
        USER_TO_INTERNAL = internal_to_user_transpose_by_type(requested_field)
        if message_text in USER_TO_INTERNAL:
            session_info[requested_field] = USER_TO_INTERNAL[message_text]
        else:
            # todo: to previous block
            pass
    print(session_info)

    command = get_next_step(session_info["interaction_type"], requested_field, override, session_info)
    eval(command)


if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
