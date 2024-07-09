# database-prep/database-seeding/insert_latest_data.py

import json
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

with open('./latest_dam_data.json') as f:
    data = json.load(f)

# Database connection
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

try:
    with connection.cursor() as cursor:
        for dam_info in data:
            for dam_name, dam_data in dam_info.items():
                for dam in dam_data['dams']:
                    dam_id = dam['dam_id']
                    dam_name = dam['dam_name']
                    latest_resource = dam['resources'][0]

                    date = latest_resource['date']
                    storage_volume = latest_resource['storage_volume']
                    percentage_full = latest_resource['percentage_full']
                    storage_inflow = latest_resource['storage_inflow']
                    storage_release = latest_resource['storage_release']

                    sql_latest_data = """
                    INSERT INTO latest_data (dam_id, dam_name, date, storage_volume, percentage_full, storage_inflow, storage_release)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE dam_name=VALUES(dam_name), date=VALUES(date), storage_volume=VALUES(storage_volume),
                    percentage_full=VALUES(percentage_full), storage_inflow=VALUES(storage_inflow), storage_release=VALUES(storage_release)
                    """
                    cursor.execute(sql_latest_data, (dam_id, dam_name, date, storage_volume, percentage_full, storage_inflow, storage_release))

    connection.commit()
finally:
    connection.close()
