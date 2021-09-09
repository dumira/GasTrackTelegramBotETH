from apscheduler.schedulers.blocking import BlockingScheduler as scheduler
import requests
import json
import datetime

def myfn():
    # api-endpoint
    URL = "https://api.etherscan.io/api"

    # api key
    apikey = "APIKEY"

    # defining a params dict for the parameters to be sent to the API
    PARAMS_ONE = {'module': 'gastracker', 'action': 'gasoracle', 'apikey': apikey}
    PARAMS_TWO = {'module': 'stats', 'action': 'ethprice', 'apikey': apikey}

    # sending get request and saving the response as response object
    gas_price = requests.get(url=URL, params=PARAMS_ONE)
    eth_price = requests.get(url=URL, params=PARAMS_TWO)

    # extracting data in json format
    gas_data = gas_price.json()
    eth_price_data = eth_price.json()

    current_time = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M %Z")
    gas_data['result']['timestamp'] = current_time
    gas_data['result']['ethbtc'] = eth_price_data['result']['ethbtc']
    gas_data['result']['ethusd'] = eth_price_data['result']['ethusd']

    print(gas_data['result'])
    print(current_time)

    with open('JSON/data.json', 'w') as f:
        json.dump(gas_data['result'], f)

# Execute your code before starting the scheduler
print('Starting scheduler, ctrl-c to exit!')

sch = scheduler()
sch.add_job(myfn, 'interval', seconds=10)
sch.start()