from fastapi import APIRouter
from sqlalchemy import text
from schedule.model import BaseModel, Schedulemodel
from schedule.services import Schedule_services
from utils.db_session import execute_custom_delete_update_query, execute_custom_query,engine


class Schedule_Api:
    Router=APIRouter()

    @Router.get("/read")
    def read():
        return Schedule_services.read_data() 
    
    @Router.post("/insert")
    def create(data:Schedulemodel):
        return Schedule_services.create_data(data) 
    
    @Router.put("/update")
    def update(data:Schedulemodel):
        return Schedule_services.update_data(data)
    
    @Router.delete("/delete")
    def delete(data:Schedulemodel):
        return Schedule_services.delete_data(data)
        