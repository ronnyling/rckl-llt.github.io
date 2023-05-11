*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarDelete.py

*** Test Cases ***
1 - Able to delete created Sales Calendar
    [Documentation]    To create valid sales calendar with random generate data
    [Tags]     hqadm    9.0
    ${weekend_details}=    create dictionary
    ...    CALENDAR_WEEK_END_DAY=Sunday
    set test variable   &{weekend_details}
    Given user retrieves token access as ${user_role}
    When user creates month with random data
    Then expected return status code 201
    When user creates sales calendar selecting auto mode with random data
    Then expected return status code 201
    When user deletes sales calendar with created data
    Then expected return status code 200
