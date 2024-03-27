from fastapi import APIRouter, FastAPI
from sqlalchemy import text

from attendence.model import AttendanceModel
from attendence.services import AttendanceServices
from utils.db_session import execute_custom_delete_update_query, execute_custom_query,engine


class Attendance:
    router = APIRouter()
    @router.post('/create_user')
    def createUser(user:AttendanceModel):
        return AttendanceServices.createUser(user)
    
    @router.get('/read_user')
    def readUser():
        return AttendanceServices.readUser()

    @router.delete('/delete_user')
    def deleteUser(user:AttendanceModel):
        return AttendanceServices.deleteUser(user)

    @router.put('/update_user')
    def update_user(user:AttendanceModel):
        return AttendanceServices.update_user(user)