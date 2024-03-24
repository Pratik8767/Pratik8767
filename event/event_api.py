from anyio import Event
from sqlalchemy import text
from fastapi import APIRouter

from event.model import EventModel
from utils.db_session import engine, execute_custom_delete_update_query, execute_custom_query
from utils.db_session import execute_custom_delete_update_query


class EventAPI:
        router=APIRouter()
        @router.post('/add_event')
        def create_event(event:EventModel):
            try:
                query=f'''select event_date from dev.tbl_d_event where event_date='{event.event_date}' '''
                with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    if len(rows)==0:
                        query=f''' insert into dev.tbl_d_event(tittle,description,event_date,venue,organized_by,event_type,meeting_link) values('{event.tittle}','{event.description}','{event.event_date}','{event.venue}','{event.organized_by}','{event.event_type}','{event.meeting_link}') '''
                        execute_custom_delete_update_query(query)
                        return "event is create"
                    else:
                        return"All ready Created"
            except Exception as e:
                print(e)

        
        
        
        @router.get('/get_event')
        def get_event():
            try:
                query=f'''select tittle,description,event_date,venue,organized_by,event_type,meeting_link from dev.tbl_d_event'''
                execute_custom_query(query)
                with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    print(rows)
                    data=[]
                    for row in rows:
                        data.append({'tittle':row[0],'description':row[1],'event_date':row[2],'venue':row[3],'organized_by':row[4],'event_type':row[5],'meeting_link':row[6]})
                        return data
            except Exception as e:
                print(e)
            
        @router.delete("/delete_event/{id}")
        def delete_event(id:str):
            try:
                query=f'''select event_date from dev.tbl_d_event where event_date='{event.event_date}' '''        
                with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    print(rows)
                    if len(rows) is not 0:
                        query=f'''delete from dev.tbl_d_event where event_date='{id}';'''
                        execute_custom_delete_update_query(query)
                        return "Update"
                    else:
                        return "not exist"
            except Exception as e:
                print(e)
                    
             
        @router.put("/Update_event/{id}")
        def Update_user(event:EventModel):
            try:
                query=f''' 'select event_date from dev.tbl_d_event where event_date={event.event_date}' '''
                with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    print(rows)
                    if len(rows) != 0:
                        query = f'''update dev.tbl_d_event set tittle='{event.tittle}',description='{event.description}',venue='{event.venue}',organized_by='{event.organized_by}','{event.event_type}','{event.meeting_link} where event_date='{event.event_date}') '''
                        execute_custom_delete_update_query(query)
                        return "Update"
                    else:
                        return "query does not exist"
            except Exception as e:
                print(e)
        
        