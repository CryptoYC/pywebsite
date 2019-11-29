import requests
import json


def chaininfo():
    url = "https://api.chain.info/v2/entity/list"
    res = requests.get(url)
    js = res.json()
    if res.status_code == requests.codes.ok:
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
    if res.status_code == requests.codes.ok:
        if not js['status'] == 0:
            return '404'
        else:
            return js
    else:
        return 'error'


def troytrade():
    url = "https://rdtradeapi.jar.today/t/public/data/blockchainchart/activeaddresses"
    r = requests.post(url=url)
    data = r.json()
    if data["code"] == "200":
        return data
    else:
        return 'error'
