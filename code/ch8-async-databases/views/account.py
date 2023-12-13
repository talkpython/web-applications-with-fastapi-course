import asyncio

import fastapi
from fastapi_chameleon import template
from infrastructure import cookie_auth
from services import user_service
from starlette import status
from starlette.requests import Request
from viewmodels.account.account_viewmodel import AccountViewModel
from viewmodels.account.login_viewmodel import LoginViewModel
from viewmodels.account.register_viewmodel import RegisterViewModel

router = fastapi.APIRouter()


@router.get('/account', include_in_schema=False)
@template()
async def index(request: Request):
    vm = AccountViewModel(request)
    await vm.load()
    return vm.to_dict()


@router.get('/account/register', include_in_schema=False)
@template()
def register(request: Request):
    vm = RegisterViewModel(request)
    return vm.to_dict()


@router.post('/account/register', include_in_schema=False)
@template()
async def register(request: Request):
    vm = RegisterViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    # Create the account
    account = await user_service.create_account(vm.name, vm.email, vm.password)

    # Login user
    response = fastapi.responses.RedirectResponse(url='/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(response, account.id)

    return response


# ################### LOGIN #################################


@router.get('/account/login', include_in_schema=False)
@template(template_file='account/login.pt')
def login_get(request: Request):
    vm = LoginViewModel(request)
    return vm.to_dict()


@router.post('/account/login', include_in_schema=False)
@template(template_file='account/login.pt')
async def login_post(request: Request):
    vm = LoginViewModel(request)
    await vm.load()

    if vm.error:
        return vm.to_dict()

    user = await user_service.login_user(vm.email, vm.password)
    if not user:
        await asyncio.sleep(5)
        vm.error = 'The account does not exist or the password is wrong.'
        return vm.to_dict()

    resp = fastapi.responses.RedirectResponse('/account', status_code=status.HTTP_302_FOUND)
    cookie_auth.set_auth(resp, user.id)

    return resp


@router.get('/account/logout', include_in_schema=False)
def logout():
    response = fastapi.responses.RedirectResponse(url='/', status_code=status.HTTP_302_FOUND)
    cookie_auth.logout(response)

    return response
