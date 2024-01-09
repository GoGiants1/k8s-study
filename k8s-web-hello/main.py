import os
from fastapi import FastAPI

app = FastAPI()
hostname = os.environ.get("HOSTNAME", "unknown")


@app.get("/")
def read_root():
    return {"hostname": hostname, "version": "v2.0.0"}
