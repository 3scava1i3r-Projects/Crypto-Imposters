// SPDX-License-Identifier: GPL-3.0-or-later
pragma solidity ^0.8.4;

import {DInterest} from "./88mph-contracts/DInterest.sol";


contract ImposterFactory is DInterest {


    function Mint(
    string memory uri,
    uint256 depositAmount,
    uint64 maturationTimestamp) public returns (uint256 ImposterId){
        _deposit(
                msg.sender,
                depositAmount,
                maturationTimestamp,
                false,
                0,
                uri
            );
    }


    //game logic


}
