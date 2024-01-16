#!/usr/bin/python
# -*- codding: utf-8 -*-

import json
import aioredis
import uvicorn
from aioredis import Redis
from prometheus_fastapi_instrumentator import Instrumentator
from fastapi.responses import JSONResponse
from fastapi import FastAPI


app=FastAPI()
Instrumentator().Instrument(app).expose(app)
aioredisconn: Redis

@app.on_event('startup')
async def on_startup() -> None:
    global redisconn
    print("Connecting to redis")
    redisconn = aioredis.Redis(connection_pool=aioredis.ConnectionPool.from_url(
        "redis://:123456@127.0.0.1:6379/0", decode_responses=True, encoding="utf-8"))

@app.get('/geo_location/{phone}', tags=["geo"], response_class=JSONResponse)
async def geo_location(phone: str):
    return json.loads(await aioredisconn.get(phone))

@app.post('/geo_location/', tags=["geo"], response_class=JSONResponse)
async def geo_location_p():
    """..."""
    return "{}"

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)