from sqlalchemy import text
from fastapi import APIRouter, FastAPI
from user.model import UserModel
from user.services import UserServices
from utils.db_session import execute_custom_delete_update_query, engine

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
            
    @router.put("/update_user")
    def updateuser(user:UserModel):
         return UserServices.updateuser(user)  
