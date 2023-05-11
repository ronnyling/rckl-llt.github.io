*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferDelete.py


*** Test Cases ***
1 - Able to delete customer transfer
    [Documentation]    Able to delete customer transfer
    [Tags]    hqadm
    ${transfer_details}=    create dictionary
    ...    FROM_DIST=DistEgg
    ...    TO_DIST=DistB19
    ...    REASON=TR0001
    set test variable  &{transfer_details}
    Given user retrieves token access as hqadm
    And user creates customer transfer using fixed data
    When user delete created customer transfer
    Then expected return status code 200