#week5_4 Filter contract address รันกับblockที่มาใหม่เรื่อยๆ ต้องกดหยุดเอง
#Credit : Earth


from web3.auto.gethdev import Web3
from web3.middleware import geth_poa_middleware
import time

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract_address = "0x0eD7e52944161450477ee417DE9Cd3a859b14fD0"

tx = []
def handle_event(event):
    print(event['address'],"Block",event['blockNumber'],"\nHash",w3.toHex(event['transactionHash']),"\n")
    tx.append(event)

#print(event) #too many data

"""def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)"""

def main():
    block_filter = w3.eth.filter({"address": contract_address})
    block_filter
if __name__ == '__main__':
    main()