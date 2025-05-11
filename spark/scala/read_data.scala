val df = spark.read.parquet("/home/log/data/nasa_log/output/july2")
df.show(10, truncate = false)
