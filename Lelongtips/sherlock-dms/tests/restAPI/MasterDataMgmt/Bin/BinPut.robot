*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinDelete.py

Test Teardown  run keywords
...    user deletes bin

*** Test Cases ***
1 - Able to update Bin using random data
    [Documentation]    To update bin using random data via API
    [Tags]     distadm     9.2
    Given user retrieves token access as ${user_role}
    And user creates bin with random data
    When user updates bin with random data
    Then expected return status code 200

2 - Able to update Bin using fixed data
    [Documentation]    To update bin using fixed data via API
    [Tags]     distadm     9.2
    ${new_bin_details}=    create dictionary
    ...    SINGLE_MULTIPLE=${false}
    ...    PICKING_AREA=${false}
    ...    RACK=19
    ...    COLUMN=15
    ...    LEVEL=13
    ...    BIN_DESC=Put Bin
    ...    REMARKS=bin put test
    set test variable   &{new_bin_details}
    Given user retrieves token access as ${user_role}
    And user creates bin with random data
    When user updates bin with fixed data
    Then expected return status code 200