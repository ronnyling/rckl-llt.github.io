*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypeDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypePost.py

*** Test Cases ***

1 - Able to update promotion claim type with random data
    [Documentation]    To update kpi type with random data
    [Tags]    sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates kpi type using random data
    Then expected return status code 201
    When user updates kpi type with random data
    Then expected return status code 200
    When user deletes kpi type with valid ID
    Then expected return status code 200

2 - Able to update promotion claim type with fixed data
    [Documentation]    To update kpi type with fixed data
    [Tags]    sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates kpi type using random data
    Then expected return status code 201
    ${vskpitype_details}=   create dictionary
    ...        KPI_TYPE_DESC=KPI Auto Update
    set test variable     &{vskpitype_details}
    When user updates kpi type with fixed data
    Then expected return status code 200
    When user deletes kpi type with valid ID
    Then expected return status code 200
