*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinDelete.py

*** Test Cases ***
1 - Able to delete created Bin
    [Documentation]    To delete created bin via API
    [Tags]     distadm     9.0
    Given user retrieves token access as ${user_role}
    When user creates bin with random data
    Then expected return status code 201
    When user deletes bin
    Then expected return status code 200
