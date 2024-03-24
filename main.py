from fastapi import FastAPI

from event.event_api import EventAPI
from user.user_api import UserAPI

app=FastAPI()
app.include_router(UserAPI.router)
app.include_router(EventAPI.router)