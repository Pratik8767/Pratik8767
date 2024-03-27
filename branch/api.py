from fastapi import APIRouter,FastAPI
from sqlalchemy import Engine, text
from branch.model import BranchModel
from branch.services import BranchServices
from utils.db_section import execute_custom_delete_update_query, execute_custom_query,engine


class BranchAPI:
    router = APIRouter()

    @router.get("/readUser")
    def read():
        query = f''' select branch_id,branch_name,branch_hod,create_date,update_date from dev.tbl_d_branch'''
        execute_custom_query(query)
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            print(rows)
            list = []
            for row in rows:
                list.append( {'branch_id':row[0],'branch_name':row[1],'branch_hod':row[2],'create_date':[3],'update_date':row[4]})
            return list
            
        
    @router.post("/createUser")
    def create(data:BranchModel):
        query=f'''select branch_id from dev.tbl_d_branch where branch_id='{data.branch_id}' '''
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
        
    @router.put("/putuser")
    def update(data:BranchModel):
        query =f'''select branch_id from dev.tbl_d_branch where branch_id='{data.branch_id}' '''
        execute_custom_query(query)
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)!=0:#0:0 true aahe he
                query =f'''update dev.tbl_d_branch set branch_name=
                '{data.branch_name}',branch_hod='{data.branch_hod}',create_date='{data.create_date}',update_date='{data.update_date}' '''
                execute_custom_delete_update_query(query)
                return 'succesfully update!!'
            else:
                return "user cant exist"
            
    @router.deelete("/deleteUser")        
    def delete(data:BranchModel):
        query=f''' select branch_id from dev.tbl_d_branch where branch_id='{data.branch_id}'''
        execute_custom_query(query)
        with engine.connect() as connection:

            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)
