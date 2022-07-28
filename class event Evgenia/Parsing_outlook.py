from O365 import Account, MSGraphProtocol

CLIENT_ID = "CLIENT_ID"
CLIENT_SECRET = "CLIENT_SECRET"

credentials = (CLIENT_ID, CLIENT_SECRET)
protocol = MSGraphProtocol(defualt_resource='defualt_resource@outlook.com')
scopes = ['Calendars.Read.Shared']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')

schedule = account.schedule()
calendar = schedule.get_default_calendar()
events = calendar.get_events(include_recurring=False)

for event in events:
    print(event)
