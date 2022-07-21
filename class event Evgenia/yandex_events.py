import caldav
from icalendar import Calendar
from datetime import datetime


class Event:
    def __init__(self, summary: str, description: str, datetimeStart: str, datetimeEnd: str):
        self.summary = summary
        self.description = description
        self.datetimeStart = datetimeStart
        self.datetimeEnd = datetimeEnd


def parse_human_readable_datetime(data):
    assert isinstance(data, str), "Type is not a string"
    if len(data) == 10:
        return datetime.strptime(data, "%d.%m.%Y")
    if len(data) == 20:
        return datetime.strptime(data, "%d.%m.%Y, %H:%M:%S")
    assert False, "Date format should be <dd.mm.yyyy> or <dd.mm.yyyy, hh:mm:ss>"


def read_events(results):
    AllEvents = []
    for eventraw in results:
        event = Calendar.from_ical(eventraw._data)
        for component in event.walk():
            if component.name == "VEVENT":
                MyNewEvent = Event(summary=component.get('summary'),
                                   description=component.get('description'),
                                   datetimeStart=component.get('dtstart').dt.strftime('%d.%m.%Y'),
                                   datetimeEnd=component.get('dtend').dt.strftime('%d.%m.%Y')
                                   )
                AllEvents.append(MyNewEvent)
    return AllEvents


def parse_yandex_calendar_events(data_begin, data_end, url, userN, passW):
    client = caldav.DAVClient(url=url, username=userN, password=passW)
    principal = client.principal()

    calendar = principal.calendar(name="Мои события")
    results = calendar.events()

    AllEvents = read_events(results)

    data_begin = parse_human_readable_datetime(data_begin)
    if data_end is None:
        data_end = datetime.today()
    else:
        data_end = parse_human_readable_datetime(data_end)

    for event in AllEvents:
        event.datetimeStart = parse_human_readable_datetime(event.datetimeStart)
        event.datetimeEnd = parse_human_readable_datetime(event.datetimeEnd)
        if data_begin <= event.datetimeStart <= data_end:
            print(f"Событие: {event.summary}")
            print(f"Комментарий: {event.description}")
            print(f"Начало: {event.datetimeStart}")
            print(f"Окончание: {event.datetimeEnd} \n")


def read_file_secret_storage(file):
    read_file = []
    with open(file, "r") as f:
        for line in f.readlines():
            read_file.append(line)
    yourUrl = read_file[0][:-1]
    username = read_file[1][:-1]
    password = read_file[2]
    return yourUrl, username, password


yourUrl, username, password = read_file_secret_storage("secret_storage")
parse_yandex_calendar_events(data_begin="01.07.2022, 10:32:00",
                             data_end=None,
                             url=yourUrl,
                             userN=username,
                             passW=password)

