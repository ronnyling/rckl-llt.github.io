*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Whatapp/WhatappGet.py

*** Test Cases ***
1 - Able to retrieved the whatapp list of customer
    [Documentation]    To retrieved the whatapp list of customer
    [Tags]     distadm    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves whatapp list of Customer
    Then expected return status code 200

2 - Able to retrieved the whatapp list of salesperson
    [Documentation]    To retrieved the whatapp list of salesperson
    [Tags]     distadm    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves whatapp list of Salesperson
    Then expected return status code 200

3 - Unable to retrieved the whatapp list of invalid
    [Documentation]    To retrieved the whatapp list of invalid
    [Tags]     distadm    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves whatapp list of invalid
    Then expected return status code 404


