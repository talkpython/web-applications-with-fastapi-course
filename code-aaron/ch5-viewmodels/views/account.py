import fastapi
from fastapi import Request
from view_models.account.account_viewmodel import AccountViewModel
from view_models.account.login_viewmodel import LoginViewModel
from view_models.account.register_viewmodel import RegisterViewModel

router = fastapi.APIRouter()


@router.get("/account")
def account(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get("/account/register")
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get("/account/login")
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get("/account/logout")
def logout():
    return {}
