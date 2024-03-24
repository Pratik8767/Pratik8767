from fastapi import FastAPI

from schedule.api import Schedule_Api

app=FastAPI()

app.include_router(Schedule_Api.Router)