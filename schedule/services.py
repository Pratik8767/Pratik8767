from sqlalchemy import text
from schedule.model import Schedulemodel
from utils.db_session import execute_custom_query,engine,execute_custom_delete_update_query

class Schedule_services:
     
    def read_data():
        try:
            query=f"select schedule_id,schedule_type,day,subject,faculty_id,branch_id,student_year,create_date,update_date from dev.tbl_f_schedule"
            execute_custom_query(query)
 
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
            
                dict1=[]
                for row in rows:
                    dict1.append({"schedule_id":row[0],"schedule_type":row[1],"day":row[2],"subject":row[3],"faculty_id":row[4],"branch_id":row[5],"student_year":row[6],"create_date":row[7],"update_date":[8]})
                return dict1
        except Exception as e:
            print(e)    
    
    def create_data(data:Schedulemodel):
        try:
            query=f"select schedule_id from dev.tbl_f_schedule where schedule_id='{data.schedule_id}'"    
            execute_custom_query(query)

            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
            
                if len(rows)==0:
                    querys=f"insert into dev.tbl_f_schedule(schedule_id,schedule_type,day,subject,faculty_id,branch_id,student_year,create_date,update_date)values('{data.schedule_id}','{data.schedule_type}','{data.day}','{data.subject}','{data.faculty_id}','{data.branch_id}','{data.student_year}','{data.create_date}','{data.update_date}')"
                    execute_custom_delete_update_query(querys)
                    return "Created successfully...!"
                else:
                    return "already exist....!"
        except Exception as e:
            print(e)    
            
    def update_data(data:Schedulemodel):
        try:
            quary=f"select schedule_id from dev.tbl_f_schedule where schedule_id='{data.schedule_id}'"
            execute_custom_query(quary)

            with engine.connect() as connection:
                result = connection.execute(text(quary))
                rows = result.fetchall()
            
                if len(rows)!=0:
                    quary=f'''update dev.tbl_f_schedule set
                    schedule_type='{data.schedule_type}',day='{data.day}',subject='{data.subject}',faculty_id='{data.faculty_id}',branch_id='{data.branch_id}',student_year='{data.student_year}',create_date='{data.create_date}',update_date='{data.update_date}' where schedule_id='{data.schedule_id}' '''
                    execute_custom_delete_update_query(quary)
                    return "updated successfully..!"
                else:
                    return "schedule_id not exist...!"        
        except Exception as e:
            print(e)    

    def delete_data(data:Schedulemodel):
        try:
            quary=f"select schedule_id from dev.tbl_f_schedule where schedule_id='{data.schedule_id}'"
            execute_custom_query(quary)

            with engine.connect() as connection:
                result = connection.execute(text(quary))
                rows = result.fetchall()
            
                if len(rows)!=0:
                    quary=f"delete from dev.tbl_f_schedule where schedule_id='{data.schedule_id}'"
                    execute_custom_delete_update_query(quary)
                    return "deleted successfully....!"
                else:
                    return "Schedule_id not Exist....!"
        except Exception as e:
            print(e)    