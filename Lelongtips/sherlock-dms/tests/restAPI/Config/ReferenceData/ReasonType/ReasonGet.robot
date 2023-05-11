*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py

Test Setup        user retrieves reason type 'Return - Bad Stock'
*** Test Cases ***

1- Able to retrieve all reason data for the given distributor provided
    [Documentation]  This test is to retrieve all reason data via API
    [Tags]    hqadm     9.2
    Given user retrieves token access as ${user_role}
    When user retrieves all reasons
    Then expected return status code 200

2- Unable to retrieve details of the invalid/non-existing reason data ID
    [Documentation]  This test is to try retrieving the details of invalid reason data ID
    [Tags]    hqadm     9.2
    [Teardown]    run keywords
    ...    user deletes reason with created data
    ...    AND expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 201
    When user retrieves reason using invalid id
    Then expected return status code 404

3- Able to retrieve selected reason data for the given distributor provided
    [Documentation]  This test is to retrieve selected reason data via API
    [Tags]    hqadm     9.2
    [Teardown]    run keywords
    ...    user deletes reason with created data
    ...    AND expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 201
    When user retrieves reason using valid id
    Then expected return status code 200


