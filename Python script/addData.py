#Called by the script that check for mqtt message, this is the script responsable for putting data in blockchain
#client

import json
from web3 import Web3
import sys
import binascii

mex = sys.argv[1]
topic = sys.argv[2]
data = json.loads(mex)
#f = open("/home/tompe/Scrivania/STAGE/Condominio1/test.txt",'a+')
#f.write(mex+"\n")
#f.close()
valueStr = data["value"]
valueInt = int(float(valueStr)*100)
ts = data["ts"]

address = Web3.toChecksumAddress(str(sys.argv[3]))

url = "http://127.0.0.1:8543"
web3 = Web3(Web3.HTTPProvider(url))

account = web3.toChecksumAddress("0x70592e1302d25bcd701b89e82bd80611fa1103e2")
web3.geth.personal.unlockAccount(account,'seed')

with open("/home/tompe/Scrivania/STAGE/Condominio1/blkchain/keystore/UTC--2019-04-10T12-45-42.429769100Z--70592e1302d25bcd701b89e82bd80611fa1103e2") as keyfile:
       encrypted_key = keyfile.read()
       private_key = web3.eth.account.decrypt(encrypted_key,'seed')

abi = json.loads("""[
	{
		"anonymous": false,
		"inputs": [
			{
				"indexed": true,
				"internalType": "address",
				"name": "previousOwner",
				"type": "address"
			},
			{
				"indexed": true,
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "OwnershipTransferred",
		"type": "event"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "uint256",
				"name": "energy",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "value",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ts",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "topic",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "option",
				"type": "uint256"
			}
		],
		"name": "addCommonEnergyUsed",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "string",
				"name": "value",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "energy",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "ts",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "topic",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "option",
				"type": "uint256"
			}
		],
		"name": "addEnergyProduced",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "string",
				"name": "value",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "energy",
				"type": "uint256"
			},
			{
				"internalType": "string",
				"name": "ts",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "topic",
				"type": "string"
			},
			{
				"internalType": "uint256",
				"name": "option",
				"type": "uint256"
			}
		],
		"name": "addEnergyUsed",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "address",
				"name": "a",
				"type": "address"
			}
		],
		"name": "addUser",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getAllDataId",
		"outputs": [
			{
				"internalType": "bytes32[]",
				"name": "",
				"type": "bytes32[]"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "getCRi",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getCommonEnergyUsed",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getOwner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getRipartitionCoeficent",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getUser",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "getdssAddress",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "owner",
		"outputs": [
			{
				"internalType": "address",
				"name": "",
				"type": "address"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "resetTotalCommonEnergyUsed",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "resetTotalEnergyProduced",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [],
		"name": "resetTotalEnergyUsed",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "address",
				"name": "_dssAddress",
				"type": "address"
			}
		],
		"name": "setdssAddress",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "bytes32",
				"name": "id",
				"type": "bytes32"
			}
		],
		"name": "showData",
		"outputs": [
			{
				"internalType": "string",
				"name": "value",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "ts",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "topic",
				"type": "string"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "showEnergyProduced",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [
			{
				"internalType": "address",
				"name": "x",
				"type": "address"
			}
		],
		"name": "showEnergyUsed",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "showTotalEnergyUsed",
		"outputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "testConnection",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": true,
		"inputs": [],
		"name": "testdssConnection",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"payable": false,
		"stateMutability": "view",
		"type": "function"
	},
	{
		"constant": false,
		"inputs": [
			{
				"internalType": "address",
				"name": "newOwner",
				"type": "address"
			}
		],
		"name": "transferOwnership",
		"outputs": [],
		"payable": false,
		"stateMutability": "nonpayable",
		"type": "function"
	}
]""")

mContract = web3.eth.contract(address=address, abi=abi)

if topic == "home_sim/pv/active_power":
    #produzione fotovoltaica
    contract_data = mContract.functions.addEnergyProduced(valueStr,valueInt,ts,topic,0).buildTransaction({'from': account,
                                                              'gas': 1728712,
                                                              'gasPrice': web3.toWei('21', 'gwei')})
    contract_data["to"] = address
    contract_data["nonce"] = web3.eth.getTransactionCount(account)
    signed = web3.eth.account.signTransaction(contract_data, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)
elif topic == "home_sim/load/active_power":
    #consumo vero e proprio di tutti i carichi esclusi i sistemi di accumulo (singola utenza)
    contract_data = mContract.functions.addEnergyUsed(valueStr,valueInt,ts,topic,0).buildTransaction({'from': account,
                                                              'gas': 1728712,
                                                              'gasPrice': web3.toWei('21', 'gwei')})
    contract_data["to"] = address
    contract_data["nonce"] = web3.eth.getTransactionCount(account)
    signed = web3.eth.account.signTransaction(contract_data, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed.rawTransaction)
    tx_receipt = web3.eth.waitForTransactionReceipt(tx_hash)

dataID = mContract.functions.getAllDataId().call()

for id in dataID:
    print(mContract.functions.showData(id).call())

