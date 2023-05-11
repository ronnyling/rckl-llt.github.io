*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarDelete.py


*** Test Cases ***
1 - Able to retrieve all sales calendar
    [Documentation]    Able to retrieve all calendar details
    [Tags]    hqadm     9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all calendar data
    Then expected return either status code 200 or status code 204

2 - Able to retrieve Sales Calendar by using id
    [Documentation]    Able to retrieve Sales Calendar by using id
    [Tags]    hqadm    9.0
    ${weekend_details}=    create dictionary
    ...    CALENDAR_WEEK_END_DAY=Sunday
    set test variable   &{weekend_details}
    Given user retrieves token access as ${user_role}
    When user creates month with random data
    Then expected return status code 201
    When user creates sales calendar selecting auto mode with random data
    Then expected return status code 201
    When user gets calendar by using id
    Then expected return status code 200
    When user deletes sales calendar with created data
    Then expected return status code 200
