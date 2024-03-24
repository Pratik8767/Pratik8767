from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils.config import database_url
from sqlalchemy import text
import uuid
import json


SQLALCHEMY_DATABASE_URL = database_url

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:admin@localhost:5432/nifedb"

# Create the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a SessionLocal class to handle database sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def is_valid_uuid(uuid_string):
    try:
        # Attempt to convert the string to a UUID
        uuid.UUID(uuid_string)
        return True
    except ValueError:
        return False


def execute_custom_query(query_str):
    with engine.connect() as connection:
        result = connection.execute(text(query_str))
        rows = result.fetchall()
        print(rows)
        records = [{"user_id": row[0], "first_name": row[1], "last_name": row[2]} for row in rows]
        return records


def execute_custom_delete_update_query(query_str):
    with engine.connect() as connection:
        connection.execute(text(query_str))
        connection.commit()