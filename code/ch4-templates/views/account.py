import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/account")
def index():
    return {}


@router.get("/account/register")
def register():
    return {}


@router.get("/account/login")
def login():
    return {}


@router.get("/account/logout")
def logout():
    return {}
