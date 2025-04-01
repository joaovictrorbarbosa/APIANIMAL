from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from random import randint

app =FastAPI()

@app.get('/')
async def home():
    return {'msg': 'tudo certo'}

uvicorn.run(app, host="127.0.0.1", port = 8090)