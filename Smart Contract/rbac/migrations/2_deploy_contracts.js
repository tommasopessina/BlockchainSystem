var rbac = artifacts.require("RBAC.sol");

module.exports = function(deployer) {
  deployer.deploy(rbac);
};