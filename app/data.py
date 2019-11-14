import requests
import json

def ChainInfo():
    url = "https://api.chain.info/v2/entity/list"
    res = requests.get(url)
    js = res.json
    if not js['success']:
        return '404'
    return js



def Troytrade():
    URL = "https://rdtradeapi.jar.today/t/public/data/blockchainchart/activeaddresses"
    r=requests.post(url=URL)
    data=r.json()
    if data["code"]=="200":
        return data   
    else:
        return 'error'

