import telebot
from telebot import types
from google_calendar.calendar_api import GoogleCalendar
from typing import List
from shedule.constants import *
from typing import Dict, Any

JsonDict = Dict[str, Any]

#todo: hide buttons after usage
#todo: if not allowed text handeler
#todo: types


bot = telebot.TeleBot('5585832399:AAGg18RRrtMF58x35moa1vSi-vbMc7RK17A')


def load_events():
    return GoogleCalendar()

class MyBrandNewBot:
    def __init__(self):
        self.session_info = {}

def create_buttons_with_names(internal_to_user_names: JsonDict) -> List[types.KeyboardButton]:
    buttons = [types.KeyboardButton(internal_to_user_names[internal_name]) for internal_name in internal_to_user_names]

    return buttons


def get_reply_markup_with_buttons(internal_to_user_names: JsonDict):
    buttons = create_buttons_with_names(internal_to_user_names=internal_to_user_names)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*buttons)

    return markup


def get_next_step(action_type: str, field: str, override: bool):
    pass


def check_event_info(action_type, session_info):


def update_google_event_


@bot.message_handler(commands=['start'])
def main(message):
    msg = bot.send_message(
        chat_id=message.chat.id,
        text='Привет! Выбери пункт из меню, который тебя интересует',
        reply_markup=get_reply_markup_with_buttons(internal_to_user_names=INTERACTION_TYPES),
    )
    bot.register_next_step_handler(msg, choose_interaction_type)


def choose_interaction_type(message):
    chosen_type = message.text
    if chosen_type == INTERACTION_TYPES["create_event"]:
        pass
        # bot.register_message_handler()
    elif chosen_type == INTERACTION_TYPES["get_schedule"]:
        send_message_for_required_date(chat_id=message.chat.id, action_type="get_schedile")


def send_message_for_required_date(chat_id, action_type: str, session_info: JsonDict = {}, override: bool = False):
    message_text = "Пожалуйста, выберите интересующий вас период"
    markup = get_reply_markup_with_buttons(internal_to_user_names=INTERNAL_TO_USER_DATE_NAMES)
    message = bot.send_message(
        chat_id=chat_id,
        text=message_text,
        reply_markup=markup
    )
    bot.register_next_step_handler(message, save_required_date,action_type, session_info, override)


def save_required_date(msg, action_type, session_info: JsonDict, override: bool):
    session_info["required_date"] = msg.text

    if action_type=="get_schedule":
        print("мы типо посмотрели расписание, вот какие мы молодцы")
    elif action_type=="create_event":
        print("мы тут тоже смотрим расписание, но ещё и делаем так")
        send_message_for_event_type(msg.chat_id, action_type="create_event", )


def get_field_send_message(msg, action_type, session_info, field: str, override):
    message_text = "Пожалуйста, выберите интересующий вас" + field  # todo: move this to constants
    markup = get_reply_markup_with_buttons(internal_to_user_names=INTERNAL_TO_USER[field])
    message = bot.send_message(
        chat_id=msg.chat_id,
        text=message_text,
        reply_markup=markup
    )
    bot.register_next_step_handler(message, save_field_to_session_info, action_type, session_info, field, override)


def save_field_to_session_info(msg, action_type, session_info, field, override):
    session_info[field] = msg.text
    print(session_info)
    eval(get_next_step(action_type, field, override))


# @bot.message_handler(commands=['start'])
# def main(message):
#     msg = bot.send_message(message.chat.id, 'Введите интересующий вас день в формате 2022-07-25') #todo: calendar via buttons
#     bot.register_next_step_handler(msg, date)
#
#
# def date(message):
#     session_info = {}
#     session_info["date"] = message.text
#     print(session_info)
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = []
#     for event_type in BOT_EVENT_TYPES:
#         buttons.append(types.KeyboardButton(EVENTS_TO_HUMAN_NAMES[event_type]))
#     markup.add(*buttons)
#     bot.send_message(message.chat.id,
#                      text="Выберите интересующий вас тип мероприятия".format(
#                          message.from_user), reply_markup=markup) #todo: automatically resize buttons
#
#     bot.register_next_step_handler(message, time_period, session_info)
#
#
# def time_period(message, session_info):
#     session_info["type"] = message.text
#     print(session_info)
#
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     buttons = []
#     for bot_allowed_action in BOT_ALLOWED_ACTIONS:
#         buttons.append(types.KeyboardButton(bot_allowed_action))
#     markup.add(*buttons)
#     bot.send_message(message.chat.id,
#                      text="Желаемый тип".format(
#                          message.from_user), reply_markup=markup)  # todo: automatically resize buttons
#     bot.register_next_step_handler(message, options, session_info)
#
#
# def options(message, session_info):
#     session_info["required_action"] = message.text
#     print(session_info)
#
#     already_existing_events = load_events()
#     for event in already_existing_events:
#         print(event)
#
#
if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
#
