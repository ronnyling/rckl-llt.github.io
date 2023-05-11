*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ExecutionResult/ChecklistResult/ChecklistResultGet.py

*** Test Cases ***
1 - Able to GET all merchandising checklist result
    [Documentation]  Able to retrieve all merchandising checklist result
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all checklist results
    Then expected return status code 200

2 - Able to GET all merchandising checklist result based on status
    [Documentation]  Able to retrieve all merchandising checklist result based on status
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves checklist with status Cancelled
    Then expected return status code 200
    When user retrieves checklist with status Confirmed
    Then expected return status code 200

3 - Able to GET merchandising checklist result by id
    [Documentation]  Able to retrieve merchandising checklist result by id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all checklist results
    Then expected return status code 200
    When user retrieves checklist result by id
    Then expected return status code 200

4 - Able to GET activity details for merchandising checklist result
    [Documentation]  Able to retrieve activity details based on merchandising checklist id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user retrieves all checklist results
    Then expected return status code 200
    When user retrieves checklist result by id
    Then expected return status code 200
    When user retrieves checklist activity details
    Then expected return status code 200


