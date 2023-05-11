*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/SalesCalendar/SalesCalendarAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/SalesCalendar/SalesCalendarListPage.py

Test Teardown   run keywords
...    user deletes created sales calendar
...    AND     sales calendar deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1 - Able to delete Sales Calendar
    [Documentation]    Able to create Sales Calendar  by using random data
    [Tags]     hqadm    9.0
    ${SCDetails}=    create dictionary
    ...    calendarName=random
    ...    startDate=random
    ...    endDate=random
    set test variable     &{SCDetails}
    Given user navigates to menu Configuration | Reference Data | Sales Calendar
    When user creates sales calendar with random data
    Then sales calendar created successfully with message 'Record created successfully'
