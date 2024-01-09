import os
from fastapi import FastAPI

app = FastAPI()
hostname = os.environ.get("HOSTNAME", "unknown")


@app.get("/")
def read_root():
    return {"Hello": "World", "hostname": hostname}
