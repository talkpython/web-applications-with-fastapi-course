import fastapi
import uvicorn
import fastapi_chameleon
from views import home
from views import account
from views import packages

app = fastapi.FastAPI()


def configure():
    configure_templates()
    configure_routes()


def configure_templates():
    fastapi_chameleon.global_init("templates")


def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


def main():
    configure()
    uvicorn.run(app, host='localhost', port=8000)


if __name__ == '__main__':
    main()
else:
    configure()
