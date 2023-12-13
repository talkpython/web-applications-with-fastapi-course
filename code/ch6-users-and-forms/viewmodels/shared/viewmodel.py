from typing import Optional

from infrastructure import cookie_auth
from starlette.requests import Request


class ViewModelBase:
    def __init__(self, request: Request):
        self.request: Request = request
        self.error: Optional[str] = None
        self.user_id: Optional[int] = None

        # We'll get this once we have users from the cookies.
        self.is_logged_in = cookie_auth.get_user_id_via_auth_cookie(self.request)

    def to_dict(self) -> dict:
        return self.__dict__
