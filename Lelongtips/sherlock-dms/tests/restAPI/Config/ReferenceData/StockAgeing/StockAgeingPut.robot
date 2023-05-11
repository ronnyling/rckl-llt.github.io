*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/StockAgeing/StockAgeingDelete.py


*** Test Cases ***
1 - Able to update aging period via API
    [Documentation]    To update a created aging period
    [Tags]     hqadm    sysimp    9.0     NRSZUANQ-25451    BUG-NRSZUANQ-53027
    ${aging_period_details_put}=    create dictionary
    ...    PERIOD_DESC=Period Description by given data PUT
    set test variable   &{aging_period_details_put}
    Given user retrieves token access as ${user_role}
    When user creates valid aging period by random data
    Then expected return status code 201
    When user retrieves the created aging period by ID
    Then expected return status code 200
    When user updates the created aging period
    Then expected return status code 200
    When user deletes the created aging period
    Then expected return status code 200


