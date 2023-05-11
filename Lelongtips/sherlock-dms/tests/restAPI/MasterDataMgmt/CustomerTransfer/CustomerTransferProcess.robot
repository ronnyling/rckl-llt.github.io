*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/CustomerTransfer/CustomerTransferProcess.py


*** Test Cases ***
1 - Able to cancel customer transfer
    [Documentation]    Able to cancel customer transfer
    [Tags]    hqadm    9.2
    ${transfer_details}=    create dictionary
    ...    FROM_DIST=DistEgg
    ...    TO_DIST=DistB19
    ...    REASON=TR0001
    set test variable  &{transfer_details}
    Given user retrieves token access as hqadm
    When user creates customer transfer using fixed data
    Then expected return status code 201
    When user cancels created customer transfer
    Then expected return status code 200

2 - Able to confirm customer transfer
    [Documentation]    Able to confirm customer transfer
    [Tags]    hqadm    9.2
    [Teardown]  run keywords
    ...     user cancels created customer transfer
    ${transfer_details}=    create dictionary
    ...    FROM_DIST=DistEgg
    ...    TO_DIST=DistB19
    ...    REASON=TR0001
    set test variable  &{transfer_details}
    Given user retrieves token access as hqadm
    When user creates customer transfer using fixed data
    Then expected return status code 201
    When user confirms created customer transfer
    Then expected return status code 202