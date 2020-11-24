pragma solidity >=0.4.22 <0.6.0;
 
import "./Roles.sol";
 
contract RBACinterface{
     
    enum RoleChoices { setBasic, setMiddle, setTop }
    uint numRole = 3;
     
    function hasRole(address _operator, uint _role) view public returns (bool);
     
    function testConnection() public pure returns (bool);
    
     function getNumRole() public view returns(uint);
     
}


