from fastapi import FastAPI
from fastapi import FastAPI

from user.user_api import UserApi

app=FastAPI()

app.include_router(UserApi.router)
