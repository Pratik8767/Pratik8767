from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel 


class BranchModel(BaseModel):
  branch_id   :str
  branch_name :str
  branch_hod  :str
  create_date :Optional[date]=date.today() 
  update_date :Optional[date]=None
  created_at : Optional[date]=date.today()
