/*
 * NB: since truffle-hdwallet-provider 0.0.5 you must wrap HDWallet providers in a 
 * function when declaring them. Failure to do so will cause commands to hang. ex:
 * ```
 * mainnet: {
 *     provider: function() { 
 *       return new HDWalletProvider(mnemonic, 'https://mainnet.infura.io/<infura-key>') 
 *     },
 *     network_id: '1',
 *     gas: 4500000,
 *     gasPrice: 10000000000,
 *   },
 */

module.exports = {
	networks: {
		development: {
		  host: "localhost",
		  port: 8543,
		from:"0x63fdc9b9b6840f52fe2b4906142cff1f4283ae42",
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
