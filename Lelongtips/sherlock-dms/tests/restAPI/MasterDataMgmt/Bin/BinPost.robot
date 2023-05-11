*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinDelete.py

Test Teardown  run keywords
...    user deletes bin

*** Test Cases ***
1 - Able to post Bin with random data
    [Documentation]    Able to post bin data via API
    [Tags]     distadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates bin with random data
    Then expected return status code 201

2. Able to post Bin with fixed data
    [Documentation]    Able to post fixed bin data via API
    [Tags]    distadm    9.2
    ${bin_details}=    create dictionary
    ...    SINGLE_MULTIPLE=${true}
    ...    PICKING_AREA=${true}
    ...    BIN_CODE=BCD1715
    ...    RACK=9
    ...    COLUMN=5
    ...    LEVEL=3
    ...    BIN_DESC=Bin Fixed Data
    ...    REMARKS=bin post fixed
    set test variable   &{bin_details}
    Given user retrieves token access as ${user_role}
    When user creates bin with fixed data
    Then expected return status code 201
