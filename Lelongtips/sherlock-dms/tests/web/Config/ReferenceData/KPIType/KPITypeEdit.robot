*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/KPIType/KPITypeEditPage.py

*** Test Cases ***
1 - Able to edit an existing KPI type with random data
    [Documentation]    Able to edit a KPI type with random data
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects KPI type to delete
    ...    AND     KPI type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user creates KPI type with random data
    Then KPI type created successfully with message 'Record created successfully'
    When user selects KPI type to edit
    And user edits KPI type with random data
    Then KPI type edited successfully with message 'Record updated successfully'

2 - Able to edit an existing KPI type with fixed data
    [Documentation]    Able to edit a KPI type with fixed data
    [Tags]     hqadm     9.2
    [Teardown]    run keywords
    ...    user selects KPI type to delete
    ...    AND     KPI type deleted successfully with message 'Record deleted'
    ...    AND     user logouts and closes browser
    ${new_kpi_details}=    create dictionary
    ...    kpi_desc=UPDT NEW DESC KPI TYPE
    set test variable     &{new_kpi_details}
    Given user navigates to menu Configuration | Reference Data | KPI Type
    When user creates KPI type with random data
    Then KPI type created successfully with message 'Record created successfully'
    When user selects KPI type to edit
    And user edits KPI type with random data
    Then KPI type edited successfully with message 'Record updated successfully'