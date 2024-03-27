from datetime import date
from sqlalchemy import text
from fastapi import APIRouter

from event.model import EventModel
from event.services import EventServices
from utils.db_session import engine, execute_custom_delete_update_query, execute_custom_query


class EventAPI:
        router=APIRouter()
        
        @router.post('/add_event')
        def create_event(event:EventModel):
                return EventServices.create_event(event)
       
 
        @router.get('/get_event')
        def get_event():
                return EventServices.get_event()
        
            
        @router.delete("/delete_event/{id}")
        def delete_event(id:str):
                return EventServices.delete_event(id)
       
                    
             
        @router.put("/Update_event")
        def update_event(event:EventModel):
                return EventServices.Update_event(event)
