from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()


@app.get("/")
async def read_main():
    return {"msg": "Hello World"}



handler = Mangum(app)
