*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingDelete.py
Library           Collections

*** Test Cases ***

1 - Able to create Aging Period with random data
    [Documentation]    To create valid Aging Period with random generate data
    [Tags]     sysimp   hqadm    9.1   NRSZUANQ-25451    BUG-NRSZUANQ-53027
    Given user retrieves token access as ${user_role}
    When user creates valid aging period by random data
    Then expected return status code 201
    When user retrieves the created aging period by ID
    Then expected return status code 200
    When user deletes the created aging period
    Then expected return status code 200

2 - Able to create an Aging Period with given data
    [Documentation]    To create an Aging Period with given data
    [Tags]     sysimp   hqadm    9.1    NRSZUANQ-25451    BUG-NRSZUANQ-53027
    ${aging_period_details}=    create dictionary
    ...    PERIOD_DESC=Period Description by given data
    set test variable   &{aging_period_details}
    Given user retrieves token access as ${user_role}
    When user creates valid aging period by random data
    Then expected return status code 201
    When user deletes the created aging period
    Then expected return status code 200

