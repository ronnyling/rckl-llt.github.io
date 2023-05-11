*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py

Test Setup        user creates prerequisite for reason 'Return - Bad Stock'
Test Teardown     user deletes reason with created data

*** Test Cases ***
1 - Able to retrieve Warehouse which assigned to Return Reason
    [Documentation]    To retrieve warehouse which assign to Return Reason API
    [Tags]    distadm     9.1   NRSZUANQ-29983
    Given user retrieves token access as ${user_role}
    When user assigns Prime warehouse to reason
    Then expected return status code 201
    When user gets reason warehouse by using id
    Then expected return status code 200
