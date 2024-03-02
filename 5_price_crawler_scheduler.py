from datetime import datetime
from datetime import timedelta
import time
import pymssql
from apscheduler.schedulers.blocking import BlockingScheduler
import requests
import json
db_settings = {
    "host": "127.0.0.1",
    "user": "",
    "password": "",
    "database": "",
    "charset": "utf8"
}

scheduler = BlockingScheduler(timezone='Asia/Taipei')

def daily_crawler():
    # TODO : 練習3
    url = "https://mis.twse.com.tw/stock/api/getStockInfo.jsp?ex_ch={stock_type}_{stock_code}.tw&json=1&delay=0"

# 讓Schedular在設定的時間可以正常關閉
def end_program():
    print("Program ends.")
    scheduler.shutdown(wait=False) # wait=False 表示不會等待Schedular裡面的job執行完就直接關閉


conn = pymssql.connect(**db_settings)
with conn.cursor() as cursor:
    today = datetime.today().strftime('%Y%m%d')
    command = "select * from [dbo].[calendar] where date = '" + today + "'"

    cursor.execute(command)
    result = cursor.fetchall()[0]
conn.commit()

# 確認當天不休市
if(result[1] != -1):
    # 設定每十秒執行一次 daily_crawler
    scheduler.add_job(daily_crawler, 'interval', seconds=10) # 間隔時間執行的寫法
    # 下行為可給job參數的寫法
    # scheduler.add_job(daily_crawler, 'interval', seconds=10, args=[..., ...]) 

    # 設定在一分鐘後執行 end_program
    run_time = datetime.now() + timedelta(minutes=1)
    scheduler.add_job(end_program, 'date', run_date=run_time) # 固定時間執行的寫法

    try:
        # 開始執行排程
        scheduler.start()
    except KeyboardInterrupt:
        # 如果按下 Ctrl+C 則停止排程並退出程式
        scheduler.shutdown()
        print("Program stopped by user.")
else:
    print("no work!")
