import pickle
import os
from pprint import pprint as pp
from google_auth_oauthlib.flow import Flow, InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request

CLIENT_SECRET_FILE = 'client_secret.json'
API_SERVICE_NAME = 'sheets'
API_VERSION = 'v4'

# If modifying these scopes, delete the file token.json.
SCOPE = ['https://www.googleapis.com/auth/calendar']
cred = None

from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
SERVICE_ACCOUNT_FILE = 'client_secret.json'
service = service_account.Credentials.from_service_account_file(
    r"C:\Users\Dasha\Desktop\IB_liba\infra_schedule\credentials.json")
#  credentials = service_account.Credentials.from_service_account_file(
        #  SERVICE_ACCOUNT_FILE, scopes=SCOPES)


def get_events(date_begin, date_end):
    with build('drive', 'v3') as service:
        event = service.events().get(calendarId='primary', eventId='eventId').execute()

        print(event['summary'])

get_events(None, None)