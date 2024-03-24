from sqlalchemy import text
from fastapi import APIRouter, FastAPI
from multipart import QuerystringParser
from user.model import UserModel
from user.services import UserServices
from utils.db_section import execute_custom_delete_update_query, engine

class UserAPI:
    router = APIRouter()
    @router.post("/create_user")
    def createUser(user:UserModel):
        return UserServices.createUser(user)

    @router.get("/read_users")
    def readuser():
        return UserServices.readuser()
        
    @router.delete('/delete_user/{id}')
    def deleteuser(id:str):
        return UserServices.deleteuser(id)

    @router.put('/update_user')
    def updateUser(user:UserModel):
        return UserServices.updateUser(user)