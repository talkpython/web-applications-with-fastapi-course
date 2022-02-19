import fastapi
import uvicorn

app = fastapi.FastAPI()


@app.get('/')
def index():
    content = """
    <h1>Hello FastApi</h1>
    """
    return fastapi.responses.HTMLResponse(content)


if __name__ == '__main__':
    uvicorn.run(app)
