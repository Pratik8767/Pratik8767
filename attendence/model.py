from datetime import date
from pydantic import BaseModel


class AttendanceModel(BaseModel):
    id : str
    user_id : str
    date : date
    status : str
    faculty_id : str