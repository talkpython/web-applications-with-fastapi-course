import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles
from views import account, home, packages

app = fastapi.FastAPI()


def main():
    configure()
    uvicorn.run(app, host="127.0.0.1", port="8020")


def configure():
    configure_templates()
    configure_routes()


def configure_templates():
    app.mount("/static", StaticFiles(directory="static"), name="static")


def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == "__main__":
    main()
else:
    configure()  # this is for production, which does not use main()
