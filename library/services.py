from sqlalchemy import text
from library.model import LibraryModel
from utils.db_session import execute_custom_delete_update_query,engine


class LibraryServices:
    def create_library(library:LibraryModel):
        try:
            query=f'''select library_id from dev.tbl_f_library where library_id='{library.library_id}';'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                if len(rows)==0:
                    query=f'''insert into dev.tbl_f_library(library_id,book_tittle,book_author,book_edition,book_type_id,shell,section,create_date,update_date) values('{library.library_id}','{library.book_tittle}','{library.book_author}','{library.book_edition}','{library.book_type_id}','{library.shell}','{library.section}','{library.create_date}','{library.update_date}')'''
                    execute_custom_delete_update_query(query)
                    return"user created sucessfully"
                else:
                    return"All ready Created"
        except Exception as e:
            print(e)
            
    def get_library():
        try:
            query=f'''select library_id,book_tittle,book_author,book_edition,book_type_id,shell,section,create_date,update_date from dev.tbl_f_library;'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                data=[]
                for row in rows:
                    data.append({'library_id':row[0],'book_tittle':row[1],'book_author':row[2],'book_edition':row[3],'book_type_id':row[4],'shell':row[5],'section':row[6],'create_date':row[7],'update_date':row[8]})
                return data
        except Exception as e:
            print(e)
            
    def delete_libray(id:str):
        try:
            query=f''' select library_id from dev.tbl_f_library where library_id='{id}';'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                if len(rows) != 0:
                    query=f'''delete from dev.tbl_f_library where library_id='{id}';'''
                    execute_custom_delete_update_query(query)
                    return "delete"
                else:
                    return "not exist"
        except Exception as e:
            print(e)
            
    def update_library(library:LibraryModel):
        try:
            query=f'''select library_id from dev.tbl_f_library where library_id='{library.library_id}';'''
            with engine.connect() as connection:
                result = connection.execute(text(query))
                rows = result.fetchall()
                print(rows)
                if len(rows)!=0:
                    query=f'''update dev.tbl_f_library set book_tittle='{library.book_tittle}',book_author='{library.book_author}',book_edition='{library.book_edition}',book_type_id='{library.book_type_id}',shell='{library.shell}',section='{library.section}',create_date='{library.create_date}',update_date='{library.update_date}'where library_id='{library.library_id}' '''
                    execute_custom_delete_update_query(query)
                    return "update query"
                else:
                    return LibraryServices.create_library(library)
        except Exception as e:
            print(e)