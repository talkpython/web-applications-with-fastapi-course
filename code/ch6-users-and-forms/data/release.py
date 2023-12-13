import datetime


class Release:
    def __init__(self, version: str, created_date: datetime.datetime):
        self.version = version
        self.created_date = created_date
