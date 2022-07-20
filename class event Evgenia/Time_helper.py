import datetime



def parse_human_readable_datetime(data):
    assert type(data) == str, "Type is not a string"
    assert len(data) in (10, 20), "Date format should be <dd.mm.yyyy> or <dd.mm.yyyy, hh:mm:ss>"
    if len(data) == 10:
        return datetime.datetime.strptime(data, "%d.%m.%Y")
    if len(data) == 20:
        return datetime.datetime.strptime(data, "%d.%m.%Y, %H:%M:%S")


data_string = parse_human_readable_datetime("your_data")
print(data_string)