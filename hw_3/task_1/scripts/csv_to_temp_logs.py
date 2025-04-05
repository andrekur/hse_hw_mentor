from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType

FILE_PATH = 's3a://mentor-hw/Logs_data.csv'

spark = SparkSession.builder.appName('MyHW_3_task_1').getOrCreate()

schema = StructType([
    StructField('log_id', IntegerType(), nullable=False),
    StructField('transaction_id', IntegerType(), nullable=True),
    StructField('category', StringType(), nullable=True),
    StructField('comment', StringType(), nullable=True),
    StructField('log_timestamp', TimestampType(), nullable=True)
])

df = spark.read.schema(schema).csv(FILE_PATH, header=True)
df.write \
    .mode('overwrite') \
    .saveAsTable('temp.logs')
