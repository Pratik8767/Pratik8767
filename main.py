from fastapi import FastAPI
from branch.branch_api import BranchAPI
from result.api import ResultAPI
from schedule.api import Schedule_Api
from attendence.api import Attendance
from event.event_api import EventAPI
from library.api import LibraryAPI
from user.user_api import UserAPI



app=FastAPI()
app.include_router(UserAPI.router, tags=["User"])
app.include_router(Attendance.router, tags=["Attendance"])
app.include_router(Schedule_Api.router, tags=["Schedule"])
app.include_router(EventAPI.router, tags=["Events"])
app.include_router(LibraryAPI.router, tags=["Library"])


app.include_router(BranchAPI.router, tags=["Branch"])
app.include_router(ResultAPI.router, tags=["Result"])






