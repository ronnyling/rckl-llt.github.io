*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/StepsOfCall/StepsOfCallGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/StepsOfCall/StepsOfCallPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/StepsOfCall/StepsOfCallDelete.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionControlDelete.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionControlPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/TransactionControl/TransactionListGet.py

*** Test Cases ***
1 - Able to create an SOC with Salesman as Delivery Rep and Transaction Control as Request with fixed data
    [Documentation]    Able to create asn SOC with Salesman as Delivery Rep and Transaction Control as Request
    [Tags]     sysimp    9.0   NRSZUANQ-6200
    ${SOCDateDetails}=    create dictionary
    ...     StartDate=2040-09-28
    ...     EndDate=2040-09-29
    ${stepsNo}=    create dictionary
    ...     STEPS_NO=1
    set test variable  &{SOCDateDetails}
    set test variable  &{stepsNo}
    Given user retrieves token access as ${user_role}
    When user retrieves the transaction id for Request and code for Delivery Rep
    Then expected return status code 200
    When user assigns the transaction control for all routes
    Then expected return status code 200
    When user creates the transaction control with fixed data
    Then expected return status code 201
    When user creates an soc as created the transaction control with fixed data
    Then expected return status code 201
    When user retrieves the created soc
    Then expected return status code 200
    When user deletes the created soc
    Then expected return status code 200
    When user deletes created transaction control
    Then expected return status code 200

2 - Able to create an SOC with Salesman as Delivery Rep and Transaction Control as Request with random data
    [Documentation]    Able to create asn SOC with Salesman as Delivery Rep and Transaction Control as Request
    [Tags]     sysimp    9.0   NRSZUANQ-6200
    ${stepsNo}=    create dictionary
    ...     STEPS_NO=1
    set test variable  &{stepsNo}
    Given user retrieves token access as ${user_role}
    When user retrieves the transaction id for Request and code for Delivery Rep
    Then expected return status code 200
    When user assigns the transaction control for all routes
    Then expected return status code 200
    When user creates the transaction control with fixed data
    Then expected return status code 201
    When user creates an soc as created the transaction control with random data
    Then expected return status code 201
    When user retrieves the created soc
    Then expected return status code 200
    When user deletes the created soc
    Then expected return status code 200
    When user deletes created transaction control
    Then expected return status code 200