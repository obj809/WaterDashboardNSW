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

# Set SPARK_LOCAL_IP to avoid loopback address warning
os.environ["SPARK_LOCAL_IP"] = "192.168.1.102"  # Replace with your actual IP address

# Parse the SQLAlchemy database URI
db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

jdbc_url = f"jdbc:mysql://{db_host}:{db_port}/{db_name}"

# Debug prints
print("JDBC URL:", jdbc_url)
print("DB User:", db_user)
print("DB Password:", db_password)
print("DB Name:", db_name)
print("DB Host:", db_host)
print("DB Port:", db_port)

# Check if any of the environment variables are None
if None in (db_user, db_password, db_name, db_host, db_port):
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
    .config("spark.executor.extraJavaOptions", "--illegal-access=warn") \
    .config("spark.driver.extraJavaOptions", "--illegal-access=warn") \
    .getOrCreate()

try:
    # Load data from dam_resources table
    print("Attempting to read data from dam_resources table...")
    df = spark.read.jdbc(url=jdbc_url, table="dam_resources", properties=connection_properties)
    print("Data successfully loaded from dam_resources table.")

    # Filter by dam_id if provided
    if len(sys.argv) > 1:
        dam_id = sys.argv[1]
        print(f"Filtering data for dam_id: {dam_id}")
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

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Stop SparkSession
    print("Stopping SparkSession...")
    spark.stop()
    print("SparkSession stopped.")
