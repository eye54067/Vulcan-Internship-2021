import asyncio
import pandas as pd
from bscscan import BscScan

YOUR_API_KEY = "FQN6F7F2VNUZD593B1GP9AMQGR77HWC39W"

async def main():
  async with BscScan(YOUR_API_KEY) as bsc:
    cake_in_pool = await bsc.get_bep20_token_transfer_events_by_address_and_contract_paginated(
            contract_address = "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
            address= "0x0eD7e52944161450477ee417DE9Cd3a859b14fD0",
            page= 1,
            offset= 1000,
            sort= "asc"
    )

    df = pd.DataFrame(cake_in_pool)
    print(df)
    df.to_csv(r'D:\Year3-2\Vulcan\Week4\cake_in_pool.csv')
    
if __name__ == "__main__":
  asyncio.run(main())

#             Pool Cake-BNB
#0x0eD7e52944161450477ee417DE9Cd3a859b14fD0   
#                LP token
#0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82