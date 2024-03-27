
from datetime import date
from typing import Optional
from pydantic import BaseModel


class LibraryModel(BaseModel):
    library_id:str
    book_tittle:str
    book_author:str
    book_edition:str
    book_type_id:str
    shell:Optional[str]=None
    section:Optional[str]=None
    create_date:Optional[date]=date.today()
    update_date:Optional[date]=None
    