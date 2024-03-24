from sqlalchemy import text
from fastapi import APIRouter, FastAPI
from multipart import QuerystringParser
from user.model import UserModel
from utils.db_section import execute_custom_delete_update_query, engine

class UserAPI:
    router = APIRouter()
    @router.post("/create_user")
    def createUser(user:UserModel):
        try :
            query = f"select user_id from dev.tbl_d_user where user_id = '{user.user_id}'"
            with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    if len(rows) == 0  :
                        query = f'''insert into dev.tbl_d_user(user_id,first_name,last_name,   mobile_number,email_id,branch_id,address,password,type) values('{user.user_id}','{user.first_name}','{user.last_name}','{user.mobile_number}','{user.email_id}','{user.branch_id}','{user.address}','{user.password}','{user.type}')'''
                        execute_custom_delete_update_query(query)
                    else:
                        return "userID Already Created!!"
        except Exception as e:
             print(e)

    @router.get("/read_users")
    def readuser():
        try :
            query = "select user_id,first_name,last_name from dev.tbl_d_user"
            # coloum = ['user_id','first_name','last_name']
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                data = []
                for row in rows:
                    data.append({'user_id':row[0],'first_name':row[1],'last_name':row[2]})
                return data
        except Exception as e:
             print(e)
        
    @router.delete('/delete_user/{id}')
    def deleteuser(id:str):
        try:
            query = f"select user_id from dev.tbl_d_user where user_id = '{id}'"
            with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    if len(rows) != 0   :
                        query = f"delete from dev.tbl_d_user where user_id = '{id}'"
                        execute_custom_delete_update_query(query)
                        return "deleted"
                    else:
                        return "Already deleted!!"
        except Exception as e:
            print(e)

# delete from dev.tbl_d_user where user_id = '{id}'