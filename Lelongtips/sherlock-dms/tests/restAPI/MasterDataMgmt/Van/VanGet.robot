*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to retrieve all Van data
    [Documentation]  To retrieve all van record via API
    [Tags]    distadm     9.0
    Given user retrieves token access as ${user_role}
    When user creates van with random data
    Then expected return status code 201
    When user gets all van data
    Then expected return status code 200
    When user deletes van with created data
    Then expected return status code 200

2 - Able to retrieve the Van by using ID
    [Documentation]    To retrieve the van via ID via API
    [Tags]     distadm    9.0    NRSZUANQ-28235
    Given user retrieves token access as ${user_role}
    When user creates van with random data
    Then expected return status code 201
    When user gets van by using id
    Then expected return status code 200
    When user deletes van with created data
    Then expected return status code 200
