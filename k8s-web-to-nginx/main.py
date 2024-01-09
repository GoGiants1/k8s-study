import os
from fastapi import FastAPI
import httpx

app = FastAPI()
hostname = os.environ.get("HOSTNAME", "unknown")


@app.get("/")
def read_root():
    return {"hostname": hostname, "version": "v2.0.0"}


@app.get("/nginx")
async def nginx():
    url = "http://nginx"
    async with httpx.AsyncClient() as client:
        r = await client.get(url)
        return r.text
