from datetime import date
import caldav
from icalendar import Calendar


class EventParameters:
    def __init__(self, summary, description, dateStart, dateEnd, timeStart, timeEnd):
        self.summary = summary
        self.description = description
        self.dateStart = dateStart
        self.dateEnd = dateEnd
        self.timeStart = timeStart
        self.timeEnd = timeEnd


def yandex_calendar_events(data_begin, data_end, url, userN, passW):
    client = caldav.DAVClient(url=url, username=userN, password=passW)
    principal = client.principal()

    calendar = principal.calendar(name="Мои события")
    results = calendar.events()
    AllEvents = []

    for eventraw in results:
        event = Calendar.from_ical(eventraw._data)
        for component in event.walk():
            if component.name == "VEVENT":
                MyNewEvent = EventParameters(summary=component.get('summary'),
                                             description=component.get('description'),
                                             dateStart=component.get('dtstart').dt.strftime('%m/%d/%Y'),
                                             dateEnd=component.get('dtend').dt.strftime('%m/%d/%Y'),
                                             timeStart=component.get('dtstart').dt.strftime('%H:%M'),
                                             timeEnd=component.get('dtend').dt.strftime('%H:%M')
                                             )
                AllEvents.append(MyNewEvent)

    for event in AllEvents:
        y_m_d = event.dateStart.split('/')
        if data_begin <= date(int(y_m_d[2]), int(y_m_d[0]), int(y_m_d[1])) <= data_end:
            print('Событие: ', event.summary)
            print('Комментарий: ', event.description)
            print('Дата начала: ', event.dateStart)
            print('Дата окончания', event.dateEnd)
            print('Время окончания', event.timeStart)
            print('Время окончания', event.timeEnd, '\n')


yandex_calendar_events(date(2020, 7, 14),
                       date(2022, 6, 30),
                       "https://caldav.yandex.ru/calendars/ew.kiseleva2014%40yandex.ru/events-18248179/",
                       "ew.kiseleva2014@yandex.ru",
                       "xuyqonjiuvucnrft")


