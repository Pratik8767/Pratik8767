from fastapi import FastAPI

from event.event_api import EventAPI

app=FastAPI()
app.include_router(EventAPI.router)