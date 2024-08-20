from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

def get_engine():
    dialect = config('PGDIALECT')
    user = config('PGUSER')
    passwd = config('PGPASSWD')
    host = config('PGHOST')
    port = config('PGPORT')
    db = config('PGDB')

    DATABASE_URL = f"{dialect}://{user}:{passwd}@{host}:{port}/{db}"
    # Test the connection
    try:
        engine = create_engine(DATABASE_URL)
        print(f'Successfully connected to the database {db}!')
        return engine
    except SQLAlchemyError as e:
        print(f"Failed to connect to the database: {e}")
    

    
    
    
