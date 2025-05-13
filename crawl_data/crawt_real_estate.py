from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time

# Khởi tạo ChromeOptions
options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)
# options.add_argument("--headless")  # Bỏ comment nếu muốn chạy nền

# Đường dẫn tới ChromeDriver
service = Service("C:/Users/aassd/Downloads/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=options)

# Xóa navigator.webdriver
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        })
    """
})

# Crawl nhiều trang
base_url = "https://batdongsan.com.vn/ban-nha-rieng"
num_pages = 50  # Số trang cần lấy

data = []

for page in range(1, num_pages + 1):
    if page == 1:
        url = base_url
    else:
        url = f"{base_url}/p{page}"

    print(f"📄 Đang xử lý trang: {url}")
    try:
        driver.get(url)
        time.sleep(8)  # Chờ trang load

        posts = driver.find_elements(By.CSS_SELECTOR, ".js__card")
        print("🔍 Số tin đăng:", len(posts))

        for post in posts:
            try:
                title = post.find_element(By.CSS_SELECTOR, ".re__card-title").text
                price = post.find_element(By.CSS_SELECTOR, ".re__card-config-price").text
                area = post.find_element(By.CSS_SELECTOR, ".re__card-config-area").text
                price_per_m2 = post.find_element(By.CSS_SELECTOR, ".re__card-config-price_per_m2").text
                location = post.find_element(By.CSS_SELECTOR, ".re__card-location span").text

                # Thử lấy số phòng ngủ và WC nếu có
                try:
                    bedroom = post.find_element(By.CSS_SELECTOR, ".re__card-config-bedroom").get_attribute("aria-label")
                except:
                    bedroom = ""

                try:
                    toilet = post.find_element(By.CSS_SELECTOR, ".re__card-config-toilet").get_attribute("aria-label")
                except:
                    toilet = ""

                data.append({
                    "Tiêu đề": title,
                    "Giá": price,
                    "Diện tích": area,
                    "Giá/m²": price_per_m2,
                    "Phòng ngủ": bedroom,
                    "WC": toilet,
                    "Địa điểm": location
                })

            except Exception as e:
                print("❌ Lỗi khi trích xuất bài đăng:", e)

    except Exception as e:
        print(f"⚠️ Lỗi khi tải trang: {e}")

# Lưu dữ liệu ra CSV
df = pd.DataFrame(data)
df.to_csv("batdongsan_data.csv", index=False, encoding="utf-8-sig")
print("✅ Đã lưu dữ liệu vào file: batdongsan_data.csv")

driver.quit()
