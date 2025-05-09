from pyspark.sql import SparkSession
from hdfs import InsecureClient
from pyspark.sql.functions import *
from pyspark.sql.types import *
import re

# Khởi tạo SparkSession
spark = SparkSession.builder \
    .appName("Finala") \
    .config("spark.sql.warehouse.dir", "/user/hive/warehouse") \
    .config("spark.sql.catalogImplementation", "hive") \
    .enableHiveSupport() \
    .getOrCreate()

sc = spark.sparkContext

# Kết nối HDFS
client = InsecureClient('http://localhost:9870', user='hadoopthanhluu')
hdfs_path = '/home/log/data/nasa/july/'
file_list = client.list(hdfs_path)

# Hàm parse log
def parse_log(log):
    log_pattern = r'(\S+) - - \[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}) ([+-]\d{4})\] "(\S+) (\S+) (\S+)" (\d{3}) (\d+)'
    match = re.match(log_pattern, log)
    if match:
        return match.groups()
    else:
        return ("", "", "", "", "", "", "", "")

# Xử lý từng file
for file in file_list:
    print(f"Đang xử lý file: {file}")
    rdd = sc.textFile(f'hdfs://localhost:9000{hdfs_path}{file}')
    logs_df = rdd.map(lambda x: parse_log(x)).toDF([
        "host", "timestamp", "tz", "method", "resource", "protocol", "responsecode", "bytes"
    ])

    # Lọc dữ liệu không hợp lệ
    logs_df = logs_df.filter(
        (col("host") != "") &
        (col("timestamp") != "") &
        (col("tz") != "") &
        (col("method") != "") &
        (col("resource") != "") &
        (col("protocol") != "") &
        (col("responsecode") != "") &
        (col("bytes") != "")
    )

    # Chuyển đổi và thêm các cột thời gian
    logs_df = logs_df.withColumn("timestamp", to_timestamp(col("timestamp"), "dd/MMM/yyyy:HH:mm:ss")) \
        .withColumn("ts_year", year("timestamp").cast(IntegerType())) \
        .withColumn("ts_month", month("timestamp").cast(IntegerType())) \
        .withColumn("ts_day", dayofmonth("timestamp").cast(IntegerType())) \
        .withColumn("ts_hour", hour("timestamp").cast(IntegerType())) \
        .withColumn("ts_minute", minute("timestamp").cast(IntegerType())) \
        .withColumn("ts_sec", second("timestamp").cast(IntegerType())) \
        .withColumn("ts_dayOfWeek", dayofweek("timestamp").cast(IntegerType())) \
        .withColumn("clientAuthId", col("host")) \
        .withColumn("userId", col("host"))

    # Ghi ra định dạng parquet
    logs_df.write.mode("append").parquet("/home/log/data/nasa_log/output/july2")
