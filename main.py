from fastapi import FastAPI, BackgroundTasks, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from extract import *
from datetime import datetime
from fastapi_utils.tasks import repeat_every
import os

# SECRET = os.getenv("SECRET")


app = FastAPI()


class Msg(BaseModel):
    msg: str
    secret: str


@app.get("/")
async def root():
    driver = await  createDriver()
    driver.get("https://ma.indeed.com/jobs?q=stage+web&fromage=1")
    print(driver.page_source)
    return driver.page_source


@app.get("/homepage")
async def demo_get():
    driver =await  createDriver()
    homepage = await get_page_source(driver)
    driver.close()
    return homepage


i=1
@app.on_event("startup")
@repeat_every(seconds=5)  # 1 hour
async def do_something():
    global i
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    driver =await createDriver()
    print(f"faho N = {i} >>>>>>>>>>>>>>>>>>> : {current_time}")
    i+=1