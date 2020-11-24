pragma solidity >=0.4.22 <0.6.0;
 
import "./Roles.sol";
import "./Ownable.sol";
 
/**
 * @title RBAC (Role-Based Access Control)
 * @dev Stores and provides setters and getters for roles and addresses.
 * This RBAC method uses strings to key roles.
 */
 
contract RBAC is Ownable{
     
   using Roles for Roles.Role;
 
   mapping (uint => Roles.Role) private roles;
 
   event RoleAdded(address indexed operator, uint role);
   event RoleRemoved(address indexed operator, uint role);
   
   //enum RoleChoices { setBasic, setMiddle, setTop }
   //uint numRole = 3;
   //RoleChoices choice;
   //RoleChoices constant defaultChoice = RoleChoices.setBasic;
    
   //Client address
    //address internal clientAddr = 0x0000000000000000000000000000000000000000;
    //ClientInterface internal client = ClientInterface(clientAddr);
    
/*     
    /// @notice gets the address of the owner  
    /// @return the address of the owner
    function getOwner() public view returns(address){
        return client.getOwner();
    }
 */
    /// @notice sets the address of the client contract to use  
    /// @dev setting a wrong address may result in false return value, or error  
    /// @param _clientAddress the address of the client
    /// @return true if connection to the new client address was successful
/*    function setClientAddress(address _clientAddress) external onlyOwner returns (bool) { //private
        clientAddr = _clientAddress;
        client = ClientInterface(clientAddr);  
        return client.testConnection();
    }
 
    /// @notice gets the address of the client being used  
    /// @return the address of the currently set client
    function getClientAddress() external view returns (address) {  //private
        return clientAddr;
    }*/
 
   ///@dev reverts if addr does not have role
   ///@param _operator address
   ///@param _role the name of the role
   /// reverts
  function checkRole(address _operator, uint _role) view public{  //external / private
    roles[_role].check(_operator);
  }
 
   ///@dev determine if addr has role
   ///@param _operator address
   ///@param _role the name of the role
   ///@return bool
  function hasRole(address _operator, uint _role) view public returns (bool){ //external / private ->internal?
    return roles[_role].has(_operator);
  }
 
   
   ///@dev add a role to an address
   ///@param _operator address
   ///@param _role the name of the role
  function addAddressRole(address _operator, uint _role) public onlyOwner{ //external / private ->internal?
//    assert(_role < numRole);
      
/*    RoleChoices c;
      
    if(_role == 0)
        c = RoleChoices.setBasic;
    if(_role == 1)
        c = RoleChoices.setMiddle;
    else
        c = RoleChoices.setTop;
 */     
     roles[_role].add(_operator);
     emit RoleAdded(_operator, _role);
  }
 
   
   ///@dev remove a role from an address
   ///@param _operator address
   ///@param _role the name of the role
  function removeRole(address _operator, uint _role) public onlyOwner{ //external / private ->internal?
      roles[_role].remove(_operator);
      emit RoleRemoved(_operator, _role);
  }
   
 /*  /// @notice get contract type/role
   /// @return return contract type/role
  function getChoice() public view returns (RoleChoices) { //external / private
        return choice;
    }
   
   /// @notice get default role / contract type
    /// @return return default role / contract type
  function getDefaultRole() public pure returns (uint) { //external / private
        return uint(defaultChoice);
    }*/
     
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



