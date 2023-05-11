*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/ServiceMaster/ServiceMasterGet.py

*** Test Cases ***
1 - Able to retrieve created service master
    [Documentation]    Able to retrieve created service master and return status code 200
    [Tags]     hqadm    distadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all service master
    Then expected return status code 200

2 - Unable to retrieve service master with invalid id
    [Documentation]    Able to retrieve created service master and return status code 200
    [Tags]     hqadm    distadm    9.0
    Given user retrieves token access as ${user_role}
    set test variable   ${sac_id}    98501D2E:3ECBF4F3-6B9F-4423-8A7F-4F43A2A99887
    When user retrieves invalid service master
    Then expected return status code 404

3 - Unable to retrieve service master with invalid id
    [Documentation]    Able to retrieve created service master and return status code 200
    [Tags]     hqadm    distadm    9.0
    Given user retrieves token access as ${user_role}
    When user get service master by code   ShamServiceCode
    Then expected return status code 200