import asyncio
import pandas as pd
from bscscan import BscScan

YOUR_API_KEY = "<YOUR API KEY>"

async def main():
  async with BscScan(YOUR_API_KEY) as bsc:
    burn = await bsc.get_bep20_token_transfer_events_by_address_and_contract_paginated(
            contract_address = "0x0e09fabb73bd3ade0a17ecc321fd13a19e81ce82",
            address= "0x000000000000000000000000000000000000dead",
            page= 1,
            offset= 300,
            sort= "asc"
    )

    df = pd.DataFrame(burn)
    print(df)
    df.to_csv(r'D:\Year3-2\Vulcan\Week3\Burn.csv')
    
if __name__ == "__main__":
  asyncio.run(main())
