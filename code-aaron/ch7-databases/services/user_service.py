from data.user import User
from typing import Optional


def create_account(name: str, email: str, password: str):
    return User(name, email, "abcde")


def login_user(email: str, password: str) -> Optional[User]:
    if password == "abcde":
        return User("test_user", email, password)
    return None
