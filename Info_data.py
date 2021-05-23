import yfinance as yf
import json
import requests
import time
import numpy as np
import pandas as pd

# 選擇股票列表
url = 'https://www.slickcharts.com/sp500'
headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

request = requests.get(url, headers = headers)

data = pd.read_html(request.text)[0]

# 欄位『Symbol』就是股票代碼
stk_list = data.Symbol
# 用 replace 將符號進行替換
stk_list = data.Symbol.apply(lambda x: x.replace('.', '-'))
stk_basic_data = yf.Ticker('AAPL').info

info_columns = list(['dividendRate', 'beta', '52WeekChange', 'shortName', 'longName', 'forwardEps', 'bookValue', 'priceToBook', 'shortRatio'])

stk_info_df = pd.DataFrame(index = stk_list.sort_values(), columns = info_columns)

failed_list = []

count = 0
for i in stk_info_df.index:
    try:
        # 打印出目前進度
        print('processing: ' + i)
        # 抓下來的資料暫存成 dictionary
        info_dict = yf.Ticker(i).info
        # 由於 yahoo finance 各檔股票所提供的欄位項目都不一致！所以這邊要針對每一檔股票分別取出欄位項目
        columns_included = list(info_dict.keys())
        # 因為在別檔公司裡有著 AAPL 裡所沒有的會計科目，因此要取兩家公司會計科目的交集
        intersect_columns = [x for x in info_columns if x in columns_included]
        # 有了該股欄位項目後，就可順利填入總表中相對應的位置
        stk_info_df.loc[i,intersect_columns] = list(pd.Series(info_dict)[intersect_columns].values)
        # 停一秒，再抓下一檔，避免對伺服器造成負擔而被鎖住
        time.sleep(1)
    except:
        failed_list.append(i)
        continue
stk_info_df.to_csv('Result.csv')

