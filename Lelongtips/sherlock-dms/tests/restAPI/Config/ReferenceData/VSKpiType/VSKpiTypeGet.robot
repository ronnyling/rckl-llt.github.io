*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypeGet.py

*** Test Cases ***
1 - Able to retrieve all kpi type
    [Documentation]    Able to retrieve allkpi type
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user retrieves all kpi type
    Then expected return status code 200