*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Holidays/HolidaysPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Holidays/HolidaysDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Holidays/HolidaysGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Holidays/HolidaysPut.py
Library           DateTime
Library           String

*** Test Cases ***
1 - Able to put Holiday Calendar with given data
    [Documentation]  To get valid holiday calendar with given data via API
    [Tags]    hqadm     9.0
    ${RANUSER}=    Generate Random String  10  [LETTERS]
    ${HC_details}=    create dictionary
    ...    HOLIDAY_TYPE=State
    ...    HOLIDAY_DESC=${RANUSER}
    set test variable   &{HC_details}
    Given user retrieves token access as ${user_role}
    When user creates holiday calendar with given data
    Then expected return status code 200
    When user gets holiday calendar with created data
    Then expected return status code 200
    When user updates holiday calendar with created data
    Then expected return status code 200
    When user deletes holiday calendar with created data
    Then expected return status code 200

2 - Able to put Holiday Calendar with random data
    [Documentation]  To get valid holiday calendar with random data via API
    [Tags]    hqadm     9.0    
    Given user retrieves token access as ${user_role}
    When user creates holiday calendar with random data
    Then expected return status code 200
    When user gets holiday calendar with created data
    Then expected return status code 200
    When user updates holiday calendar with created data
    Then expected return status code 200
    When user deletes holiday calendar with created data
    Then expected return status code 200