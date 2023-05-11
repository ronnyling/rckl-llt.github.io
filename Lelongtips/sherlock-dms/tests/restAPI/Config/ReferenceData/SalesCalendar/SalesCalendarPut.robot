*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarGet.py

Test Teardown     user deletes created sales calendar as teardown

*** Test Cases ***

1- Able to update created Sales Calendar using given data
    [Documentation]  To update already created valid sales calendar
    [Tags]    hqadm     9.0
    ${update_month_quarter}=    create dictionary
    ...    CALENDAR_MONTH_QUARTER=Q1
    ...    CALENDAR_MONTH_HALF_YEARLY=H1
    set test variable   &{update_month_quarter}
    ${weekend_details}=    create dictionary
    ...    CALENDAR_WEEK_END_DAY=Sunday
    set test variable   &{weekend_details}
    Given user retrieves token access as ${user_role}
    When user creates sales calendar selecting manual mode with random data
    Then expected return status code 201
    When user gets calendar by using id
    Then expected return status code 200
    When user updates sales calendar with given data
    Then expected return status code 200