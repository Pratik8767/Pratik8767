from datetime import datetime,date
from typing import Optional
from pydantic import BaseModel


class UserModel(BaseModel):
    user_id : str
    first_name : str
    last_name : str
    mobile_number : str
    email_id : str
    branch_id : str
    city : Optional[str] = None
    state : Optional[str] = None
    zip_code : Optional[int] = None
    address : str
    password : str
    type : str
    create_date : Optional[date] = date.today()
    update_date : Optional[date] = None
