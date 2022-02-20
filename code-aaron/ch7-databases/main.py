import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from views import account, home, packages
import data.db_session as db_session

app = fastapi.FastAPI()


def main():
    configure(dev_mode=True)
    uvicorn.run(app, host="127.0.0.1", port="8020")


def configure(dev_mode: bool):
    configure_templates()
    configure_routes()
    configure_db(dev_mode)


def configure_templates():
    app.mount("/static", StaticFiles(directory="static"), name="static")


def configure_db(dev_mode: bool):
    './db/sqlite'
    file = (Path(__file__).parent / 'db' / 'pypi.sqlite').absolute()
    db_session.global_init(file.as_posix())
    

def configure_routes():
    app.include_router(home.router)
    app.include_router(account.router)
    app.include_router(packages.router)


if __name__ == "__main__":
    main()
else:
    configure(dev_mode=False)  # this is for production, which does not use main()
