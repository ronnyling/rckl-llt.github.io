*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionControlDelete.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionControlPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionListGet.py

*** Test Cases ***

1 - Able to create Transaction Control with Opeartion Type as Van Sales and Transaction Control as Request
    [Documentation]    Able to create Transaction Control with Opeartion Type as Van Sales and Transaction Control as Request
    [Tags]     sysimp    9.0   NRSZUANQ-6200
    ${TransactionDetails}=    create dictionary
    ...     PRINT_COPY=${3}
    ...     MAX_PRINT_COPY=${10}
    set test variable  &{TransactionDetails}
    Given user retrieves token access as ${user_role}
    When user retrieves the transaction id for Request and code for Van Sales
    Then expected return status code 200
    When user assigns the transaction control for all routes
    Then expected return status code 200
    When user creates the transaction control with fixed data
    Then expected return status code 201
    When user deletes created transaction control
    Then expected return status code 200


