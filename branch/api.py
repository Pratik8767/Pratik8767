from fastapi import APIRouter,FastAPI
from sqlalchemy import Engine, text
from branch.model import BranchModel
from branch.services import BranchServices
from utils.db_session import execute_custom_delete_update_query, execute_custom_query,engine


class BranchAPI:
    router = APIRouter()

    @router.get("/readUser")
    def read():
        return BranchServices.read()
            
        
    @router.post("/createUser")
    def create(data:BranchModel):
        return BranchServices.createBranch(data)
        
    @router.put("/putuser")
    def update(data:BranchModel):
        return BranchServices.updateBranch(data)
            
    @router.delete("/deleteUser")        
    def delete(data:BranchModel):
        return BranchServices.deleteBranch(data)
