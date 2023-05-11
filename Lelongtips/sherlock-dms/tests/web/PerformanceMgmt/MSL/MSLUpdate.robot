*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLListPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLUpdatePage.py

*** Test Cases ***
1- User able to update created MSL with random data
    [Documentation]  To validate user able to update MSL with random data
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    And user clicks on Cancel button
    When user validate created MSL is listed in the table and select to edit
    And user updates MSL using random data
    Then MSL updated successfully with message 'Record updated'
    When user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'

2- User able to update created MSL with fixed data
    [Documentation]  To validate user able to update MSL with fixed data
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    And user clicks on Cancel button
    When user validate created MSL is listed in the table and select to edit
    ${msl_details}=    create dictionary
    ...    desc=Update MSL Perf Mgm
    ...    start_dt=2023-01-01
    ...    end_dt=2023-12-31
    ...    status=Inactive
    set test variable     &{msl_details}
    And user updates MSL using fixed data
    Then MSL updated successfully with message 'Record updated'
    When user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'

