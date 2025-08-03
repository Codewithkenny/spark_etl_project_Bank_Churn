from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import os 

# initialize the Spark Session
spark = SparkSession.builder \
        .appName('ExploreBankChurn') \
        .getOrCreate()

print("Spark session started.")

# Define file path
file_path = 'data/Bank_Churn.csv'
output_path = 'output/transformed_churn.csv'

#Ensure outout directory exist
os.makedirs('output', exist_ok=True)


#Extract
print("Extracting data...")
df = spark.read.csv('Bank_Churn.csv', header=True, inferSchema=True)

print("Transforming data...")
# Drop Duplicates
df = df.dropDuplicates()

# Drop rows with any nulls
df = df.na.drop()

# Rename columns to lowercase for consistency
df = df.select([col(c).alias(c.lower()) for c in df.columns])











# Show the sample data
df.show(10, truncate=False)

print("SparkSession created successfully.")

# Stop the session
spark.stop()
