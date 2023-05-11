*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py

Test Setup        user retrieves reason type 'Return - Bad Stock'

*** Test Cases ***
1 - Able to delete Reason with created data
    [Documentation]    To delete valid reason with created data via API
    [Tags]    hqadm    hquser     9.0
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 201
    When user deletes reason with created data
    Then expected return status code 200

2- Unable to delete the invalid/non-existing reason data ID
    [Documentation]  This test is to try deleting the invalid reason ID
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user deletes reason with created data
    ...    AND expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 201
    When user deletes reason with invalid data
    Then expected return status code 404

