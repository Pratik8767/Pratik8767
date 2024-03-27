from datetime import datetime,date
from typing import Optional
from pydantic import BaseModel

class EventModel(BaseModel):
    event_id:str
    tittle:str
    description:str
    event_date: Optional[date]=date.today()
    venue:str
    organized_by:str
    event_type:str
    meeting_link:str