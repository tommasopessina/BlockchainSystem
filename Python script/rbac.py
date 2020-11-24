#ONLY TESTING SCRIPT

import json
from web3 import Web3
import sys

if len(sys.argv)!=2:	
 print("Please insert the RBAC address")
 sys.exit(0)

address = Web3.toChecksumAddress(str(sys.argv[1]))

url = "http://127.0.0.1:8543"
web3 = Web3(Web3.HTTPProvider(url))

print("Blockchain connected? ", web3.isConnected())

print("Actual block number? ", web3.eth.blockNumber)

account = web3.toChecksumAddress("0xc7733379aed8f2eee08622a47d26826cdb072793")

web3.geth.personal.unlockAccount(account,'seed')

abi = json.loads('[{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"uint256","name":"_role","type":"uint256"}],"name":"addAddressRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"testConnection","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"dateExipration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"uint256","name":"_role","type":"uint256"}],"name":"checkRole","outputs":[],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"uint256","name":"_role","type":"uint256"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_operator","type":"address"},{"internalType":"uint256","name":"_role","type":"uint256"}],"name":"removeRole","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"uint256","name":"role","type":"uint256"}],"name":"RoleAdded","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"uint256","name":"role","type":"uint256"}],"name":"RoleRemoved","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"}]')

mContract = web3.eth.contract(address=address, abi=abi)

print("Contract's functions:")
print(mContract.all_functions())

print("Trying to get contract address...")
num = mContract.functions.getAddress().call()
print(num, "-> YES, IT WORKS!")
