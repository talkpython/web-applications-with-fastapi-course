from typing import Optional

from data import db_session
from data.user import User


def user_count() -> int:
    session = db_session.create_session()

    try:
        return session.query(User).count()
    finally:
        session.close()


def create_account(name: str, email: str, password: str) -> User:
    session = db_session.create_session()

    try:
        user = User()
        user.email = email
        user.name = name
        # TODO: Set proper password
        user.hash_password = "TBD"

        session.add(user)
        session.commit()

        return user
    finally:
        session.close()


def login_user(email: str, password: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        user = session.query(User).filter(User.email == email).first()
        if not user:
            return user

        # TODO: Verify password
        if False:
            return None

        return user
    finally:
        session.close()


def get_user_by_id(user_id: int) -> Optional[User]:
    session = db_session.create_session()

    try:
        return session.query(User).filter(User.id == user_id).first()
    finally:
        session.close()


def get_user_by_email(email: str) -> Optional[User]:
    session = db_session.create_session()

    try:
        return session.query(User).filter(User.email == email).first()
    finally:
        session.close()
