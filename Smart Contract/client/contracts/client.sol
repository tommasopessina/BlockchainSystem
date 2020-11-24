pragma solidity >=0.4.22 <0.6.0;
 
import "./dssInterface.sol";
import "./Ownable.sol";
 
 
/// @title Client
/// @author Tommaso Pessina
/// @notice Client is who use energy.
contract client is Ownable {
    
    //ENERGY is integer value -> Multuplied by 100
    //VALUE is the string value of energy
     
    /// @notice get contract owner
    /// @return the address of contract owner
    function getOwner() public view returns(address){
        return owner;
    }
 
    //data dss  
    address internal dssAddr = 0x0000000000000000000000000000000000000000;
    dssInterface internal dss = dssInterface(dssAddr);  
    
    //Get numer of user that is equals to how many electric meter (or family in condominium)
    //It must has the correct role for do that
    function getUser() public onlyOwner view returns(uint){
        return dss.getNumUser(msg.sender);
    }
    
    //Require admin permission
    function resetTotalEnergyUsed() public returns(uint){
        return dss.resetTotalEnergyUsed(msg.sender);
    }
    
    //Require admin permission
    function resetTotalEnergyProduced() public returns(uint){
        return dss.resetTotalEnergyProduced(msg.sender);
    }
    
    //Require admin permission
    function resetTotalCommonEnergyUsed() public returns(uint){
        return dss.resetTotalCommonEnergyUsed(msg.sender);
    }
    
    //Require admin permission
    function getCRi() public returns (uint){
        return dss.getCRi(msg.sender); //the result is multiplied by 100 for not lose the decimal
    }
    
    /*function addData(string memory value, uint ts, string memory topic, uint option) public returns(bytes32){
        return dss.addData(msg.sender, value, ts, topic, option);
    }*/
    
    //Show data's details given the id. Require get permission
    function showData(bytes32 id) public view returns(string memory value, string memory ts, string memory topic){
        return  dss.showData(msg.sender,  id);
    }
    
    //Get all the dataID for getting the single value. Require get permission
    function getAllDataId() public view returns (bytes32[] memory) {
        return dss.getAllData(msg.sender); 
    }
    
    //Add a user in the system. Each electric meter has a contract
    //It must has the correct role for do that
    function addUser(address a) public onlyOwner returns (bool){
        return dss.addUser(msg.sender,a);
    }
    
    //Add the energy used by the electric meter that call the function. 
    //It must has the correct role for do that
    function addEnergyUsed(string memory value,uint energy, string memory ts, string memory topic, uint option) public onlyOwner returns(bool){
        return dss.addEnergyUsed(msg.sender,value,energy,ts,topic,option);
    }

    //Show the energy used by a given electric meter address.
    //It must has the correct role for do that. Generally done by the supplier
    function showEnergyUsed(address x) public onlyOwner view returns (uint){
        return dss.showEnergyUsed(msg.sender,x);
    }
    
    //Add the energy produced.
    //It must has the correct role for do that. Generally done by the electric meter of the energy producuer.
    function addEnergyProduced(string memory value,uint energy, string memory ts, string memory topic, uint option) public returns(bool){
        return dss.addEnergyProduced(msg.sender,value,energy,ts,topic,option);
    }
    
    //Add the energy used by the common utilities.
    //It must has the correct role for do that. Generally done by the electric meter of the common utilities.
    function addCommonEnergyUsed(uint energy,string memory value, string memory ts, string memory topic, uint option) public returns(bool){
        return dss.addCommonEnergyUsed(msg.sender,energy,value,ts,topic,option);
    }
    
    //Get the energy used by the common utilities.
    //It must has the correct role for do that.
    function getCommonEnergyUsed() public view returns(uint){
        return dss.getCommonEnergyUsed(msg.sender);
    }
    
    //Get the ripartition of the common utilities (according to the number of user)
    //It must has the correct role for do that.
    function getRipartitionCoeficent() public view returns(uint){
        return dss.getRipartitionCoeficent(msg.sender);
    }
    
    //Show the total energy used by the condominium.
    //It must has the correct role for do that.
    function showTotalEnergyUsed() public view returns(uint){
        return dss.showTotalEnergyUsed(msg.sender);
    }
    
    //Show all the energy produced progressively.
    //It must has the correct role for do that.
    function showEnergyProduced() public view returns(uint){
        return dss.showEnergyProduced(msg.sender);
    }
 
    /// @notice sets the address of the dss contract to use  
    /// @dev setting a wrong address may result in false return value, or error  
    /// @param _dssAddress the address of the dss  
    /// @return true if connection to the new dss address was successful
    function setdssAddress(address _dssAddress) public onlyOwner returns (bool) { //private
        dssAddr = _dssAddress;
        dss = dssInterface(dssAddr);  
        return dss.testConnection();
    }
 
    /// @notice gets the address of the dss being used  
    /// @return the address of the currently set dss  
    function getdssAddress() external view returns (address) { //private
        return dssAddr;
    }
 
    /// @notice can be used by a client contract to ensure that they've connected to this contract interface successfully
    /// @return true, unconditionally  
    function testConnection() public pure returns (bool) {
        return true;  
    }
 
    /// @notice for testing; tests that the dss is callable  
    /// @return true if connection successful  
    function testdssConnection() public view returns (bool) {
        return dss.testConnection();  
    }
     
}



