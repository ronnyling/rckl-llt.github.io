*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to delete Van using created data
    [Documentation]    To delete van using created data via API
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates van with random data
    Then expected return status code 201
    When user deletes van with created data
    Then expected return status code 200
