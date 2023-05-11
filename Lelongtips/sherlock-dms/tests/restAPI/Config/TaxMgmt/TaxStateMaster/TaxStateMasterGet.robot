*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStateMaster/TaxStateMasterGet.py

*** Test Cases ***
1 - Able to get all tax state master
    [Documentation]    Able to retrieve all tax state master
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user retrieves all tax state master
    Then expected return status code 200

2 - Able to filter tax state master by code
    [Documentation]    Able to retrieve tax state master by code
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user retrieves tax state master by code 333
    Then expected return status code 200
