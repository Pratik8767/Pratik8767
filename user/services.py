from sqlalchemy import text
from user.model import UserModel
from utils.db_section import execute_custom_delete_update_query, execute_custom_query,engine


class Userservices:
    def readuser():
        query = f'''select user_id,first_name,last_name,mobile_number,email_id,branch_id,city,state,zip_code,address,password,type,create_date,update_date from dev.tbl_d_user'''
        execute_custom_query(query)#it is variable jo ke db_section.py
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            list = []
            for i in rows:
                list.append({'user_id':i[0],'first_name':i[1],'last_name':i[2],'mobile_number':i[3],'email_id':i[4],'branch_id':i[5],'city':i[6],'state':i[7],'zip_code':i[8],'address':i[9],'type':i[10],'create_date':i[11],'update_date':i[12]})
            return list
        
    def createUser(kunal:UserModel):
        query = f'''select user_id from dev.tbl_d_user where user_id = '{kunal.user_id}' '''
        execute_custom_query(query)#check kar sathi

        with engine.connect() as connection:#
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)==0:#
                query = f''' insert into dev.tbl_d_user(user_id) values('{kunal.user_id}') '''
                execute_custom_delete_update_query(query)#data
                return "Successfully Created!!"
            else:
                return "User_id Already Exixt!!"
    

    def updateuser(kunal:UserModel):
        query =f'''select user_id from dev.tbl_d_user where user_id='{kunal.user_id}' '''
        execute_custom_query(query)
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)!=0:#0:0 true aahe he
                query =f'''update dev.tbl_d_user set first_name='{kunal.first_name}',last_name=
                '{kunal.last_name}' '''
                execute_custom_delete_update_query(query)
                return 'succesfully update!!'
            else:
                return "user cant exist"
    def deleteuser( kunal:UserModel):
         query =f'''select user_id from dev.tbl_d_user where user_id='{kunal.user_id}' '''
         execute_custom_query(query)
         with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)!=0:
                query=f'''delete from dev.tbl_d_user where user_id='{kunal.user_id}' '''
                execute_custom_delete_update_query(query)
                return "delete successfully"
            else:
                return "not exist"
