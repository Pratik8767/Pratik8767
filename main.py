from fastapi import FastAPI
from fastapi import FastAPI
from schedule.api import Schedule_Api

from user.user_api import UserApi

app=FastAPI()

app.include_router(UserApi.router)



app.include_router(Schedule_Api.Router)
