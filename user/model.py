from datetime import datetime,date
from sqlite3 import Date
from typing import Optional
from pydantic import BaseModel

class UserModel(BaseModel):
    user_id:str
    first_name:str
    last_name:str
    mobile_number:str
    email_id:str
    branch_id :Optional[str]=None
    city :Optional[str]=None
    state :Optional[str]=None
    zip_code: Optional[int]=None
    address :Optional[str]=None
    password :Optional[str]=None
    type: str
    create_date: Optional[date]=date.today()
    update_date:Optional[date]=None