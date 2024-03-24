from datetime import date
from pydantic import BaseModel


class UserModel(BaseModel):
    user_id : str
    first_name : str
    last_name : str
    mobile_number : str
    email_id : str
    branch_id : str
    city : str
    state : str
    zip_code : int
    address : str
    password : str
    type : str
    create_date : date 
    update_date : date