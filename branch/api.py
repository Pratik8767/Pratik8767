from fastapi import APIRouter,FastAPI
from branch.model import BranchModel
from branch.section import BranchServices
from utils.db_section import execute_custom_delete_update_query


class BranchAPI:
    router = APIRouter()
    @router.post('/createBranch')
    def create(branch:BranchModel):
        return BranchServices.createBranch(branch)