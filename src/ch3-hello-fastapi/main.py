import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get("/")
def index():
    return "Hello world"


if __name__ == '__main__':
    uvicorn.run(app)

