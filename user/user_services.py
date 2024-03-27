from sqlalchemy import text
from user.user_model import UserModel
from utils.db_session import execute_custom_delete_update_query, engine

class UserServices:
    def get_users():
      try:
        query = "select user_id, first_name, last_name from dev.tbl_d_user"
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            
            records = [{"user_id": row[0], "first_name": row[1], "last_name": row[2]} for row in rows]
           
            return records
      except Exception as e:
         print(e)


    def create_user(user:UserModel):
       try:
        query = f"select user_id from dev.tbl_d_user where user_id = '{user.user_id}'"
        with engine.connect()as connection:
           result=connection.execute(text(query))
           rows=result.fetchall()
           if len(rows)==0:
              query = f'''insert into dev.tbl_d_user(user_id,first_name,last_name,   mobile_number,email_id,branch_id,address,password,type) values('{user.user_id}',
              '{user.first_name}',
              '{user.last_name}','{user.mobile_number}','{user.email_id}','{user.branch_id}','{user.address}','{user.password}','{user.type}')'''
              execute_custom_delete_update_query(query)
           else:
              return "userId already created."
       except Exception as e:
          print(e) 

    def update_user(user:UserModel):
       try:
          query=f"select user_id from dev.tbl_d_user where user_id='{user.user_id}'"
          with engine.connect() as connection:
             result=connection.execute(text(query))
             rows=result.fetchall()
             if len(rows)!=0:
                query=f'''UPDATE dev.tbl_d_user set first_name='{user.first_name}',last_name='{user.last_name}' where user_id='{user.user_id}';'''
                execute_custom_delete_update_query(query)
                return "record updated"
             else:
                 UserServices.create_user(user)
                 return "user created"        
       except Exception as e:
        print(e)
   

    def delete_user(id:str):
       try:
         query = f"select user_id from dev.tbl_d_user where user_id ='{id}'"
         with engine.connect() as connection:
            result=connection.execute(text(query))
            rows=result.fetchall()
            if len(rows)!=0:
             query = f"delete from dev.tbl_d_user where user_id ='{id}'"
             execute_custom_delete_update_query(query)
             return "deleted"
            else :
               return "Already deleted"
            
       except Exception as e:
          print(e)  