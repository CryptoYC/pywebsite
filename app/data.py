import requests
import json

def chaininfo():
    url = "https://api.chain.info/v2/entity/list"
    res = requests.get(url)
    js = res.json
    if js["code"]=="200":
        if not js['success']:
            return '404'   
        else:
            return js
    else:
        return 'error'
    



def troytrade():
    URL = "https://rdtradeapi.jar.today/t/public/data/blockchainchart/activeaddresses"
    r=requests.post(url=URL)
    data=r.json()
    if data["code"]=="200":
        return data   
    else:
        return 'error'

