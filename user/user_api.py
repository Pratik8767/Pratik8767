from fastapi import APIRouter
from sqlalchemy import text

from user.user_model import UserModel
from user.user_services import UserServices


class UserApi():
    router=APIRouter()

    @router.get("/get_users")
    def get_user():
       return UserServices.get_users()
    
    @router.post("/create_user")
    def create_user(user:UserModel):
       return UserServices.create_user(user) 

    @router.put("/update_user") 
    def update_user(user:UserModel)  :
       return UserServices.update_user(user)     

              
    @router.delete("/delete_user/{id}")
    def delete_user(id:str):
       return UserServices.delete_user(id)   

    

