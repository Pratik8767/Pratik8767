from datetime import date
from pydantic import BaseModel


class Resultmodel(BaseModel):
    result_id : str
    exam_id :  str
    user_id : str
    total_marks : int
    obtain_marks : int
    create_date : date
    update_date : date