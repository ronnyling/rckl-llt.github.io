*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistDelete.py


*** Test Cases ***
1 - Able to DELETE merchandising checklist by id
    [Documentation]  Able to delete merchandising checklist by id
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user adds merchandising checklist using random data
    Then expected return status code 201
    When user deletes merchandising checklist
    Then expected return status code 200