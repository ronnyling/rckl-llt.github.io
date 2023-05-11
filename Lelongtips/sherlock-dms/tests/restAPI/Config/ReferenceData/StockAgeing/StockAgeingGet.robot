*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingDelete.py


*** Test Cases ***
1 - Able to get all Aging Period
    [Documentation]    To retrieve all valid aging period
    [Tags]     hqadm   sysimp   9.1   NRSZUANQ-25451
    Given user retrieves token access as ${user_role}
    When user retrieves all aging period
    Then expected return status code 200

2 - Able to get Aging Period by ID
    [Documentation]    To retrieve an aging period by ID
    [Tags]     hqadm   sysimp    9.1   NRSZUANQ-25451
    Given user retrieves token access as ${user_role}
    When user creates valid aging period by random data
    Then expected return status code 201
    When user retrieves the created aging period by ID
