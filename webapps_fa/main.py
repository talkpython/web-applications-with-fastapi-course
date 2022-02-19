from pathlib import Path

import fastapi
import uvicorn

import fastapi_chameleon
from fastapi_chameleon import template

app = fastapi.FastAPI()

dev_mode = True

BASE_DIR = Path(__file__).resolve().parent
template_folder = str(BASE_DIR / 'templates')
fastapi_chameleon.global_init(template_folder, auto_reload=dev_mode)


@app.get('/')
@template(template_file='index.html')
def index(user: str = 'unknown'):
    return {
        'user_name': user,
    }


if __name__ == '__main__':
    uvicorn.run(app)
