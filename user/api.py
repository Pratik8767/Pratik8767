from sqlalchemy import text
from fastapi import APIRouter
from user.model import UserModel
from user.services import UserServices
from utils.db_session import engine, execute_custom_delete_update_query, execute_custom_query
from utils.db_session import execute_custom_delete_update_query

class UserAPI:
    router=APIRouter()

    @router.post('/add_user')
    def create_user(user:UserModel):
        return UserServices.create_user(user)
        
    @router.get('/get_users')
    def get_user():
        return UserServices.get_user()
    
        
    @router.delete("/delete_user/{id}")
    def delete_user(id:str):
        return UserServices.delete_user(id)

    @router.put("/update/user")
    def update_user(user:UserModel):
        return UserServices.update_user(user)