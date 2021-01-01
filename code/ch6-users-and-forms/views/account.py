import fastapi
from fastapi_chameleon import template
from starlette.requests import Request

from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

router = fastapi.APIRouter()


@router.get('/account')
@template()
def index(request: Request):
    vm = AccountViewModel(request)
    return vm.to_dict()


@router.get('/account/register')
@template()
def register(request: Request):
    print("GET REGISTER")
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/account/register')
@template()
def register(request: Request):
    print("POST REGISTER")
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.get('/account/login')
@template()
def login(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.get('/account/logout')
def logout(request: Request):
    return {}
