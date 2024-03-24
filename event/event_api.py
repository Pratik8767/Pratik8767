from certifi import where
from fastapi import APIRouter
from sqlalchemy import text

from event.model import HolidayModel 
from utils.db_session import execute_custom_delete_update_query,engine


class HolidayAPI:
    router=APIRouter()

    @router.post('/add_holiday')
    def create_holiday(holiday:HolidayModel):
        query = f'''select holiday_id from dev.tbl_d_holiday where holiday_id='{holiday.holiday_id}' '''
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)==0:
                query = f'''insert into dev.tbl_d_holiday(holiday_id,tittle,description,date,create_date,update_date) values('{holiday.tittle}','{holiday.holiday_id}','{holiday.description}','{holiday.date}','{holiday.create_date}','{holiday.update_date}') '''
                execute_custom_delete_update_query(query)
                return "hoiday is created"
            else:
                return "Already Created"


    @router.get('/get_holiday')
    def get_holiday():
     query=f'''select holiday_id,tittle,description,date,create_date,update_date from dev.tbl_d_holiday'''
     with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            data=[]
            for row in rows:
                data.append({'holiday_id':row[0],'tittle':row[1],'description':row[2],'date':row[3],'create_date':row[4],'update_date':row[5]})
            return data
     
    
    @router.delete("/delete_holiday/{id}")
    def delete_holiday(id:str):
        query=f''' select holiday_id,tittle,description,date,create_date,update_date from dev.tbl_d_holiday where holiday_id='{id}' '''
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            if len(rows) is not 0:
                query=f'''delete from dev.tbl_d_holiday where holiday_id='{id}' '''
                execute_custom_delete_update_query(query)
                return "Update"
            else:
                return "not exist"
            
    
