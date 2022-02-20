from re import L
from fastapi import Response, Request
from typing import Optional
import hashlib
from infrastructure import num_convert

auth_cookie_name = "pypi_account"


def set_auth(response: Response, user_id: int):
    hash_val = __hash_text(str(user_id))
    val = "{}:{}".format(user_id, hash_val)
    # we don't have SSL setup in development so secure=False
    # when running in production set this to true - remember that if you do not use https then it will not exchange cookies securely.
    response.set_cookie(
        auth_cookie_name, val, secure=False, httponly=True, samesite="Lax"
    )
    pass


def __hash_text(text: str) -> str:
    text = "you_shall_not_" + text + "PASSS!!"
    return hashlib.sha512(text.encode("utf-8")).hexdigest()


def get_user_id_from_auth_cookie(request: Request) -> Optional[int]:
    if auth_cookie_name not in request.cookies:
        print("ain't no cookie here")
        return None
    val = request.cookies[auth_cookie_name]
    parts = val.split(":")
    if len(parts) != 2:
        print("not two parts")
        return None
    if parts[1] != __hash_text(parts[0]):
        print("Warning: hash mismatch, invalid cookie value")
        return None
    print("why did I manage to get here??")
    return num_convert.try_int(parts[0])


def logout(response: Response):
    response.delete_cookie(auth_cookie_name)
