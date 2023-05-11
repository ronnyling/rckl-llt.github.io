*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeListPage.py

*** Test Cases ***
1 - Able to Create KPI Type using random data
    [Documentation]    Able to create KPI type using random data
    [Tags]     hqadm    9.2
    [Teardown]    run keywords
    ...    user selects KPI type to delete
    ...    AND     KPI type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user creates KPI type with random data
    Then KPI type created successfully with message 'Record created successfully'

2 - Validate error messages when KPI type fields are left empty
    [Documentation]    Unable to create a KPI type with invalid data
    [Tags]     hqadm    9.2
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user clicks on Add button
    And user clicks on Save button
    Then validate error message on empty fields