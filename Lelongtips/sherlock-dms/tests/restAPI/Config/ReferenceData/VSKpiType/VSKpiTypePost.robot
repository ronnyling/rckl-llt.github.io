*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/VSKpiType/VSKpiTypePost.py


*** Test Cases ***

1 - Able to create kpi type using random data
    [Documentation]    Able to create kpi type using random data
    [Tags]    sysimp    9.1
    Given user retrieves token access as ${user_role}
    When user creates kpi type using random data
    Then expected return status code 201

2 - Able to create kpi type using given data
    [Documentation]    Able to create kpi type by using given data
    [Tags]   sysimp    9.1
    Given user retrieves token access as ${user_role}
    ${vskpitype_details}=   create dictionary
    ...        KPI_TYPE_DESC=qhequiwehn
    set test variable     &{vskpitype_details}
    When user creates kpi type using given data
    Then expected return status code 201