import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from view_models.home.indexviewmodel import IndexViewModel

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request, user: str = "guest"):
    vm = IndexViewModel(request, user)
    return templates.TemplateResponse("home/index.html", vm.to_dict())


@router.get("/about")
def about(request: Request, user: str = "guest"):
    vm = IndexViewModel(request, user)
    return templates.TemplateResponse("home/about.html", vm.to_dict())
