*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to GET all checklist
    [Documentation]    To retrieve all checklist via API
    [Tags]     hqadm    distadm    9.2    NRSZUANQ-47896
    Given user retrieves token access as ${user_role}
    When user retrieves all checklists
    Then expected return status code 200

2 - Able to GET checklist by valid id
    [Documentation]    To retrieve created checklist using valid id via API
    [Tags]     hqadm    9.2  NRSZUANQ-47897
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user retrieves checklist using valid id
    Then expected return status code 200
    When user deletes created checklist using valid id
    Then expected return status code 200

3 - Unable to GET checklist by invalid id
    [Documentation]    To test unable to retrieve created checklist using invalid id via API
    [Tags]     hqadm    9.2  NRSZUANQ-47898
    Given user retrieves token access as ${user_role}
    When user retrieves checklist using invalid id
    Then expected return status code 404



