*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supervisor/Checklist/ChecklistDelete.py

*** Test Cases ***
1 - Able to PUT new checklist
    [Documentation]    To test able to update checklist via API
    [Tags]     hqadm    9.2  NRSZUANQ-47900
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user updates created checklist with random data
    Then expected return status code 200
    When user deletes created checklist using valid id
    Then expected return status code 200

2 - Unable to PUT existing checklist using distributor access
    [Documentation]    To test unable to update checklist using distributor token
    [Tags]     distadm    9.2  NRSZUANQ-47904
    Given user retrieves token access as hqadm
    When user creates checklist with random data
    Then expected return status code 201
    When user retrieves token access as distadm
    And user updates created checklist with random data
    Then expected return status code 403

3 - Unable to PUT checklist with new checklist type
    [Documentation]    To test unable to update checklist with new checklist type via API
    [Tags]     hqadm    9.2  NRSZUANQ-47911
    ${checklist_details}=   create dictionary
    ...    CHECKLIST_TYPE=R
    ${new_checklist_details}=   create dictionary
    ...    CHECKLIST_TYPE=S
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user updates created checklist with fixed data
    Then expected return status code 400
    When user deletes created checklist using valid id
    Then expected return status code 200

4 - Unable to PUT checklist with new checklist code
    [Documentation]    To test unable to update checklist with new code via API
    [Tags]     hqadm    9.2  NRSZUANQ-47912
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user updates created checklist with code data
    Then expected return status code 400
    When user deletes created checklist using valid id
    Then expected return status code 200

5 - Unable to PUT checklist with new start date if initial start date has passed
    [Documentation]    To test unable to update checklist with new start date when initial start date has passed
    [Tags]     hqadm    9.2    NRSZUANQ-47913
    ${new_checklist_details}=   create dictionary
    ...    START_DT=2022-02-28
    ...    END_DT=2023-02-28
    Given user retrieves token access as ${user_role}
    When user updates created checklist with past start date data
    Then expected return status code 400

6 - Unable to PUT checklist item if start date has passed
    [Documentation]    To test unable to update checklist when start date has passed
    [Tags]     hqadm    9.2    NRSZUANQ-47914
    ${new_checklist_details}=   create dictionary
    ...    CHECKLIST_ITEM_DESC=NEWLY UPDATED DESC
    Given user retrieves token access as ${user_role}
    When user updates created checklist with past start date data
    Then expected return status code 400

7 - Able to PUT checklist item with new end date if initial end date has passed
    [Documentation]    To test able to update checklist with new end date when initial end date has passed
    [Tags]     hqadm    9.2     NRSZUANQ-47915
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user updates created checklist with random data
    Then expected return status code 200
    When user deletes created checklist using valid id
    Then expected return status code 200

8 - Unable to PUT checklist without checklist item
    [Documentation]    To test unable to update checklist without checklist item
    [Tags]     hqadm    9.2  NRSZUANQ-47908
    ${new_checklist_details}=   create dictionary
    ...    CHECKLIST_ITEM=${EMPTY}
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user updates created checklist with fixed data
    Then expected return status code 400
    When user deletes created checklist using valid id
    Then expected return status code 200

9 - Unable to PUT checklist without workplan item
    [Documentation]    To test unable to update checklist without workplan item
    [Tags]     hqadm    9.2  NRSZUANQ-48475
    ${new_checklist_details}=   create dictionary
    ...    WORK_PLAN_ITEM=${EMPTY}
    Given user retrieves token access as ${user_role}
    When user creates checklist with random data
    Then expected return status code 201
    When user updates created checklist with fixed data
    Then expected return status code 400
    When user deletes created checklist using valid id
    Then expected return status code 200


