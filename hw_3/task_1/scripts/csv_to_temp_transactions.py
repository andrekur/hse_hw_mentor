from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType, DoubleType, BooleanType

FILE_PATH = 's3a://mentor-hw/Transactions_data.csv'

spark = SparkSession.builder.appName('MyHW_3_task_1').getOrCreate()

schema = StructType([
    StructField('transaction_id', IntegerType(), nullable=False),
    StructField('user_id', IntegerType(), nullable=False),
    StructField('amount', DoubleType(), nullable=False),
    StructField('currency', StringType(), nullable=False),
    StructField('transaction_date', TimestampType(), nullable=False),
    StructField('is_fraud', IntegerType(), nullable=False)
])

df = spark.read \
        .schema(schema) \
        .csv(FILE_PATH, header=True)

df = df.withColumn('is_fraud', col('is_fraud').cast(BooleanType()))

df.write \
    .mode('overwrite') \
    .saveAsTable('temp.transactions')
