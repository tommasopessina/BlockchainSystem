pragma solidity >=0.4.22 <0.6.0;

/**
 * @title Roles
 * @dev Library for managing addresses assigned to a Role.
 */
library Roles {
    
  struct Role {
    mapping (address => bool) bearer;
  }

  /**
   * @dev give an address access to this role
   */
  function add(Role storage role, address addr) internal{
    
      require(addr != address(0x0000000000000000000000000000000000000000));
      require(!has(role, addr));
        
      role.bearer[addr] = true;
  }

  /**
   * @dev remove an address access to this role
   */
  function remove(Role storage role, address addr) internal{
      
      require(addr != address(0x0000000000000000000000000000000000000000));
      require(has(role, addr));
      
      role.bearer[addr] = false;
  }

  /**
   * @dev check if an address has this role
   */
  function check(Role storage role, address addr) view internal{
      
      require(addr != address(0x0000000000000000000000000000000000000000));
      
      require(has(role, addr));
  }

  /**
   * @dev check if an address has this role
   * @return bool
   */
  function has(Role storage role, address addr) view internal returns (bool) {
      
      require(addr != address(0x0000000000000000000000000000000000000000));
      
      return role.bearer[addr];
  }
  
}

