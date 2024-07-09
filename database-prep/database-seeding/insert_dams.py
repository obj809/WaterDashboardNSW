# database-prep/database-seeding/insert_dams.py

import json
import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

with open('./list_of_dams.json') as f:
    data = json.load(f)

connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

try:
    with connection.cursor() as cursor:
        for dam in data['dams']:
            dam_id = dam['dam_id']
            dam_name = dam['dam_name']
            full_volume = dam['full_volume']
            latitude = dam['lat']
            longitude = dam['long']

            sql_dams = """
            INSERT INTO dams (dam_id, dam_name, full_volume, latitude, longitude)
            VALUES (%s, %s, %s, %s, %s)
            ON DUPLICATE KEY UPDATE dam_name=VALUES(dam_name), full_volume=VALUES(full_volume), latitude=VALUES(latitude), longitude=VALUES(longitude)
            """
            cursor.execute(sql_dams, (dam_id, dam_name, full_volume, latitude, longitude))

    connection.commit()
finally:
    connection.close()
