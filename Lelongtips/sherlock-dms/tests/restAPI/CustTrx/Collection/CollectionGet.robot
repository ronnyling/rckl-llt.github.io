*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/Collection/CollectionGet.py


Test Setup        run keywords
...               user retrieves token access as distadm
...               AND    user gets distributor by using code 'DistEgg'


*** Test Cases ***
1 - Able to retrieve all Collection
    [Documentation]    Able to retrieve all collection
    [Tags]    distadm    9.2     NRSZUANQ-44091
    Given user retrieves token access as ${user_role}
    When user retrieves all collection
    Then expected return status code 200

2 - Able to retrieve Collection using ID
    [Documentation]    Able to retrieve collection using id
    [Tags]    distadm    9.2     NRSZUANQ-44091
    Given user retrieves token access as ${user_role}
    When user retrieves all collection
    Then expected return status code 200
    When user retrieves collection by random id
    Then expected return status code 200

3 - Unable to GET Collection using HQ access and get 403
    [Documentation]    Unable to retrieve collection using other than distributor user
    [Tags]        hqadm   hquser   sysimp    9.2     NRSZUANQ-44091
    Given user retrieves token access as hqadm
    When user retrieves all collection
    Then expected return status code 403