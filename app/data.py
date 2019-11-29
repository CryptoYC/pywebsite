import requests
import json
import time
from bs4 import BeautifulSoup
def chaininfo():
    url = "https://api.chain.info/v2/entity/list"
    res = requests.get(url)
    js = res.json()
    
    if res.status_code==requests.codes.ok:
        if not js['success']:
            return '404'   
        else:
            return js
    else:
        return 'error'


def sncrating():
    url = "https://sncrating.com/api/exchange/index"
    res = requests.get(url)
    js = res.json()
    if res.status_code==requests.codes.ok:
        if not js['status'] == 0  :
            return '404'
        else:
            return js
    else:
        return 'error'

    



def troytrade():
    URL = "https://rdtradeapi.jar.today/t/public/data/blockchainchart/activeaddresses"
    r=requests.post(url=URL)
    url = ""
    data=r.json()
    if data["code"]=="200":
        lenth = len(data['data']['btc'])
        price = btcPrice()
        price_len = len(price)
        b = [0]*(lenth-price_len)
        btc_price = b+ price
        data['btc_price'] = btc_price
        return json.dumps(data) 
    else:
        return 'error'

def btcPrice():
    url = "https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20091029&end="
    res =requests.get(url)
    list=[]
    soup = BeautifulSoup(res.text,'html5lib')
    for i in soup.select('tr.cmc-table-row.sc-1ebpa92-0.kQmhAn'):
        date = i.select('td')[0].get_text()
        price = i.select('td')[1].get_text()
        d = time.strptime(date,'%b %d, %Y')
        date = time.strftime("%Y-%m-%d %H:%M:%S",d)
        list.append(float(price.replace(',','')))
    return list[::-1]
