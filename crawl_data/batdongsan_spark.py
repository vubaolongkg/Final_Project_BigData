from pyspark.sql import SparkSession
from pyspark.sql.functions import col, regexp_replace, split
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. Tạo SparkSession
spark = SparkSession.builder.appName("XuLyNhaDat").getOrCreate()

# 2. Đọc CSV
df = spark.read.option("header", True).csv("D:/thuchanh/BigData/Final_Project_BigData/crawl_data/batdongsan_data.csv")

# 3. Làm sạch & chuẩn hóa dữ liệu
df_clean = df.select(
    # Xoá dấu " đầu/cuối
    regexp_replace(col("Tiêu đề"), r'^"|"$', '').alias("TieuDe"),

    # Giá: "5,6 tỷ" → "5.6"
    regexp_replace(col("Giá"), r' tỷ', '').alias("Gia_raw"),

    # Diện tích: "60,4 m²" → "60.4"
    regexp_replace(col("Diện tích"), r' m²', '').alias("DienTich_raw"),

    # Giá/m²: "92,72 tr/m²" → "92.72"
    regexp_replace(col("Giá/m²"), r' tr/m²', '').alias("GiaTrenM2_raw"),

    # Phòng ngủ: "4 Phòng ngủ" → 4
    regexp_replace(col("Phòng ngủ"), r' Phòng ngủ', '').cast("int").alias("PhongNgu"),

    # WC: "3 WC" → 3
    regexp_replace(col("WC"), r' WC', '').cast("int").alias("WC"),

    # Địa điểm: "Quận 9, Hồ Chí Minh" → "Quận 9", "Hồ Chí Minh"
    split(col("Địa điểm"), ",\\s*").getItem(0).alias("Quan"),
    split(col("Địa điểm"), ",\\s*").getItem(1).alias("TinhThanh")
)

# 4. Chuyển dấu "," → "." rồi ép kiểu float
df_final = df_clean.select(
    col("TieuDe"),
    regexp_replace("Gia_raw", ",", ".").cast("float").alias("Gia"),
    regexp_replace("DienTich_raw", ",", ".").cast("float").alias("DienTich"),
    regexp_replace("GiaTrenM2_raw", ",", ".").cast("float").alias("GiaTrenM2"),
    col("PhongNgu"),
    col("WC"),
    col("Quan"),
    col("TinhThanh")
)

# 5. Lưu kết quả ra file CSV
df_final.coalesce(1) \
    .write.option("header", True) \
    .mode("overwrite") \
    .csv("output_nha")

# 6. Hiển thị ra màn hình
df_final.show(truncate=False)
