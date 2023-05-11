*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxStateMaster/TaxStateMasterPost.py

*** Test Cases ***
1 - Able to create tax state master with random data
    [Documentation]    Able to create tax state master with random generated data
    [Tags]     distadm    9.1
    Given user retrieves token access as distadm
    When user creates tax state master with random data
    Then expected return status code 200
