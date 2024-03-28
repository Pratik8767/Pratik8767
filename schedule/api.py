from fastapi import APIRouter
from sqlalchemy import text
from schedule.model import  Schedulemodel
from schedule.services import Schedule_services


class Schedule_Api:
    router=APIRouter()

    @router.get("/read")
    def read():
        return Schedule_services.read_data() 
    
    @router.post("/insert")
    def create(data:Schedulemodel):
        return Schedule_services.create_data(data) 
    
    @router.put("/update")
    def update(data:Schedulemodel):
        return Schedule_services.update_data(data)
    
    @router.delete("/delete")
    def delete(data:Schedulemodel):
        return Schedule_services.delete_data(data)
        