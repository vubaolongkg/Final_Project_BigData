df.coalesce(1)
  .write
  .option("header", "true")
  .csv("/home/log/data/nasa_log/output/output_csv")
