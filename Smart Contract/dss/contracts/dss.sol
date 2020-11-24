pragma solidity >=0.4.22 <0.6.0;
 
import "./Ownable.sol";
import "./RBACinterface.sol";

//WARNING: energy values has to be multiplied by 100 (for make possible consider the value like "x.ywz")
//WARING: the CRi result is multiplied by 100 (for not lose the decimal)

/// @title DataStorageSystem
/// @author Tommaso Pessina
/// @notice Collects and provides energy information
contract dss is Ownable {
    
    uint constant addPermission = 1; //Permission for adding energy (used or produced)
    uint constant getPermission = 2; //Permission for getting energy data (used or produced)
    uint constant adminPermission = 3; //Permission for adding new user or getting num. of user
    uint constant readPermission = 4; //Not used
    uint constant commonPermission = 5; //Permission for adding or getting common energy.
    
    Data[] data; 
    address[] user;
    mapping(bytes32 => uint) dataIdToIndex; //Valutare l'eliminazione
    mapping(address => uint) dataIdToAddress;
    
    uint totalEnergyProduced = 0; //KWh
    uint energyLeft = 0; //KWh //not used
    uint totalEnergyUsed = 0;
    uint totalCommonEnergyUsed = 0;
 
    uint numUser = 0; //Necessary for calculate the ripartition coeficent (of common energy used)
 
     //RBAC address
    address internal rbacAddr = 0x0000000000000000000000000000000000000000; //Initial dummy address
    RBACinterface internal rbac = RBACinterface(rbacAddr);  
 
    //defines a struct "Data"
    struct Data {
        bytes32 id; //Identificator of the data
        //address addr; //Address of who produced or used the energy
        //uint energy; //The quantity of energy
        // uint date; //The production's date of the data
        string value;
        string ts;
        string topic;
    }
    
    //Function that reset the counter of totalEnergyUsed, require adminPermission
    function resetTotalEnergyUsed(address x) public returns(uint){
        if(rbac.hasRole(x,adminPermission)){
            totalEnergyUsed = 0;
            return totalEnergyUsed;
        }else{
            return totalEnergyUsed;
        }
    }
    
    //Function that reset the counter of totalEnergyProduced, require adminPermission
    function resetTotalEnergyProduced(address x) public returns(uint){
        if(rbac.hasRole(x,adminPermission)){
            totalEnergyProduced = 0;
            return totalEnergyProduced;
        }else{
            return totalEnergyProduced;
        }
    }
    
    //Function that reset the counter of totalCommonEnergyUsed, require adminPermission
    function resetTotalCommonEnergyUsed(address x) public returns(uint){
        if(rbac.hasRole(x,adminPermission)){
            totalCommonEnergyUsed = 0;
            return totalCommonEnergyUsed;
        }else{
            return totalCommonEnergyUsed;
        }
    }
    
    //function that return the number of user in the system, require adminPermission
    function getNumUser(address x) public view returns(uint){
        if (rbac.hasRole(x,adminPermission)){
            return numUser;
        }
        else{
            return 0;
        }
    }
    
    //Function for gettin the i-th coefficient of ripartition, require adminPermission
    function getCRi(address caller) public returns (uint){
        if (rbac.hasRole(caller,adminPermission)){
            uint prodTmp = showEnergyProducedPVT();
            uint tot = showTotalEnergyUsedPVT();
            uint res = 0;
            if(prodTmp > tot){
                 res = 1; //Because the result will be divided by 100
            }else{
                uint prod = prodTmp*100; //for not lose the decimal
                res = prod/tot;
                //uint resTmp = res*100; //float not work
            }
            //unit to string
            uint ts = block.timestamp;
            string memory resString = uint2str(res);
            string memory tsString = uint2str(ts);
            addData(caller,resString,tsString,"CRi",0);
            return res; //is the real result multiplied by 100
        }
        else{
            return 0; //default value 
        }
    }   
    
 function uint2str(uint _i) public pure returns (string memory _uintAsString) {
    if (_i == 0) {
        return "0";
    }
    uint j = _i;
    uint len;
    while (j != 0) {
        len++;
        j /= 10;
    }
    bytes memory bstr = new bytes(len);
    uint k = len - 1;
    while (_i != 0) {
        bstr[k--] = byte(uint8(48 + _i % 10));
        _i /= 10;
    }
    return string(bstr);
}  

    //Function that allow to add an user, require adminPermission
    function addUser(address caller, address userIN) public returns (bool){
        if (rbac.hasRole(caller,adminPermission)){
            uint arrayLength = user.length;
            bool found=false;
            //Check if the user is already present
            for (uint i=0; i<arrayLength; i++) {
                if(user[i]==userIN){
                    found=true;
                    break;
                }
            }
            if(!found){
                numUser++;
                user.push(userIN);
                return true;
            }
            else{
                return false;
            }
        }else{
            return false;
        }
    }
    
    //Function for adding the energy produced in the data structure, require addPermission
    function addEnergyProduced(address x, string memory value,uint energy, string memory ts, string memory topic, uint option) public returns(bool){
        if(rbac.hasRole(x,addPermission)){
            totalEnergyProduced += energy;
            bytes32 tmp = addData(x,value,ts,topic,option); //call the function for adding the data
            return true;
        }else{
            return false;
        }
    }
    
    //Function for adding the common energy used by updating the counter, require commonPermission
    function addCommonEnergyUsed(address x, uint energy, string memory value, string memory ts, string memory topic, uint option) public returns(bool){
        if(rbac.hasRole(x,commonPermission)){
            totalCommonEnergyUsed += energy;
            totalEnergyUsed += energy;
            bytes32 tmp = addData(x,value,ts,topic,option); //call the function for adding the data
            return true;
        }else{
            return false;
        }
    }
    
    //function for getting the common energy used (his counter), require getPermission
    function getCommonEnergyUsed(address x) public view returns(uint){
        require(rbac.hasRole(x,getPermission));
        return totalCommonEnergyUsed;
    }
    
    //function for the ripartition of the common energy used by the num of user, require getPermission  
    function getRipartitionCoeficent(address x) public view returns(uint){
        require(rbac.hasRole(x,getPermission));
        uint energy = getCommonEnergyUsed(x);
        uint nUser = getNumUser(x);
        return energy/nUser; 
    }
    
    function addEnergyUsed(address x, string memory value, uint energy, string memory ts, string memory topic, uint option) public returns(bool){
        assert(rbac.hasRole(x,addPermission));
        
        totalEnergyUsed += energy;
        
        bytes32 tmp = addData(x,value,ts,topic,option);
        
        if(tmp!=0){
            return true;
        }
        else{
            return false;
        }
        /*
        //Create a unique id
        bytes32 id = keccak256(abi.encodePacked(energy,x));
        //Check that the id does not already exists
        require(!dataExists(id));
     
        //If there is nothing, add data
        if(dataIdToAddress[x] == 0){
            uint newIndex = data.push(Data(id, x, energy))-1;  
            dataIdToIndex[id] = newIndex+1;
            dataIdToAddress[x] = newIndex+1;
            return true;
        }
        //If there is a data, update that
        else{
            uint oldEnergy = showEnergyUsedPVT(x);
            uint newIndex = data.push(Data(id, x, energy+oldEnergy))-1;  
            dataIdToIndex[id] = newIndex+1;
            dataIdToAddress[x] = newIndex+1;
            return true;
        }*/
    }
    
    //Function for adding the data in the smart contract. This can only be called by the other function, so is private.
    function addData(address caller, string memory value, string memory ts, string memory topic, uint option) private returns (bytes32){
         //Create a unique id
        bytes32 id = keccak256(abi.encodePacked(caller,value,ts,topic));
        //Check that the id does not already exists
        require(!dataExists(id));
        uint newIndex = data.push(Data(id, value, ts, topic))-1;  
        dataIdToIndex[id] = newIndex+1;
        return id;
    }
    
    /// @notice gets the unique ids of data, pending and read, in reverse chronological order
    /// @return an array of unique data ids
    function getAllData(address x) public view returns (bytes32[] memory) {
        assert(rbac.hasRole(x,getPermission));
        bytes32[] memory output = new bytes32[](data.length); 

        //get all ids 
        if (data.length > 0) {
            uint index = 0;
            for (uint n = data.length; n > 0; n--) {
                output[index++] = data[n-1].id;
            }
        }
        
        return output; 
    }

    
    function _getDataByAddress(address a) private view returns (uint) {
        return dataIdToAddress[a]-1;  
    }
    
/*    function showEnergyUsed(address call, address x) public view returns (uint){
        require(rbac.hasRole(call,getPermission));
        Data storage theData = data[_getDataByAddress(x)];
        return theData.energy;  
    }*/
    
/*    function showEnergyUsedPVT(address x) private view returns (uint){
        Data storage theData = data[_getDataByAddress(x)];
        return theData.energy;  
    }*/
    
    /* NOT implemented
    function showEnergyLeft(address caller) public returns (uint){
        
    }*/
    
    //function for showing the data given the id. Require getPermission
    function showData(address caller, bytes32 id) public view returns(string memory value, string memory ts, string memory topic){
        //check if data exits (given an id)
        if(rbac.hasRole(caller, getPermission)){
            if (dataExists(id)) {
                Data storage theData = data[_getDataIndex(id)];
                return (theData.value, theData.ts, theData.topic); 
            }
            else {
                return ("0","0","");
            }
        }else{
            return ("0","0","");
        }
    }
    
    
    //Function that show the counter of totalEnergyUsed, require getPermission
    function showTotalEnergyUsed(address caller) public view returns (uint){
        require(rbac.hasRole(caller,getPermission));
        return totalEnergyUsed;
    }
    
    //Function that show the counter of totalEnergyUsed, ONLY for ptivate use.
    function showTotalEnergyUsedPVT() private view returns (uint){
        return totalEnergyUsed;
    }
    
    //function that show the total energy produced, require getPermission
    function showEnergyProduced(address caller) public view returns (uint){
        require(rbac.hasRole(caller,getPermission));
        return totalEnergyProduced;
    }
    
    //Function that show the total energy produced, ONLY for private use
    function showEnergyProducedPVT() private view returns (uint){
        return totalEnergyProduced;
    }
     
     /// @notice sets the address of the rbac contract to use  
    /// @dev setting a wrong address may result in false return value, or error  
    /// @param _rbacAddress the address of the rbac  
    /// @return true if connection to the new rbac address was successful
    function setRBACaddress(address _rbacAddress) external onlyOwner returns (bool) {
        rbacAddr = _rbacAddress;
        rbac = RBACinterface(rbacAddr);  
        return rbac.testConnection();
    }
     
    /// @notice gets the address of the dss being used  
    /// @return the address of the currently set dss  
    function getRBACaddress() external view returns (address) {
        return rbacAddr;
    }
     
    /// @notice for testing; tests that the dss is callable  
    /// @return true if connection successful  
    function testRBACconnection() public view returns (bool) {
        return rbac.testConnection();  
    }
 
    /// @notice returns the array index of the data with the given id  
    /// @dev if the data id is invalid, then the return value will be incorrect and may cause error;
    /// @param dataId the data id to get
    /// @return an array index  
    function _getDataIndex(bytes32 dataId) private view returns (uint) {
        if(dataExists(dataId))
            return dataIdToIndex[dataId]-1;  
    }
 
 
    /// @notice determines whether a data exists with the given id  
    /// @param _dataId the data id to test
    /// @return true if data exists and id is valid
    function dataExists(bytes32 _dataId) public view returns (bool) {  //private?
        if (data.length == 0)
            return false;
        uint index = dataIdToIndex[_dataId];  
        return (index > 0);  
    }

    /// @notice can be used by a client contract to ensure that they've connected to this contract interface successfully
    /// @return true, unconditionally  
    function testConnection() public pure returns (bool) {
        return true;  
    }
 
    /// @notice gets the address of this contract  
    /// @return address  
    function getAddress() public view returns (address) {
        return address(this);
    }

}



