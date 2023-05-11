*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonPut.py
Test Setup        user retrieves reason type 'Return - Bad Stock'

*** Test Cases ***

1- Able to update reason data with newly created agent ID
    [Documentation]    This test is to update reason data with newly created ship to Id via API     sysimp
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes reason with created data
    ...    AND expected return status code 200
    ${reason_details}=    create dictionary
    ...    REASON_DESC=Test123Desc
    set test variable   &{reason_details}
    Given user retrieves token access as ${user_role}
    When user creates reason with fixed data
    Then expected return status code 201
    When user updates reason with valid id
    Then expected return status code 200

2- Unable to update details of the invalid/non-existing reason data ID
    [Documentation]  This test is to try updating the details of invalid reason data ID
    [Tags]    hqadm    9.2
    [Teardown]    run keywords
    ...    user deletes reason with created data
    ...    AND expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates reason with fixed data
    Then expected return status code 201
    When user updates reason with invalid id
    Then expected return status code 404
