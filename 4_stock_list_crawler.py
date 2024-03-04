import pymssql
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.microsoft import EdgeChromiumDriverManager

db_settings = {
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "database": "",
    "charset": "utf8"
}

# 儲存台灣50前10的陣列
taiwan50 = []

# 搜尋台灣50前10
def find_Taiwan50():
    # 這邊是用Edge作為範例，可以依照你使用瀏覽器的習慣做修改
    options = Options()
    options.add_argument("--headless")  # 執行時不顯示瀏覽器
    options.add_argument("--disable-notifications")  # 禁止瀏覽器的彈跳通知
    #options.add_experimental_option("detach", True) # 爬蟲完不關閉瀏覽器
    driver = webdriver.Edge()

    driver.get("https://www.cmoney.tw/etf/tw/0050")

    # TODO : 練習2

    #edge.close()

# 載入SQL (若為台灣50前10，isTaiwan50 = 1)
def find_stock(url, start, end):
    try:
        conn = pymssql.connect(**db_settings)
        # TODO : 練習2
    except Exception as e:
       print(e)

find_Taiwan50()
#print(taiwan50)
find_stock("https://isin.twse.com.tw/isin/C_public.jsp?strMode=4", "股票", "特別股")
find_stock("https://isin.twse.com.tw/isin/C_public.jsp?strMode=2", "股票", "上市認購(售)權證")