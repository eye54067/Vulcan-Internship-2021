#week5_5 Filter transaction by specifying start block and end block
        #result : transactionHash, blockNumber, topics, and data

from web3.auto.gethdev import Web3
from web3.middleware import geth_poa_middleware
import pandas as pd

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

contract_address = "0x0eD7e52944161450477ee417DE9Cd3a859b14fD0"
url = 'https://api.bscscan.com/api?module=contract&action=getabi&address=0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82&apikey=FQN6F7F2VNUZD593B1GP9AMQGR77HWC39W'

f = w3.eth.filter({'fromBlock': 8767610, 'toBlock': 8767710,'address': contract_address})
h = w3.eth.get_filter_logs(f.filter_id)
print(h)

"""df = pd.DataFrame.from_records(h, columns= ['transactionHash','blockNumber','topics','data'])
print(df)"""


#df1.to_csv(r'D:\Year3-2\Vulcan\Week5\h5.csv')"""