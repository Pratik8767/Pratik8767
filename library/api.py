

from fastapi import APIRouter
from sqlalchemy import text

from library.model import LibraryModel
from library.services import LibraryServices
from utils.db_session import execute_custom_delete_update_query,engine


class LibraryAPI:
    router=APIRouter()
    
    @router.post('/add_library')
    def create_library(library:LibraryModel):
        return LibraryServices.create_library(library)
        
    @router.get('/get_library')
    def get_library():
        return LibraryServices.get_library()
            
    @router.delete("/delete_library/{id}")
    def delete_libray(id:str):
        return LibraryServices.delete_libray(id)
            
    @router.put("/update_library")
    def update_library(library:LibraryModel):
        return LibraryServices.update_library(library)