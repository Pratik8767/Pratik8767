from sqlalchemy import text
from fastapi import APIRouter, FastAPI
from branch.model import BranchModel
from branch.services import BranchServices
from utils.db_session import execute_custom_delete_update_query, engine

class BranchAPI:
    router = APIRouter()
    
    @router.post("/Create_Branch")
    def createbranch(branch:BranchModel):
       return BranchServices.create_branch(branch)  
     
    @router.get("/Read_Branch")
    def readbranch():
      return BranchServices.read_branch()  
       
    @router.delete('/Delete_Branch/{id}')
    def deletebranch(id:str):
         return BranchServices.Delete_Branch(id)
            
    @router.put("/Update_Branch")
    def updatebranch(branch:BranchModel):
         return BranchServices.Update_Branch(branch)  