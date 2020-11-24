pragma solidity >=0.4.22 <0.6.0;
 
contract dssInterface {
 
/*    enum dataState{
        pending,
        read
    }*/
    
    //ALL PUBLIC??
 
    function getPendinData(address x) public returns (bytes32[] memory);
 
    function dataExists(bytes32 _dataId) public view returns (bool);  
 
    function getData(bytes32 _dataId) public view returns (
        bytes32 id,
        string memory name,  
        string memory otherInfo,
        uint sensorData,
        //dataState state
        bool read);
 
    function getMostRecentData(bool _pending) public view returns (
        bytes32 id,
        string memory name,  
        string memory otherInfo,
        uint sensorData,
        //dataState state
        bool read);
 
 
    function testConnection() public pure returns (bool);
    
    function getNumUser(address x) public view returns(uint);
    
    function addUser(address caller, address userIN) public returns (bool);
    
    function addEnergyUsed(address x, string memory value, uint energy, string memory ts, string memory topic, uint option) public returns(bool);

    function showEnergyUsed(address call, address x) public view returns (uint);
    
    function addEnergyProduced(address x, string memory value,uint energy, string memory ts, string memory topic, uint option) public returns(bool);
    
    function addCommonEnergyUsed(address x, uint energy, string memory value, string memory ts, string memory topic, uint option) public returns(bool);
    
    function getCommonEnergyUsed(address x) public view returns(uint);
    
    function getRipartitionCoeficent(address x) public view returns(uint);
    
    function showTotalEnergyUsed(address caller) public view returns (uint);
    
    function showEnergyProduced(address caller) public view returns (uint);
    
    //function below are not implementi in client!!!
    
    function resetTotalEnergyUsed(address x) public returns(uint);
    
    function resetTotalEnergyProduced(address x) public returns(uint);
    
    function resetTotalCommonEnergyUsed(address x) public returns(uint);
    
    //function below are implemented !
    
    function showData(address caller, bytes32 id) public view returns(string memory value, string memory ts, string memory topic);
    
    function addData(address caller, string memory value, string memory ts, string memory topic, uint option) private returns (bytes32);
 
    function getAllData(address x) public view returns (bytes32[] memory);
    
    function getCRi(address caller) public returns (uint);
}



