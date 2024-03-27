from fastapi import APIRouter
from sqlalchemy import text
from result.model import Resultmodel
from result.services import Result_services

class ResultAPI:
    router=APIRouter()

    @router.get("/getUser")
    def read():
        return Result_services.readUser()
    

    @router.post('/postuser')
    def createuser(data:Resultmodel):
        return Result_services.createuser(data)
            
    @router.put('/putuser')
    def updateuser(data:Resultmodel):
        return Result_services.updateuser(data)
        
    @router.delete('/deleteuser')
    def updateuser(data:Resultmodel):
       return Result_services.deleteuser(data)