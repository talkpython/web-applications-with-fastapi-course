from starlette.requests import Request

from data.user import User
from viewmodels.shared.viewmodel import ViewModelBase


class AccountViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)
        self.user = User('Michael', 'michael@talkpython.fm', '9hsdhhsy74s')
