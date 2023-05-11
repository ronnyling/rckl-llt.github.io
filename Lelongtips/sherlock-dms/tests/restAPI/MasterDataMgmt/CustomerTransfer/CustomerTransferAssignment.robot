*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferAssignment.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerDelete.py


*** Test Cases ***
1 - Able to assign customer to transfer
    [Documentation]    Able to assign customer to transfer
    [Tags]    hqadm    9.2
    [Teardown]  run keywords
    ...     user deletes created customer data
    Given user retrieves token access as distadm
    When user creates customer with random data
    Then user assign hierarchy
    ${transfer_details}=    create dictionary
    ...    FROM_DIST=DistEgg
    ...    TO_DIST=DistB19
    ...    REASON=TR0001
    set test variable  &{transfer_details}
    Given user retrieves token access as hqadm
    When user creates customer transfer using fixed data
    Then expected return status code 201
    ${assignment_details}=    create dictionary
    ...    GEO_TREE=General Geo Tree
    ...    FROM_NODE=Not Bahagia
    ...    TO_NODE=TerritoryB19
    set test variable  &{assignment_details}
    When user assigns customer to created transfer
    Then expected return status code 200