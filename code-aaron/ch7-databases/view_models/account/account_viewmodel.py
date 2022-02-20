from view_models.shared.viewmodel import ViewModelBase
from data.user import User
from fastapi import Request


class AccountViewModel(ViewModelBase):
    def __init__(
        self,
        request: Request,
    ):
        super().__init__(request)
        self.user = User("AaronTeo", "ayhteo@gmail.com", "rhfbjhkdshias")
