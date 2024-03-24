from fastapi import FastAPI
from event.event_api import HolidayAPI
from user.user_api import UserAPI

app=FastAPI()
#app.include_router(UserAPI.router)
app.include_router(HolidayAPI.router)

