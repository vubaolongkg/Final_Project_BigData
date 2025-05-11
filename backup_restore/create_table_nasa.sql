CREATE TABLE `nasa_logs_cleaned`(
  `host` string, 
  `timestamp` string, 
  `tz` string, 
  `method` string, 
  `resource` string, 
  `protocol` string, 
  `responsecode` int, 
  `bytes` int, 
  `ts_year` int, 
  `ts_month` int, 
  `ts_day` int, 
  `ts_hour` int, 
  `ts_minute` int, 
  `ts_sec` int, 
  `ts_dayofweek` string, 
  `clientauthid` string, 
  `userid` string)
ROW FORMAT SERDE 
  'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe' 
WITH SERDEPROPERTIES ( 
  'field.delim'=',', 
  'serialization.format'=',') 
STORED AS INPUTFORMAT 
  'org.apache.hadoop.mapred.TextInputFormat' 
OUTPUTFORMAT 
  'org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat'
LOCATION
  'hdfs://localhost:9000/user/hive/warehouse/nasa_logs_cleaned'
TBLPROPERTIES (
  'bucketing_version'='2', 
  'transient_lastDdlTime'='1746337503')