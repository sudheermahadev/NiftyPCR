import json
import requests
import pandas as pd

stocks=["ADANIENT","SBIN","UPL"]
for i in stocks:
        print(i)
        url = "https://www.nseindia.com/api/option-chain-equities?symbol="+i
        print(url)
        headers = {"Accept-Encoding":"gzip, deflate, br",
                "Accept-Language":"en-US,en;q=0.5",
                "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0"
        }


        response = requests.get(url, headers=headers).content

        data = json.loads(response.decode('utf-8'))
        data

        data.keys()
        data['filtered'].keys()
        totCE = data['filtered']['CE']['totOI']
        totPE = data['filtered']['PE']['totOI']

        pcr= totPE/totCE
        print(pcr)

        from datetime import datetime
        NOW=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(NOW)