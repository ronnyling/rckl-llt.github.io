*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankPost.py

*** Test Cases ***
1 - Able to retrieve all bank
    [Documentation]  To retrieve all bank record via API
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves all bank
    Then expected return status code 200

2 - Able to retrieve bank by using id
    [Documentation]  To retrieve bank by passing in ID via API
    [Tags]    distadm
    Given user retrieves token access as ${user_role}
    When user creates bank using random data
    Then expected return status code 201
    When user retrieves bank by created id
    Then expected return status code 200
