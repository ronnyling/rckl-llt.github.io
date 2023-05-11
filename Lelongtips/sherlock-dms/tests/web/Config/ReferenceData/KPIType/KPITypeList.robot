*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeListPage.py

*** Test Cases ***
1-Able to search created KPI type
    [Documentation]    To test user is able to search created KPI type
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects KPI type to delete
    ...    AND     KPI type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user creates KPI type with random data
    Then message type created successfully with message 'Record created successfully'
    When user searches created KPI type
    Then record display in listing successfully

2-Able to filter created KPI type
    [Documentation]       To test user is able to filter created KPI type
    [Tags]      hqadm     9.2
    [Teardown]    run keywords
    ...    user selects KPI type to delete
    ...    AND     KPI type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user creates KPI type with random data
    Then KPI type created successfully with message 'Record created successfully'
    When user filters created KPI type
    Then record display in listing successfully