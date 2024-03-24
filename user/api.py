from fastapi import APIRouter, FastAPI
from sqlalchemy import text

from user.model import UserModel
from user.services import Userservices
from utils.db_section import execute_custom_delete_update_query, execute_custom_query,engine

class UserAPI:
    router = APIRouter()

    @router.get('/getuser')
    def readUser():
        return Userservices.readuser()
        
    @router.post('/postuser')
    def createUser(kunal:UserModel):
       return Userservices.createUser(kunal)
    
    @router.put("/putuser")
    def updateuser(kunal:UserModel):
            return Userservices.updateuser(kunal)
    
    @router.delete("/deleteuser")
    def deleteuser( kunal:UserModel):
         return Userservices.deleteuser(kunal)
         
        


        
        