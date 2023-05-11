*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/SalesCalendar/SalesCalendarAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/SalesCalendar/SalesCalendarListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/SalesCalendar/SalesCalendarEditPage.py

Test Teardown   run keywords
...    user deletes created sales calendar
...    AND     sales calendar deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1 - Able to update Sales Calendar with given data
    [Documentation]    Able to update Sales calendar by using given data
    [Tags]     hqadm    9.0
    ${SCDetails}=    create dictionary
    ...    calendarName=SC2025-26
    ...    startDate=Sep 1, 2020
    ...    endDate=Aug 31, 2021
    set test variable     &{SCDetails}
    ${QuarterDetails}=    create dictionary
    ...    quarterName=Q1
    set test variable     &{QuarterDetails}
    Given user navigates to menu Configuration | Reference Data | Sales Calendar
    When user creates sales calendar with given data
    Then sales calendar created successfully with message 'Record created successfully'
    Then user updates created sales calendar with given data
    And sales calendar updated successfully with message 'Record updated successfully'
