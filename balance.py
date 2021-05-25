from web3 import Web3
import requests
import json
import time


infura_url = "https://mainnet.infura.io/v3/0d4ea061d3654026850566e67389f15c"

web3 = Web3(Web3.HTTPProvider(infura_url))

web3.isConnected()

address = input("Enter Valid Eth Address: " )
Web3.isChecksumAddress(address)
# print(Web3.toWei(0xe08e5bb6a766c7649bb88f321a0a1cdaad40892c, 'ether'))

# print(web3.fromWei(balance, 'ether'))
# print(balance)

# Currency eth to usd
while True:
    balance = web3.eth.getBalance(address)
    eth = web3.fromWei(balance, 'ether')
    response = requests.get('https://api.coinbase.com/v2/prices/ETH-USD/spot')
    data = response.json()
    currency = data["data"] ["base"]
    prices = data["data"] ["amount"]
    usdt = (float(prices)*float(eth))
    print("Your Eth Balance is : ", eth)
    print(f"Your Price in USDT is : {usdt}")
    time.sleep(5)
