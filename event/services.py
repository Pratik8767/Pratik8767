from sqlalchemy import text
from event.model import EventModel
from utils.db_session import execute_custom_delete_update_query,engine


class EventServices:
    def get_event():
            query=f'''select event_id,tittle,description,event_date,venue,organized_by,event_type,meeting_link from dev.tbl_d_event'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                data=[]
                for row in rows:
                        data.append({'tittle':row[0],'description':row[1],'event_date':row[2],'venue':row[3],'organized_by':row[4],'event_type':row[5],'meeting_link':row[6]})
                return data
            
    def create_event(event:EventModel):
            query=f'''select event_id from dev.tbl_d_event where event_id='{event.event_id}' '''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows)==0:
                        query=f''' insert into dev.tbl_d_event(event_id,tittle,description,event_date,venue,organized_by,event_type,meeting_link) values('{event.event_id}','{event.tittle}','{event.description}','{event.event_date}','{event.venue}','{event.organized_by}','{event.event_type}','{event.meeting_link}') ;'''
                        execute_custom_delete_update_query(query)
                        return "event is create"
                else:
                        return"All ready Created"
    def delete_event(id:str):
            query=f'''select event_id from dev.tbl_d_event where event_id='{id}' '''        
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                if len(rows)!=0:
                        query=f'''delete from dev.tbl_d_event where event_id='{id}';'''
                        execute_custom_delete_update_query(query)
                        return "deleted"
                else:
                        return "not exist"
                    
    def Update_event(event:EventModel):
            query=f''' select event_id from dev.tbl_d_event where event_id='{event.event_id}' '''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                if len(rows) != 0:
                        query = f'''update dev.tbl_d_event set tittle='{event.tittle}',description='{event.description}',venue='{event.venue}',organized_by='{event.organized_by}',event_type='{event.event_type}',meeting_link='{event.meeting_link}'  where event_id='{event.event_id}'; '''
                        execute_custom_delete_update_query(query)
                        return "Update"
                else: 
                      EventServices.create_event()
                      return "event created"
        
                            