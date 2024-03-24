from fastapi import FastAPI

from user.user_api import UserAPI

app=FastAPI()
app.include_router(UserAPI.router)