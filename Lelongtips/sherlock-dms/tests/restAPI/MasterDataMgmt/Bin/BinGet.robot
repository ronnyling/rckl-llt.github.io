*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Bin/BinDelete.py

*** Test Cases ***
1 - Able to get all bin data
    [Documentation]  To test get all bin data via API
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all bin data
    Then expected return status code 200

2 - Able to get bin data by valid id
    [Documentation]    To test get single bin data by valid id via API
    [Tags]    distadm    9.2
    [Teardown]   run keywords
    ...    user deletes bin
    Given user retrieves token access as ${user_role}
    When user creates bin with random data
    Then expected return status code 201
    When user retrieves bin by using valid id
    Then expected return status code 200

2 - Unable to get bin data by invalid id
    [Documentation]    To test unable to get single bin data by invalid id via API
    [Tags]    distadm    9.2
    [Teardown]   run keywords
    ...    user deletes bin
    Given user retrieves token access as ${user_role}
    When user creates bin with random data
    Then expected return status code 201
    When user retrieves bin by using invalid id
    Then expected return status code 404