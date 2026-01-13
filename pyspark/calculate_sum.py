from pyspark.sql import SparkSession
from pyspark.sql.functions import *
from pyspark.sql.types import StructType, StructField, StringType, FloatType
import os

os.environ['PYSPARK_PYTHON'] = 'python'
os.environ['PYSPARK_DRIVER_PYTHON'] = 'python'

if 'spark' not in globals():
    spark = SparkSession.builder.master("local[1]").config("spark.ui.enabled", "false").getOrCreate()

data = [("John Doe", "john@example.com", 50000.0),
    ("Jane Smith", "jane@example.com", 60000.0),
    ("Bob Johnson", "bob@example.com", 55000.0)]

schema = StructType([
    StructField('Name', StringType(), False),
    StructField('Email', StringType(), False),
    StructField('Salary', FloatType(), False)
])

df = spark.createDataFrame(data, schema)

df1 = df.agg(sum(col('salary')))
df1.show()
spark.stop()