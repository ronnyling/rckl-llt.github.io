*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferGet.py


*** Test Cases ***
1 - Able to retreive all customer transfer
    [Documentation]    Able to retreive all customer transfer
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all customer transfer
    Then expected return status code 200

2 - Able to retreive customer transfer by id
    [Documentation]    Able to retreive customer transfer by id
    [Tags]    hqadm1    9.2
    Given user retrieves token access as hqadm
    When user retrieves customer transfer by id
    Then expected return status code 200