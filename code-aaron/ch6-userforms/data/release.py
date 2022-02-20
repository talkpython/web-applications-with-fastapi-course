import datetime


class Release:
    def __init__(self, version: str, created_date: datetime.datetime):
        self.created_date = created_date
        self.version = version
