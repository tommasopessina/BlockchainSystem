var client = artifacts.require("client.sol");

module.exports = function(deployer) {
  deployer.deploy(client);
};
