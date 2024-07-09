# flask-backend/app/pyspark_analysis.py

import os
from pyspark.sql import SparkSession
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set SPARK_LOCAL_IP to avoid loopback address warning
os.environ["SPARK_LOCAL_IP"] = "192.168.1.102"  # Replace with your actual IP address

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

spark = SparkSession.builder \
    .appName("DamDataAnalysis") \
    .config("spark.jars.packages", "mysql:mysql-connector-java:8.0.26") \
    .config("spark.executor.extraJavaOptions", "--illegal-access=warn") \
    .config("spark.driver.extraJavaOptions", "--illegal-access=warn") \
    .getOrCreate()

try:
    print("Attempting to read data from dam_resources table...")
    df = spark.read.jdbc(url=jdbc_url, table="dam_resources", properties=connection_properties)
    df.show()
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    print("Stopping SparkSession...")
    spark.stop()
    print("SparkSession stopped.")
