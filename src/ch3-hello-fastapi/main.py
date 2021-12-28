import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return "Hello world"


uvicorn.run(app)
