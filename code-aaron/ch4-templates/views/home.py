import fastapi
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = fastapi.APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
def index(request: Request, user: str = "guest"):
    return templates.TemplateResponse(
        "home/index.html",
        {
            "request": request,
            "user_name": user,
            "package_count": 274_000,
            "release_count": 2_234_847,
            "user_count": 73_874,
            "packages": [
                {"id": "fastapi", "summary": "A great web framework"},
                {"id": "uvicorn", "summary": "Your favourite ASGI server"},
                {"id": "httpx", "summary": "Requests fro an async world"},
            ],
        },
    )


@router.get("/about")
def about(request: Request, user: str = "guest"):
    return templates.TemplateResponse(
        "home/about.html", {"request": request, "user_name": user}
    )
