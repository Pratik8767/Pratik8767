from fastapi import FastAPI
from result.api import ResultAPI
from schedule.api import Schedule_Api
from attendence.api import Attendance
from user.user_api import UserApi
from event.event_api import EventAPI
from library.api import LibraryAPI
from branch.api import BranchAPI



app=FastAPI()

app.include_router(UserApi.router)
app.include_router(Attendance.router)
app.include_router(Schedule_Api.Router)
app.include_router(EventAPI.router)
app.include_router(LibraryAPI.router)
app.include_router(BranchAPI.router)
app.include_router(ResultAPI.router)






