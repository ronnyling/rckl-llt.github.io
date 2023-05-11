*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py

Test Setup        user creates prerequisite for reason 'Return - Bad Stock'
Test Teardown     user deletes reason with created data

*** Test Cases ***
1 - Able to updates Warehouse to Return Reason
    [Documentation]    To update warehouse to Return Reason API
    [Tags]    distadm     9.1    NRSZUANQ-29981    NRSZUANQ-29982
    Given user retrieves token access as ${user_role}
    When user assigns Prime warehouse to reason
    Then expected return status code 201
    When user updates reason warehouse with random data
    Then expected return status code 200

2 - Unable to update Non Prime Warehouse with Prime Warehouse record
    [Documentation]    To update non prime warehouse in prime warehouse field
    [Tags]    distadm     9.1    NRSZUANQ-29986    NRSZUANQ-29987
    Given user retrieves token access as ${user_role}
    When user assigns both warehouse to reason
    Then expected return status code 201
    When user updates reason warehouse with invalid warehouse
    Then expected return status code 404
