# database-prep/database-seeding/insert_all_data.py

import json
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

with open('./all_dam_data.json') as f:
    data = json.load(f)

connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

try:
    with connection.cursor() as cursor:
        for dam_data in data:
            for dam_name, dam_info in dam_data.items():
                dam_id = None
                for dam in dam_info['dams']:
                    dam_id = dam['dam_id']
                    for resource in dam['resources']:
                        date = resource['date']
                        storage_volume = resource['storage_volume']
                        percentage_full = resource['percentage_full']
                        storage_inflow = resource['storage_inflow']
                        storage_release = resource['storage_release']

                        sql = """
                        INSERT INTO dam_resources (dam_id, date, storage_volume, percentage_full, storage_inflow, storage_release)
                        VALUES (%s, %s, %s, %s, %s, %s)
                        """
                        cursor.execute(sql, (dam_id, date, storage_volume, percentage_full, storage_inflow, storage_release))

    connection.commit()
finally:
    connection.close()
