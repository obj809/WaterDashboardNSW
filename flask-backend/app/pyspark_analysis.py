# flask-backend/app/pyspark_analysis.py

import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import avg
from datetime import datetime, timedelta
import json
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Parse the SQLAlchemy database URI
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = 'local_dam_data'
db_host = 'localhost'
db_port = '3306'  # Default MySQL port

jdbc_url = f"jdbc:mysql://{db_host}:{db_port}/{db_name}"

# Debug prints
print("JDBC URL:", jdbc_url)
print("DB User:", db_user)
print("DB Password:", db_password)

# Check if any of the environment variables are None
if None in (jdbc_url, db_user, db_password):
    raise ValueError("One or more environment variables are not set")

connection_properties = {
    "user": db_user,
    "password": db_password,
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("DamDataAnalysis") \
    .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.26") \
    .getOrCreate()

# Load data from dam_resources table
df = spark.read.jdbc(url=jdbc_url, table="dam_resources", properties=connection_properties)

# Filter by dam_id if provided
if len(sys.argv) > 1:
    dam_id = sys.argv[1]
    df = df.filter(df.dam_id == dam_id)

# Clean and process data (if necessary)
df = df.filter(df.percentage_full.isNotNull())

# Calculate average percentage_full for different periods
current_date = datetime.now()

# Last 12 months
date_12_months_ago = current_date - timedelta(days=365)
avg_12_months = df.filter(df.date >= date_12_months_ago).groupBy().agg(avg("percentage_full").alias("avg_percentage_full_12_months")).collect()[0]["avg_percentage_full_12_months"]

# Last 5 years
date_5_years_ago = current_date - timedelta(days=5*365)
avg_5_years = df.filter(df.date >= date_5_years_ago).groupBy().agg(avg("percentage_full").alias("avg_percentage_full_5_years")).collect()[0]["avg_percentage_full_5_years"]

# Last 20 years
date_20_years_ago = current_date - timedelta(days=20*365)
avg_20_years = df.filter(df.date >= date_20_years_ago).groupBy().agg(avg("percentage_full").alias("avg_percentage_full_20_years")).collect()[0]["avg_percentage_full_20_years"]

# Convert Decimal to float
averages = {
    "avg_percentage_full_12_months": float(avg_12_months),
    "avg_percentage_full_5_years": float(avg_5_years),
    "avg_percentage_full_20_years": float(avg_20_years)
}

# Output the averages as a JSON string
print(json.dumps(averages))

# Stop SparkSession
spark.stop()
