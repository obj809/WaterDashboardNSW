# flask-backend/app/db_info.py

from dotenv import load_dotenv
import os
import sqlalchemy

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

if None in (db_user, db_password, db_name, db_host, db_port):
    raise ValueError("One or more environment variables are not set")

database_url = f"mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

engine = sqlalchemy.create_engine(database_url)

def get_database_name():
    with engine.connect() as connection:
        result = connection.execute("SELECT DATABASE();")
        database_name = result.fetchone()[0]
        return database_name

if __name__ == "__main__":
    try:
        db_name = get_database_name()
        print(f"Connected to database: {db_name}")
    except Exception as e:
        print(f"Error: {e}")
