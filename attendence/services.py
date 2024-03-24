from sqlalchemy import text
from attendence.model import AttendanceModel
from utils.db_section import execute_custom_delete_update_query, execute_custom_query,engine


class AttendanceServices:
    def readUser():
        try:
            query = f'''select id,user_id,date,status,faculty_id from dev.tbl_f_attendance'''
            col = ['id','user_id','date','status','faculty_id']
            execute_custom_query(query, col)
            data=[]
            dt={}
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                for row in rows:
                    for i in range(len(col)):
                        dt[col[i]]=row[i]
                    data.append(dt)
                return data
        except Exception as e:
            print(e)

    def createUser(user:AttendanceModel):
        try:
            query = f'''select id from dev.tbl_f_attendance where id = '{user.id}' '''
            col = ['id']
            execute_custom_query(query,col)
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows) == 0:
                    query = f'''insert into dev.tbl_f_attendance(id,user_id,date,status,faculty_id) values('{user.id}','{user.user_id}','{user.date}','{user.status}','{user.faculty_id}')'''
                    execute_custom_delete_update_query(query)
                    return "Successfully Created!!"
                else:
                    return "Already created!!"
        except Exception as e:
            print(e)

    def deleteUser(user:AttendanceModel):
        try:
            query = f'''select id from dev.tbl_f_attendance where id = '{user.id}' '''
            col = ['id']
            execute_custom_query(query,col)
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows) != 0:
                    query = f'''delete from dev.tbl_f_attendance where id = '{user.id}' '''
                    execute_custom_delete_update_query(query)
                    return "Successfully Deleted!!"
                else:
                    return "Not Exixt!!"
        except Exception as e:
            print(e)

    def update_user(user:AttendanceModel):
        try:
            query = f'''select id from dev.tbl_f_attendance where id = '{user.id}' '''
            col = ['id']
            execute_custom_query(query,col)
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows) != 0:
                    query = f'''update dev.tbl_f_attendance set user_id = '{user.user_id}', status = '{user.status}',faculty_id = '{user.faculty_id}' where id = '{user.id}' '''
                    execute_custom_delete_update_query(query)
                    return "Successfully Updated!!"
                else:
                    AttendanceServices.createUser(user)
                    return "Newly Created!!"
        except Exception as e:
            print(e)