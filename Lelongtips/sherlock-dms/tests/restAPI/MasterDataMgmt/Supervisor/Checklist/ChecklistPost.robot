*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to POST new checklist
    [Documentation]    To test able to create new checklist via API
    [Tags]     hqadm    9.2  NRSZUANQ-47899
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user deletes created checklist using valid id
    Then expected return status code 200

2 - Unable to POST new checklist using distributor access
    [Documentation]    To test unable to create checklist using distributor token
    [Tags]     distadm    9.2  NRSZUANQ-47903
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 403

3 - Unable to POST checklist with invalid checklist type
    [Documentation]    To test unable to create checklist with invalid type via API
    [Tags]     hqadm    9.2  NRSZUANQ-47910
    ${checklist_details}=   create dictionary
    ...    CHECKLIST_TYPE=SALES
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 400

4 - Unable to POST checklist without checklist item
    [Documentation]    To test unable to create checklist without checklist item
    [Tags]     hqadm    9.2  NRSZUANQ-47907
    ${checklist_details}=   create dictionary
    ...    CHECKLIST_ITEM=${EMPTY}
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 400

5 - Unable to POST checklist without workplan item
    [Documentation]    To test unable to create checklist without workplan item
    [Tags]     hqadm    9.2  NRSZUANQ-48474
    ${checklist_details}=   create dictionary
    ...    WORK_PLAN_ITEM=${EMPTY}
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 400
