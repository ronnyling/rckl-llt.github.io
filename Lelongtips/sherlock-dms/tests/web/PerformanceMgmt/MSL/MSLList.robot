*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLListPage.py

*** Test Cases ***
1- Verify Hq admin able to view all managing buttons
    [Documentation]  To validate user able to view all add/edit/delete buttons
    [Tags]   9.2   hqadm 
    Given user navigates to menu Performance Management | Must Sell List
    Then user validates all managing buttons present and visible

2- Distributor only have view access but not managing permission
    [Documentation]  To validate user have view access and not able to see add/edit/delete buttons
    [Tags]   9.2   distadm   
    Given user navigates to menu Performance Management | Must Sell List
    Then user validates all managing buttons absent and hidden

3- User able to search MSL
    [Documentation]  To validate user able to filter MSL using filter in listing
    [Tags]   9.2   hqadm
    ${msl_details}=    create dictionary
    ...    desc=MSL SCH DESC
    ...    start_dt=2022-02-02
    ...    end_dt=2022-02-03
    ...    status=Active
    set test variable     &{msl_details}
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using fixed data
    Then MSL created successfully with message 'Record created successfully'
    When user searches created MSL in listing page
    And user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'

4- User able to filter MSL
    [Documentation]  To validate user able to filter MSL using filter in listing
    [Tags]   9.2   hqadm
    ${msl_details}=    create dictionary
    ...    desc=MSL FLT DESC
    ...    start_dt=2022-02-02
    ...    end_dt=2022-02-03
    ...    status=Active
    set test variable     &{msl_details}
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using fixed data
    Then MSL created successfully with message 'Record created successfully'
    When user searches filters MSL in listing page
    And user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'