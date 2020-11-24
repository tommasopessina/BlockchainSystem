#This script set the given RBAC address in the dss's contract
#dss

import json
from web3 import Web3
import sys
import binascii

if len(sys.argv)!=3:	
 print("Please insert (1) dss address (2) RBAC address")
 sys.exit(0)

address = Web3.toChecksumAddress(str(sys.argv[1]))
rbacAddress = Web3.toChecksumAddress(str(sys.argv[2]))

print("Inserted RBAC address:",rbacAddress)

url = "http://127.0.0.1:8543"
web3 = Web3(Web3.HTTPProvider(url))

print("Blockchain connected? ", web3.isConnected())
    
print("Actual block number? ", web3.eth.blockNumber)

account = web3.toChecksumAddress("0x63fdc9b9b6840f52fe2b4906142cff1f4283ae42")
web3.geth.personal.unlockAccount(account,'seed')

abi = json.loads('[{"constant":true,"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"showTotalEnergyUsed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"resetTotalEnergyUsed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"bytes32","name":"_dataId","type":"bytes32"}],"name":"dataExists","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"testConnection","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"pure","type":"function"},{"constant":true,"inputs":[],"name":"dateExipration","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getAddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"testRBACconnection","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"getCommonEnergyUsed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"x","type":"address"},{"internalType":"string","name":"value","type":"string"},{"internalType":"uint256","name":"energy","type":"uint256"},{"internalType":"string","name":"ts","type":"string"},{"internalType":"string","name":"topic","type":"string"},{"internalType":"uint256","name":"option","type":"uint256"}],"name":"addEnergyUsed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"resetTotalCommonEnergyUsed","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"x","type":"address"},{"internalType":"uint256","name":"energy","type":"uint256"},{"internalType":"string","name":"value","type":"string"},{"internalType":"string","name":"ts","type":"string"},{"internalType":"string","name":"topic","type":"string"},{"internalType":"uint256","name":"option","type":"uint256"}],"name":"addCommonEnergyUsed","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"getAllData","outputs":[{"internalType":"bytes32[]","name":"","type":"bytes32[]"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"caller","type":"address"},{"internalType":"bytes32","name":"id","type":"bytes32"}],"name":"showData","outputs":[{"internalType":"string","name":"value","type":"string"},{"internalType":"string","name":"ts","type":"string"},{"internalType":"string","name":"topic","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"x","type":"address"},{"internalType":"string","name":"value","type":"string"},{"internalType":"uint256","name":"energy","type":"uint256"},{"internalType":"string","name":"ts","type":"string"},{"internalType":"string","name":"topic","type":"string"},{"internalType":"uint256","name":"option","type":"uint256"}],"name":"addEnergyProduced","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"resetTotalEnergyProduced","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"caller","type":"address"},{"internalType":"address","name":"userIN","type":"address"}],"name":"addUser","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"getRipartitionCoeficent","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"getRBACaddress","outputs":[{"internalType":"address","name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"_rbacAddress","type":"address"}],"name":"setRBACaddress","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"showEnergyProduced","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"internalType":"address","name":"x","type":"address"}],"name":"getNumUser","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"internalType":"address","name":"caller","type":"address"}],"name":"getCRi","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[{"internalType":"uint256","name":"_i","type":"uint256"}],"name":"uint2str","outputs":[{"internalType":"string","name":"_uintAsString","type":"string"}],"payable":false,"stateMutability":"pure","type":"function"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"}]')

mContract = web3.eth.contract(address=address, abi=abi)

print("Contract's functions:")
print(mContract.all_functions())

num = mContract.functions.getAddress().call()
print("Contract address:",num)

with open("/home/tompe/Scrivania/STAGE/Condominio1/blkchain/keystore/UTC--2019-04-10T12-45-54.049858200Z--63fdc9b9b6840f52fe2b4906142cff1f4283ae42") as keyfile:
       encrypted_key = keyfile.read()
       private_key = web3.eth.account.decrypt(encrypted_key,'seed')

contract_data = mContract.functions.setRBACaddress(rbacAddress).buildTransaction({'from': account,
                                                          'gas': 1728712,
                                                          'gasPrice': web3.toWei('21', 'gwei')})
contract_data["to"] = address
contract_data["nonce"] = web3.eth.getTransactionCount(account)
signed = web3.eth.account.signTransaction(contract_data, private_key)
tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

num = mContract.functions.getRBACaddress().call()
print("RBAC address:",num)

