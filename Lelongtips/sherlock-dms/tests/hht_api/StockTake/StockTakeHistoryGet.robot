*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/StockTake/StockTakeHistoryGet.py


*** Test Cases ***
1 - Able to retrieve stock take history
    [Documentation]    Able to retrieve stock take history
    [Tags]    salesperson    9.2    NRSZUANQ-52270
    Given user retrieves token access as ${user_role}
    When user retrieves stock take history
    Then expected return status code 200