from pydantic import BaseModel
from datetime import date

class Schedulemodel(BaseModel):
    schedule_id:str
    schedule_type:str
    day:str
    subject:str
    faculty_id:str
    branch_id:int
    student_year:int
    create_date:date 
    update_date:date

