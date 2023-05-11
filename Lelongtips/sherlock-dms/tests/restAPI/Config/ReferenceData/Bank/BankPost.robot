*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankPost.py

*** Test Cases ***
1 - Able to create bank using random data
    [Documentation]    Able to create bank and return status code 201
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates bank using random data
    Then expected return status code 201