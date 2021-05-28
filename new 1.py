import requests
import numpy as np
import pandas as pd

link = 'https://quality.data.gov.tw/dq_download_json.php?nid=11549&md5_url=bb878d47ffbe7b83bfc1b41d0b24946e'
r = requests.get(link)
data = pd.DataFrame(r.json())
list = data.證券代號
print(list)

""" 
 ###show the recent stock market
    url = 'https://www.slickcharts.com/sp500'
    headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}

    request = requests.get(url, headers = headers)

    data = pd.read_html(request.text)[0]
    
"""