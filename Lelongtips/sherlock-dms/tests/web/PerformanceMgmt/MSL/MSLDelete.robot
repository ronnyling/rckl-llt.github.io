*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLListPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/MSL/MSLUpdatePage.py
*** Test Cases ***
1- User able to delete created MSL
    [Documentation]  To validate user able to delete created MSL
    [Tags]   9.2   hqadm
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    And user clicks on Cancel button
    When user validate created MSL is listed in the table and select to delete
    Then MSL deleted successfully with message 'Record deleted'

2- User able to delete MSL product assignment
    [Documentation]  To validate user able to delete MSL product assignment
    [Tags]   9.2    hqadm
    [Teardown]  run keywords
    ...    user validate created MSL is listed in the table and select to delete
    ...    AND    MSL deleted successfully with message 'Record deleted'
    ...    AND    user logouts and closes browser
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    And user assigns product to MSL
    Then user deletes MSL product assignment

3- User able to delete MSL distributor assignment
    [Documentation]  To validate user able to delete MSL distributor assignment
    [Tags]   9.2    hqadm
    [Teardown]  run keywords
    ...    user validate created MSL is listed in the table and select to delete
    ...    AND    MSL deleted successfully with message 'Record deleted'
    ...    AND    user logouts and closes browser
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    And user assigns distributor to MSL
    Then user deletes MSL distributor assignment

4- User able to delete MSL route assignment
    [Documentation]  To validate user able to delete MSL route assignment
    [Tags]   9.2    hqadm
    [Teardown]  run keywords
    ...    user validate created MSL is listed in the table and select to delete
    ...    AND    MSL deleted successfully with message 'Record deleted'
    ...    AND    user logouts and closes browser
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    And user assigns route to MSL
    Then user deletes MSL route assignment


5- User able to delete MSL customer assignment
    [Documentation]  To validate user able delete MSL customer assignment
    [Tags]   9.2    hqadm
    [Teardown]  run keywords
    ...    user validate created MSL is listed in the table and select to delete
    ...    AND    MSL deleted successfully with message 'Record deleted'
    ...    AND    user logouts and closes browser
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    And user assigns customer to MSL
    Then user deletes MSL customer assignment

6- User able to delete MSL attribute assignment
    [Documentation]  To validate user able to delete MSL attribute assignment
    [Tags]   9.2    hqadm
    [Teardown]  run keywords
    ...    user validate created MSL is listed in the table and select to delete
    ...    AND    MSL deleted successfully with message 'Record deleted'
    ...    AND    user logouts and closes browser
    Given user navigates to menu Performance Management | Must Sell List
    When user creates MSL using random data
    Then MSL created successfully with message 'Record added'
    When user navigate to Assignment tab
    And user assigns attribute to MSL
    Then user deletes MSL attribute assignment




