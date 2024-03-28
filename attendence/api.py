from fastapi import APIRouter, FastAPI
from sqlalchemy import text

from attendence.model import AttendanceModel
from attendence.services import AttendanceServices


class Attendance:
    router = APIRouter()
    @router.post('/create_attendence')
    def createUser(user:AttendanceModel):
        return AttendanceServices.createUser(user)
    
    @router.get('/read_attendence')
    def readUser():
        return AttendanceServices.readUser()

    @router.delete('/delete_attendence')
    def deleteUser(user:AttendanceModel):
        return AttendanceServices.deleteUser(user)

    @router.put('/update_attendence')
    def update_user(user:AttendanceModel):
        return AttendanceServices.update_user(user)