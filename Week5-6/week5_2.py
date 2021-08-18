#week5_2  ดึง Transaction Hash ที่ส่งไปหา Contract Address จากการใช้ Block no.หา

from web3.auto.gethdev import Web3
from web3.middleware import geth_poa_middleware

w3 = Web3(Web3.HTTPProvider('https://bsc-dataseed.binance.org/'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

block = 8709221
address = '0x0eD7e52944161450477ee417DE9Cd3a859b14fD0'
gb = w3.eth.get_block(block)
print("Block",block," Transaction count:",len(gb['transactions']),"\nTxHash of sending to",address)
for i in gb['transactions']:
    if(w3.eth.getTransaction(i)['to'] == address):
        print(w3.toHex(w3.eth.getTransaction(i)['blockHash']))