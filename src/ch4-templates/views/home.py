import fastapi
from fastapi_chameleon import template

router = fastapi.APIRouter()


@router.get("/")
@template(template_file="home/index.pt")
def index(user: str = "anon"):
    return {"user_name": user if user else "anon"}


@router.get("/about")
def about():
    return {}
