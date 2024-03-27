from sqlalchemy import  text
from branch.model import BranchModel
from utils.db_session import execute_custom_delete_update_query,engine


class BranchServices:
 def create_branch(branch:BranchModel):
        try :
            query = f"select branch_id from dev.tbl_d_branch where branch_id = '{branch.branch_id}'"
            with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    if len(rows) == 0  :
                        query = f'''insert into dev.tbl_d_branch(branch_id,branch_name,branch_hod, 
                        create_date,update_date) 
                        values('{branch.branch_id}','{branch.branch_name}','{branch.branch_hod}','{branch.create_date}','{branch.update_date}') '''
                        execute_custom_delete_update_query(query)
                        return "Branch Created sucessfully" 
                    else:
                        return "BranchID Already Created!!"
        except Exception as e:
             print(e)
             
 def read_branch():
        try :
            query = "select branch_id,branch_name,branch_hod,create_date,update_date from dev.tbl_d_branch;"
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                data = []
                for row in rows:
                    data.append({'branch_id':row[0],'branch_name':row[1],'branch_hod':row[2]})
                return data
        except Exception as e:
             print(e)
        
 def Delete_Branch(id:str):
        try:
            query = f"select branch_id from dev.tbl_d_branch where branch_id = '{id}'"
            with engine.connect() as connection:
                    result = connection.execute(text(query))
                    rows = result.fetchall()
                    if len(rows) != 0:
                        query = f"delete from dev.tbl_d_branch where branch_id = '{id}'"
                        execute_custom_delete_update_query(query)
                        return "deleted"
                    else:
                        return "Already deleted!!"
        except Exception as e:
            print(e)
            
 def Update_Branch(branch:BranchModel):
    try:
        query=f''' select branch_id from dev.tbl_d_branch where branch_id='{branch.branch_id}';'''
        with engine.connect() as connection:
            result = connection.execute(text(query))
            rows = result.fetchall()
            if len(rows)!=0:
                    query=f'''update dev.tbl_d_branch 
                    set branch_name='{branch.branch_name}',branch_hod='{branch.branch_hod}'
                    where branch_id='{branch.branch_id}';'''
                    execute_custom_delete_update_query(query)
                    return "update query"
            else:
                    BranchServices.createBranch()
                    return "Branch Created"
    except Exception as e:
            print(e)
