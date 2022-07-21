from __future__ import print_function

import datetime
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def GoogleCalendar():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # Проверяет существование файла с информацией об авторизованном пользователе
    # и проверяет действительность учетных данных.
    # Это верно, если учетные данные имеют токен и срок действия токена не истек.
    # Надо затестить from_authorized_user_info
    # Скорее всего необязательно считывать данные из файлика
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Файл client_secret берётся в консоле гугла в разделе Credentials
            # Создаётся локальный сервер для авторизации пользователя
            # Вся необходимая для дальней авторизации записывается в файл token.json
            flow = InstalledAppFlow.from_client_secrets_file( # todo: подтягивать данные онлайн
                '/Users/sergeymarkin/Desktop/ib_laboratory/google_calendar/client_secret_122582591655-ommn1ml19bqlepf6vec55vujutsgn4ht.apps.googleusercontent.com.json', SCOPES)
            creds = flow.run_local_server(port=0, authorization_prompt_message='Для авторизации перейдите по ссылке:\n{url}',
                                          success_message='Авторизация прошла успешно!\nМожете закрыть эту страницу.',
                                          open_browser=False)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # Создаёт ресурс для взаимодействия с API.
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        # Записываем в calendar_list названия созданных календарей и выводим данные из него
        calendar_list = {}
        for calendar_list_entry in service.calendarList().list().execute()['items']:
            calendar_list[calendar_list_entry['id']] = calendar_list_entry['summary']
        for num_calendar, num in zip(calendar_list, range(len(calendar_list))):
            print(f'{num+1}. {calendar_list[num_calendar]}')
        nums_calendar = str(input('Укажите номер календарей через пробел:\n')).split()
        for num_calendar in nums_calendar:
            events_result = service.events().list(calendarId=list(calendar_list)[int(num_calendar)-1], timeMin=now,
                                                  singleEvents=True,
                                                  orderBy='startTime').execute()
            events = events_result.get('items', [])

            if not events:
                print('Нет предстоящих мероприятий.')
                return

            # Выводим информацию о событиях
            for event in events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                if isinstance(['description'], str):
                    print(start, event['summary'], event['description'])
                else:
                    print(start, event['summary'])

    except HttpError as error:
        print('An error occurred: %s' % error)

GoogleCalendar()