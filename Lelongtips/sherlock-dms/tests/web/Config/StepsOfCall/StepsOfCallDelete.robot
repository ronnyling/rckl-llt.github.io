*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library  ${EXECDIR}${/}resources/web/Config/StepsOfCall/StepsOfCallAddPage.py
Library  ${EXECDIR}${/}resources/web/Config/StepsOfCall/StepsOfCallListingPage.py
Library  ${EXECDIR}${/}resources/web/Config/StepsOfCall/StepsOfCallDeletePage.py
Library  ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionControlDelete.py
Library  ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionControlPost.py
Library  ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionListGet.py
Library  ${EXECDIR}${/}resources/web/Config/StepsOfCall/StepsOfCallAddPage.py

*** Test Cases ***
1 - Able to Delete SOC with Delivery Rep as Salesperson with ramdom data
    [Documentation]    Able to Delete SOC with Delivery Rep as Salesperson
    [Tags]     sysimp  9.0
    ${SOCDateDetails}=    create dictionary
    ...     StartDate=2020-09-29
    ...     EndDate=2020-09-30
    set test variable  &{SOCDateDetails}
    Given user retrieves token access as ${user_role}
    When user retrieves the transaction id for Request and code for Delivery Rep
    Then expected return status code 200
    When user assigns the transaction control for all routes
    Then expected return status code 200
    When user creates the transaction control with fixed data
    Then expected return status code 201
    When user navigates to menu Configuration | Steps of Call
    Then user fills soc general info using created transaction
    When user fills and saves soc activity assignment using created transaction
    Then The steps of call is created successfully with message 'Record created successfully'
    Then user deletes the created soc
    And The steps of call is deleted successfully with message 'Record deleted'
    When user deletes created transaction control
    Then expected return status code 200



