import caldav
import datetime
from typing import Union
from caldav import DAVClient
import json


def parse_event_data_to_json(description: str):
    info = description.split("\r\n")
    info = [[item[:item.find(":")], item[item.find(":") + 1:]] for item in info]
    answer = {field: value for field, value in zip([el[0] for el in info], [el[1] for el in info])}
    return answer



def get_events(client: DAVClient, datetime_begin: Union[str, datetime.datetime], datetime_end: Union[str, datetime.datetime]):
    if isinstance(datetime_begin, str):
        datetime_begin = datetime.datetime.strptime(datetime_begin, "%d.%m.%Y") # todo: нормальные таймхелперы
    if isinstance(datetime_end, str):
        datetime_end = datetime.datetime.strptime(datetime_end, "%d.%m.%Y")

    events = []
    my_principal = client.principal()
    calendars = my_principal.calendars()
    for calendar in calendars:
        events.extend(calendar.date_search(start=datetime_begin, end=datetime_end, expand=True))

    return events


def create_event(client: DAVClient, datetime_begin: Union[str, datetime.datetime], datetime_end: Union[str, datetime.datetime], title: str):
    if isinstance(datetime_begin, str):
        datetime_begin = datetime.datetime.strptime(datetime_begin, "%d.%m.%Y") # todo: нормальные таймхелперы
    if isinstance(datetime_end, str):
        datetime_end = datetime.datetime.strptime(datetime_end, "%d.%m.%Y")

    my_principal = client.principal()
    calendars = my_principal.calendars()
    calendar = calendars[0] #todo: pick one calendar [how?]

    new_event = calendar.save_event(
        dtstart=datetime_begin,
        dtend=datetime_end,
        summary=title,
        description="this is secret info about the further meeting"
    )



events = get_events(
    client=caldav.DAVClient(),
    datetime_begin="01.05.2022",
    timedelta="22.07.2022"
)
my_events = []
for event in events:
    my_events.append(parse_event_data_to_json(event.data))
print(1)
create_event(
    client=caldav.DAVClient(),
    datetime_begin="01.05.2022",
    datetime_end="22.07.2022",
    title="Моё новое событие"
)
