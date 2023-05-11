*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistGet.py


*** Test Cases ***
1 - Able to GET merchandising checklist
    [Documentation]  Able to retrieve merchandising checklist
    [Tags]    hqadm1    9.2
    Given user retrieves token access as hqadm
    When user retrieves all checklist
    Then expected return status code 200

2 - Able to GET merchandising checklist by id
    [Documentation]  Able to retrieve checklist by code
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user randoms a checklist from list
    And user retrieves checklist by id
    Then expected return status code 200