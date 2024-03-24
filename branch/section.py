from pydantic import BaseModel
from branch.model import BranchModel
from utils.db_section import execute_custom_delete_update_query


class BranchServices(BaseModel):
    def createBranch(branch:BranchModel):
        query = f'''insert into dev.tbl_d_branch(branch_id,branch_name,branch_hod) values('{branch.branch_id}','{branch.branch_name}','{branch.branch_hod}')'''
        execute_custom_delete_update_query(query)