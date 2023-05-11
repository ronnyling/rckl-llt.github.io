*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/SalesCalendar/SalesCalendarDelete.py

Test Teardown     user deletes created sales calendar as teardown

*** Test Cases ***
1 - Able to create Sales Calendar selecting auto mode with random data
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


2 - Able to create Sales Calendar selecting auto mode with given data
    [Documentation]  To create valid sales calendar with given data via API
    [Tags]    hqadm     9.0
    ${weekend_details}=    create dictionary
    ...    CALENDAR_WEEK_END_DAY=Sunday
    set test variable   &{weekend_details}
    Given user retrieves token access as ${user_role}
    When user creates month with given data
    Then expected return status code 201
    When user creates sales calendar selecting auto mode with given data
    Then expected return status code 201

3 - Able to create Sales Calendar selecting manual mode with random data
    [Documentation]    To create valid sales calendar in manual mode
    [Tags]     hqadm    9.0
    ${weekend_details}=    create dictionary
    ...    CALENDAR_WEEK_END_DAY=Sunday
    set test variable   &{weekend_details}
    Given user retrieves token access as ${user_role}
    When user creates sales calendar selecting manual mode with random data
    Then expected return status code 201

