from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import pandas as pd

# Thiết lập driver
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # chạy ẩn
service = Service("C:/Users/aassd/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Truy cập trang web
url = "https://batdongsan.com.vn/ban-nha-rieng-ho-chi-minh"
driver.get(url)
time.sleep(5)  # chờ trang load JS

# Tìm các tin đăng
posts = driver.find_elements(By.CSS_SELECTOR, ".js__card")

# Lưu dữ liệu vào list
data = []

for post in posts:
    try:
        title = post.find_element(By.CSS_SELECTOR, ".js__card-title").text
        price = post.find_element(By.CSS_SELECTOR, ".re__card-config-price").text
        location = post.find_element(By.CSS_SELECTOR, ".re__card-location").text
        data.append({
            "Tiêu đề": title,
            "Giá": price,
            "Địa điểm": location
        })
    except:
        continue

driver.quit()

# Ghi vào file CSV
df = pd.DataFrame(data)
df.to_csv("batdongsan_data.csv", index=False, encoding="utf-8-sig")

print("✅ Đã lưu dữ liệu vào file batdongsan_data.csv")
