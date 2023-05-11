*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py

Test Setup        user creates prerequisite for reason 'Return - Bad Stock'
Test Teardown     user deletes reason with created data

*** Test Cases ***
1 - Able to assign Warehouse to Return Reason
    [Documentation]    To assign warehouse to Return Reason API
    [Tags]    distadm     9.1   NRSZUANQ-29979    NRSZUANQ-29980
    Given user retrieves token access as ${user_role}
    When user assigns Prime warehouse to reason
    Then expected return status code 201

2 - Unable to POST Warehouse with HQ access
    [Documentation]    Unable to assign warehouse using HQ access via API
    [Tags]    hqadm   hquser     9.1   NRSZUANQ-29990
    Given user retrieves token access as hqadm
    When user assigns Prime warehouse to reason
    Then expected return status code 403
