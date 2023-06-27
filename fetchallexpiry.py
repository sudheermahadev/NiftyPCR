
import json
import requests
import pandas as pd

url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
headers = {"Accept-Encoding":"gzip, deflate, br",
           "Accept-Language":"en-US,en;q=0.5",
           "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
}

session = requests.Session()
data = session.get(url, headers= headers).json()["records"]["data"]
print(data)

