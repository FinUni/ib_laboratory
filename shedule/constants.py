INTERACTION_TYPES_TO_NEXT_STEP = {
    "get_schedule": "",
    "add_presence": "",
}

# todo: хочу выпилить функциональность

INTERNAL_TO_USER = {

    "interaction_type": {
        "get_schedule": "Посмотреть расписание",
        "add_presence": "Записаться"  # todo: мне не нравится, как тут звучит
    },
    "event_type": {
        "silent": "коворкинг",
        "project": "обсуждение проекта",
        "speaker": "спикер"
    },
    "adm_event_type": {
        "closed": "лаба закрыта", # не важно, потому что она нужна человеку, который расписывает стены, или потому что в вс в вузе выходной
        "adm_speaker": "спикер",
        "lessons": "пары"  # пары, созданные не по расписанию универа всё равно удаляться, давайте не дурить и не делать пары руками
    },

}

# session_info["interaction_type"], requested_field or action type
NEXT_STEP = [
    [["get_schedule", "interaction_type"], ["GET", "date"]],
    [["get_schedule", "date"], ["SEND_SCHEDULE"]],
    [["get_schedule", "SEND_SCHEDULE"], ["GET", "interaction_type"]],

    [["add_presence", "interaction_type"], ["GET", "event_type"]],
    [["add_presence", "event_type"], ["GET", "date"]],
    [["add_presence", "date"], ["POSSIBLE_TIME"]],
    [["add_presence", "POSSIBLE_TIME"], ["GET", "time"]], #todo: cycle to another date
    [["add_presence", "time"], ["CHECK"]],
    [["add_presence", "CHECK"], ["EVENT"]],
]

REQUIRED_FIELDS = ["date", "event_type", "time"]

MESSAGE_TEXT = {
    "date": "Пожалуйста, введите интересующую вас дату в формате 2022-07-16",
    "interaction_type": "Хотите посмотреть расписание на другую дату или создать событие?",
    "event_type": "Выберете тип события",
    "time": "Выберете желаемое время начала" , # todo: перепелить на удобные кнопки
    "check": "Верна ли эта информация: ",
    "cancel": "Данное событие не состоится, пожалуйста, используете внезапно образовавшееся время с пользой."
}

TIME_BEGINNERS = [
    "8:30",
    "10:10",
    "11:50",
    "14:00",
    "15:40",
    "17:20",
    "18:55",
    "20:30"
]

EVENT_TYPES_PRIORITY = {
    "closed": 4,
    "lesson": 3,
    "adm_speaker": 2,
    "speaker": 1,
    "project": 1,
    "silent": 1,

}