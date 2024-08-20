from decouple import config, UndefinedValueError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

def build_engine():
    try:
        dialect = config('PGDIALECT')
        user = config('PGUSER')
        passwd = config('PGPASSWD')
        host = config('PGHOST')
        port = config('PGPORT')
        db = config('PGDB')
    except UndefinedValueError as e:
        print(f"Missing environment variable: {e}")
        raise

    DATABASE_URL = f"{dialect}://{user}:{passwd}@{host}:{port}/{db}"

    # Test the connection
    try:
        engine = create_engine(DATABASE_URL)
        print(f'Successfully connected to the database {db}!')
        return engine
    except SQLAlchemyError as e:
        print(f"Failed to connect to the database: {e}")
    

    
    
    
