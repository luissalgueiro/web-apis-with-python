from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def index():
    response = {"Hello":"FastAPI"}
    return response