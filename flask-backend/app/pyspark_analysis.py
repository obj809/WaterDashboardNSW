# flask-backend/app/pyspark_analysis.py

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv
import os

load_dotenv()


db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

jdbc_url = f"jdbc:mysql://{db_host}:{db_port}/{db_name}"


if None in (db_user, db_password, db_name, db_host, db_port):
    raise ValueError("One or more environment variables are not set")

connection_properties = {
    "user": db_user,
    "password": db_password,
    "driver": "com.mysql.cj.jdbc.Driver"
}

spark = SparkSession.builder \
    .appName("DamDataAnalysis") \
    .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.26") \
    .config("spark.executor.extraJavaOptions", "--illegal-access=warn") \
    .config("spark.driver.extraJavaOptions", "--illegal-access=warn") \
    .getOrCreate()

try:
    print("Attempting to read data from dam_resources table...")
    df = spark.read.jdbc(url=jdbc_url, table="dam_resources", properties=connection_properties)
    print("Data successfully loaded from dam_resources table.")

    if len(sys.argv) > 1:
        dam_id = sys.argv[1]
        print(f"Filtering data for dam_id: {dam_id}")
        df = df.filter(df.dam_id == dam_id)

    df = df.filter(df.percentage_full.isNotNull())

    current_date = datetime.now()

    date_12_months_ago = current_date - timedelta(days=365)
    avg_12_months = df.filter(df.date >= date_12_months_ago).groupBy().agg(avg("percentage_full").alias("avg_percentage_full_12_months")).collect()[0]["avg_percentage_full_12_months"]


    date_5_years_ago = current_date - timedelta(days=5*365)
    avg_5_years = df.filter(df.date >= date_5_years_ago).groupBy().agg(avg("percentage_full").alias("avg_percentage_full_5_years")).collect()[0]["avg_percentage_full_5_years"]

    date_20_years_ago = current_date - timedelta(days=20*365)
    avg_20_years = df.filter(df.date >= date_20_years_ago).groupBy().agg(avg("percentage_full").alias("avg_percentage_full_20_years")).collect()[0]["avg_percentage_full_20_years"]

    averages = {
        "avg_percentage_full_12_months": float(avg_12_months),
        "avg_percentage_full_5_years": float(avg_5_years),
        "avg_percentage_full_20_years": float(avg_20_years)
    }

    print(json.dumps(averages))

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    print("Stopping SparkSession...")
    spark.stop()
    print("SparkSession stopped.")
