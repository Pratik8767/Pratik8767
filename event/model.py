from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel 


class HolidayModel(BaseModel):
     holiday_id :str
     tittle :str
     description :str
     date :date
     create_date : Optional[date]=date.today() # type: ignore
     update_date : Optional[date]=None # type: ignore
     