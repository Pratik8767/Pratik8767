from pydantic import BaseModel
from sqlalchemy import Engine, text
from branch.model import BranchModel
from utils.db_section import execute_custom_delete_update_query, execute_custom_query


class BranchServices(BaseModel):
    def createBranch(data:BranchModel):
        query=f'''select branch_id from dev.tbl_d_branch where branch_id='{data.branch_id}''''
        execute_custom_query(query)
        with Engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)==0:
                query = f'''insert into dev.tbl_d_branch(branch_id,branch_name,branch_hod,create_date,update_date) values('{data.branch_id}','{data.branch_name}','{data.branch_hod}','{data.create_date}','{data.update_date}')'''
                execute_custom_delete_update_query(query)
                return "Successfully Created!!" 
            else:       
                return "User_id Already Exixt!!"
            