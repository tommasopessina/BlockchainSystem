# BlockchainSystem

This file contain very usefull and important commands

-------------------SUGGESTION------------------------

1) ALWAYS SAVE THE ADDRESS OF THE DEPLOYED CONTRACT (IN ORDER TO BE ABLE TO WORK WITH IT)
2) THE ABI INSIDE THE PYTHON SCRIPT IS EQUAL TO THE ONE PRODUCED BY THE COMPILATION OF TRUFFLE (under build/contract/*)

----------------------REQUISITE---------------------------------

1) CREATE AT LEAST 3 ACCOUNTS, I.E. 1 CLIENT, 1 RBAC AND 1 DSS
2) CHANGE IN EACH PYTHON SCRIPT THE ADDRESS OF THE ACCOUNT TO WHICH IT REFERS -> room for improvements
3) CHANGE IN EACH PYTHON SCRIPT THAT REFER TO THE BROKER THE IP/PORT OF IT -> room from improvements

-----------------------BLOCKCHAIN------------------------ 

->BLOCKCHAIN INITIALIZATION

mkdir blkchain
geth --datadir blkchain init genesis.json

->BRING UP BLOCKCHAIN

geth --port 3000 --networkid 58343 --nodiscover --datadir=./blkchain --maxpeers=0  --rpc --rpcport 8543 --rpcaddr 127.0.0.1 --rpccorsdomain "*" --rpcapi "eth,net,web3,personal,miner" --allow-insecure-unlock

-> CONNECT TO BLOCKCHAIN

geth attach http://127.0.0.1:8543  -> ! IP:PORT ACCCORDING TO THE COMMAND ABOVE ! <-

-> USEFULL COMMANDS FOR THE GETH CONSOLE

1) miner.start()
2) miner.stop()
3) personal.unlockAccount("address","password")

------------------------SMART CONTRACT---------------------------

-> INITIALIZE THE ENVIRONMENT (inside the desired directory)
	-> ! NECESSARY ONLY THE FIRST TIME (OR if you plan to start all the process from scratch) ! <-
 
truffle init 

-> OPEN TRUFFLE CONSOLE (INTERACTION WITH SMART CONTRACT)

truffle console

-> COMPILE SMART CONTRACT (IN THE TRUFFLE CONSOLE)

truffle compile

-> MIGRATE A CONTRACT IN BLOCKCHAIN (FROM TRUFFLE CONSOLE) -> AFTER HAVING CREATED THE deploy-contract.js FILE
	-> IT WILL RETURN THE ADDRESS OF THE CONTRACT *SAVE IT*

truffle migrate

-> INTERACTION WITH A DEPLOYED CONTRACT IN BLOCKCHAIN

var dApp
ContactName.deployed().then(function(instance) { dApp = instance; })

-> OTHER INFO

1) By running "truffle init" will be created some directory and file that can be used as example
2) truffle-config.js SHOULD BE LIKE:

module.exports = {
	networks: {
		development: {
		  host: "localhost",	-> ACCORDING TO YOUR IP ADRESS OF THE BLOCKCHAIN
		  port: 8543,		-> ACCORDING TO YOUR PORT OF THE BLOCKCHAIN
		  from:"0x70592e1302d25bcd701b89e82bd80611fa1103e2", -> CHANGE WITH THE ADDRESS OF THE ACCOUNT THAT DEPLOY THE CONTRACT
		  network_id: "*" // Match any network id
		}
	},
compilers: {
  	solc: {
		version:"0.5.11",
		settings: {
		      evmVersion: "byzantium"
		    }
	}
    }	
};

3) IN ORDER TO DEPLOY A CONTRACT THE 2_deploy_contracts.js SHOULD BE LIKE:

var dss = artifacts.require("SMART_CONTRACT_NAME.sol");

module.exports = function(deployer) {
  deployer.deploy(dss);
};


