from fastapi import FastAPI

from attendence.api import Attendance
from user.api import UserAPI

app = FastAPI()

# app.include_router(UserAPI.router)

app.include_router(Attendance.router)