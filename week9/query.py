#Example of querying volumeUSD and reserveUSD 

import requests
import json
import pandas as pd

# Using Query Language

query = """query {
        farmsAtLatestBlock: pair( id:"0x0ed7e52944161450477ee417de9cd3a859b14fd0" ) {
            id
            volumeUSD
            reserveUSD
      }
        farmsOneWeekAgo: pair(id:"0x0ed7e52944161450477ee417de9cd3a859b14fd0", 
      block: { number: 9211000 }) #block of last week
  		{
            id
            volumeUSD
            reserveUSD
      }
}
"""

url = 'https://bsc.streamingfast.io/subgraphs/name/pancakeswap/exchange-v2'

r = requests.post(url, json={'query': query})
print(r.status_code)
print(r.text)
json_data = json.loads(r.text)
df_data = json_data['farmsAtLatestBlock']['farmsOneWeekAgo']
df = pd.DataFrame(df_data)