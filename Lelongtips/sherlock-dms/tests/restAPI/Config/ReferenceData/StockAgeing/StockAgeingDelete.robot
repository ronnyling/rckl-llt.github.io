*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingDelete.py

*** Test Cases ***
1 - Able to delete an Aging Period
    [Documentation]    To Delete an Aging Period
    [Tags]     sysimp   hqadm    9.1   NRSZUANQ-25451    BUG-NRSZUANQ-53027
    Given user retrieves token access as ${user_role}
    When user creates valid aging period by random data
    Then expected return status code 201
    When user deletes the created aging period
    Then expected return status code 200

2 - Unable to delete aging period by with invalid ID
    [Documentation]    Unable to delete aging period with invalid ID
    [Tags]     hqadm   sysimp    9.1   NRSZUANQ-25451    BUG-NRSZUANQ-53027
    Given user retrieves token access as ${user_role}
    When user creates valid aging period by random data
    Then expected return status code 201
    When user deletes the invalid aging period
    Then expected return status code 400
    When user deletes the created aging period
    Then expected return status code 200
