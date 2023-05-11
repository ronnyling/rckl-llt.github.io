*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferPost.py


*** Test Cases ***
1 - Able to POST customer transfer
    [Documentation]    Able to create customer transfer
    [Tags]    hqadm    9.2
    ${transfer_details}=    create dictionary
    ...    FROM_DIST=DistEgg
    ...    TO_DIST=DistB19
    ...    REASON=TR0001
    set test variable  &{transfer_details}
    Given user retrieves token access as hqadm
    When user creates customer transfer using fixed data
    Then expected return status code 201