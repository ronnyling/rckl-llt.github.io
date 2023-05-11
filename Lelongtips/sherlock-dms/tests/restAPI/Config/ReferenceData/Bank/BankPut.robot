*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Bank/BankPut.py
Library           Collections


*** Test Cases ***
1 - Able to update bank via API
    [Documentation]    To to update created bank and delete
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates bank using random data
    Then expected return status code 201
    When user retrieves bank by created id
    Then expected return status code 200
     ${bank_update_details} =    create dictionary
    ...    BANK_DESC=edited bank
    When user update created bank
    Then expected return status code 200
    When user deletes created bank
    Then expected return status code 200
