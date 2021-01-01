from typing import Optional

from starlette.requests import Request

from viewmodels.shared.viewmodel import ViewModelBase


class RegisterViewModel(ViewModelBase):
    def __init__(self, request: Request):
        super().__init__(request)

        self.name: Optional[str] = None
        self.password: Optional[str] = None
        self.email: Optional[str] = None
