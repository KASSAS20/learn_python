import pytz

class User:
    def __init__(self, name, time_zone) -> None:
        if time_zone not in pytz.all_timezones:
            time_zone = 'America/New_York'
        print(time_zone)
        self.name = name 
        self.time_zone = time_zone


class Event:
    def __init__(self, time, date, time_zone, list_users) -> None:
        self.time = time
        self.dste = date
        self.time_zone = time_zone
        self.list_user = list_users



