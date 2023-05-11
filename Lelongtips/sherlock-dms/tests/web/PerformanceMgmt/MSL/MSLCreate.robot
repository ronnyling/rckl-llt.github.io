*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLListPage.py

*** Test Cases ***
1- User able to create MSL with random data
    [Documentation]  To validate user able to create MSL with random data
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user clicks on Cancel button
    And user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'

2- User able to create MSL with fixed data
    [Documentation]  To validate user able to create MSL with random data
    [Tags]   9.2  hqadm
    ${msl_details}=    create dictionary
    ...    desc=AT Fixed MSL Creation
    ...    start_dt=2022-01-01
    ...    end_dt=2022-12-31
    ...    status=Active
    set test variable     &{msl_details}
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using fixed data
    Then MSL created successfully with message 'Record added'
    When user clicks on Cancel button
    And user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'

3- User unable to create facing setup without filling up mandatory fields
    [Documentation]  To validate user unable to create MSL without filling up all mandatory fields and error message shown
    [Tags]   9.1   hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user clicks on Add button
    And user clicks on Save button
    Then user validates the missing mandatory error message

4- User able to assign Product to created MSL
    [Documentation]  To validate user able to assign MSL with Product
    [Tags]   9.2    hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    Then user assigns product to MSL

5- User able to assign Distributor to created MSL
    [Documentation]  To validate user able to assign MSL with Distributor
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    Then user assigns distributor to MSL

6- User able to assign Route to created MSL
    [Documentation]  To validate user able to assign MSL with Route
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    Then user assigns route to MSL

7- User able to assign Customer to created MSL
    [Documentation]  To validate user able to assign MSL with Customer
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    Then user assigns customer to MSL

8- User able to assign Attribute to created MSL
    [Documentation]  To validate user able to assign MSL with Attribute
    [Tags]   9.2  hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    Then user assigns attribute to MSL

