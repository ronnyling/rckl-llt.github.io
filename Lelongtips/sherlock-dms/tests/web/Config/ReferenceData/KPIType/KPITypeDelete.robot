*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeListPage.py

*** Test Cases ***
1-Able to delete KPI type
    [Documentation]    To ensure user is able to delete created KPI Type
    [Tags]      hqadm     9.2
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user creates KPI type with random data
    Then KPI type created successfully with message 'Record created successfully'
    When user selects KPI type to delete
    Then KPI type deleted successfully with message 'Record deleted'