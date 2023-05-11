*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypeDelete.py

*** Test Cases ***
1 - Unable to delete claim type by with invalid ID
    [Documentation]    Unable to delete claim type with invalid ID
    [Tags]     hqadm   9.0
    Given user retrieves token access as ${user_role}
    When user creates valid claim type with random data
    Then expected return status code 201
    When user deletes claim type with invalid ID
    Then expected return status code 404
    When user deletes claim type with created data
