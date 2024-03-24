from sqlalchemy import text
from fastapi import APIRouter

from user.model import UserModel
from utils.db_session import engine, execute_custom_delete_update_query
from utils.db_session import execute_custom_delete_update_query


class UserAPI:
    router=APIRouter()

    @router.post('/add_user')
    def create_user(user:UserModel):
        query = f'''insert into dev.tbl_d_user(user_id,first_name,last_name,mobile_number,email_id,branch_id,city,state,zip_code,address,password,type,create_date,update_date) values('{user.user_id}','{user.first_name}','{user.last_name}','{user.mobile_number}','{user.email_id}','{user.branch_id}','{user.city}','{user.state}',{user.zip_code},'{user.address}','{user.password}','{user.type}','{user.create_date}','{user.update_date}');'''
        execute_custom_delete_update_query(query)
        
    @router.get('/get_users')
    def get_user():
        query=f'''select user_id,first_name,last_name from dev.tbl_d_user'''
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            data=[]
            for row in rows:
                data.append({'user_id':row[0],'first_name':row[1],'last_name':row[2]})
            return data
        
    @router.delete("/delete_user/{id}")
    def delete_user(id:str):
        query=f''' select user_id from dev.tbl_d_user where user_id='{id}';'''
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            if len(rows) is not 0:
                query=f'''delete from dev.tbl_d_user where user_id='{id}';'''
                execute_custom_delete_update_query(query)
                return "Update"
            else:
                return "not exist"
            



            
    # @router.put("/create_user/{id}")
    # def create_user(user:UserModel):
    #     query=f''' 'select user_id from dev.tbl_d_user where user_id={user.user_id}' '''
    #     with engine.connect() as connection:
    #             result = connection.execute(text(query))
    #             rows = result.fetchall()
    #             print(rows)
    #             if len(rows) != 0:
    #                 query = f'''update dev.tbl_d_user set  user_id=656,first_name
    #                 last_name, where User_id={user.user_id}'''
    #                 execute_custom_delete_update_query(query)
    #                 create "Update"
    #             else:
    #                 create"User_id does not exist"
            