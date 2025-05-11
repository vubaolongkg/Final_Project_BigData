-- Đưa dữ liệu từ file csv trên hdfs và lưu trữ vào hive
CREATE EXTERNAL TABLE nasa_logs (
  host STRING,
  `timestamp` STRING,
  tz STRING,
  method STRING,
  resource STRING,
  protocol STRING,
  responsecode INT,
  bytes INT,
  ts_year INT,
  ts_month INT,
  ts_day INT,
  ts_hour INT,
  ts_minute INT,
  ts_sec INT,
  ts_dayOfWeek STRING,
  clientAuthId STRING,
  userId STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE
LOCATION '/home/log/data/nasa_log/output/output_csv/';
-- Top 10 khách hàng request nhiều nhất.
SELECT host, COUNT(*) AS request_count
FROM nasa_logs_cleaned
GROUP BY host
ORDER BY request_count DESC
LIMIT 10;
-- Phân phối mã phản hồi HTTP
SELECT responsecode, COUNT(*) AS response_count 
FROM nasa_logs_cleaned
GROUP BY responsecode 
ORDER BY response_count DESC;
-- Số lượng request mỗi ngày.
SELECT ts_year, ts_month, ts_day, 
COUNT(*) AS requests_per_day 
FROM nasa_logs_cleaned
GROUP BY ts_year, ts_month, ts_day 
ORDER BY ts_year, ts_month, ts_day;
-- Số lượng request của khách hàng theo thời gian.
SELECT ts_year, ts_month, ts_day, host, COUNT(*) AS request_count 
FROM nasa_logs_cleaned
GROUP BY ts_year, ts_month, ts_day, host 
ORDER BY ts_year, ts_month, ts_day, request_count DESC;
