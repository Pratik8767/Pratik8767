from fastapi import FastAPI

from user.api import UserAPI
from library.api import LibraryAPI

app=FastAPI()
app.include_router(UserAPI.router)
app.include_router(LibraryAPI.router)
