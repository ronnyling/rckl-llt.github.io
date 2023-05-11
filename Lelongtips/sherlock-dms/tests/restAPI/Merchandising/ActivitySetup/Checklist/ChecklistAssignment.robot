*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistAssignment.py
Library           ${EXECDIR}${/}resources/restAPI/Merchandising/ActivitySetup/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to POST merchandising checklist with random data
    [Documentation]  Able to add merchandising checklist with random data
    [Tags]    hqadm    9.2
    Given user retrieves token access as hqadm
    When user adds merchandising checklist using random data
    Then expected return status code 201
    When user assigns checklist to Level:Sales Office, Node:Eggy Global Company, Dist:DistEgg
    And user create customer assignment for checklist to Customer:CT0000001549
    Then expected return status code 201
    When user deletes merchandising checklist
    Then expected return status code 200
