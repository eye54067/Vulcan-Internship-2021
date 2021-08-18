# Get Daily Transaction Count
import asyncio
from bscscan import BscScan
import pandas as pd

YOUR_API_KEY = "<Your API KEY>"

async def main():
    async with BscScan(YOUR_API_KEY) as client:
        query = await client.get_normal_txs_by_address(
            address="0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
            startdate="2021-06-26", enddate="2021-06-26", sort="asc")
        df = pd.DataFrame(query)
        df.to_csv(r'D:\Year3-2\Vulcan\Week4\get_txn.csv')
    
if __name__ == "__main__":
  asyncio.run(main())