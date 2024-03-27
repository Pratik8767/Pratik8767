from sqlalchemy import text
from result.model import Resultmodel
from utils.db_session import execute_custom_delete_update_query, execute_custom_query,engine


class Result_services:
    def readUser():
        try:
            query=f'''select result_id,exam_id,user_id,total_marks,obtain_marks,create_date,update_date from dev.tbl_f_result'''
            execute_custom_query(query)
            with engine.connect() as connection:
                result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            list = []
            for row in rows:
                    list.append({'result_id':row[0],'exam_id':row[1],'user_id':row[2],'total_marks':row[3],'obtain_marks':row[4],'create_id':row[5],'update_id':row[6]})
            return list
        except Exception as e:
            print(e) 
    
    def createuser(data:Resultmodel):
        try:
            query = f'''select result_id from dev.tbl_f_result where result_id = '{data.result_id}' '''
            execute_custom_query(query)#check kar sathi

            with engine.connect() as connection:#
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows)==0:
                        query = f''' insert into dev.tbl_f_result(result_id) values('{data.result_id}') '''
                        execute_custom_delete_update_query(query)#data
                        return "Successfully Created!!"
                else:
                        return "User_id Already Exixt!!"
        except Exception as e:
                print(e)
    def updateuser(data:Resultmodel):
        try:
            query =f'''select result_id from dev.tbl_f_result where result_id='{data.result_id}' '''
            execute_custom_query(query)
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows)!=0:#0:0 true aahe he
                    query =f'''update dev.tbl_f_result set total_marks='{data.total_marks}',obtain_marks=
                    '{data.obtain_marks}' '''
                    execute_custom_delete_update_query(query)
                    return 'succesfully update!!'
                else:
                    return "user cant exist"
        except Exception as e:
             print(e)

    def deleteuser(data:Resultmodel):
        try:
            query =f'''select result_id from dev.tbl_f_result where result_id='{data.result_id}' '''
            execute_custom_query(query)
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows)!=0:#0:0 true aahe he
                    query =f'''delete from dev.tbl_f_result where result_id = '{data.result_id}' '''
                    execute_custom_delete_update_query(query)
                    return 'succesfully deleted!!'
                else:
                    return "user cant exist"
        except Exception as e:
             print(e)        