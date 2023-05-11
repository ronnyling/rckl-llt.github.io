*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankDelete.py

*** Test Cases ***
1 - Able to delete created bank
    [Documentation]    Able to delete created bank and return status code 200
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates bank using random data
    Then expected return status code 201
    When user deletes created bank
    Then expected return status code 200
