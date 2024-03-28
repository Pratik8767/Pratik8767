from sqlalchemy import text
from fastapi import APIRouter, FastAPI
from user.user_model import UserModel
from user.user_services import UserServices

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
