*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}setup/web/AlertCheck.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Holidays/HolidaysAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Holidays/HolidaysListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Holidays/HolidaysEditPage.py

Test Teardown    user deletes created holiday calendar

*** Test Cases ***
1 - Able to Create Holiday Calender with given data
    [Documentation]    Able to create Holiday  calender by using given data
    [Tags]     hqadm  9.1   TC_01
    ${HCDetails}=    create dictionary
    ...    type=State
    ...    description=HelloWorld1
    ...    date=today
    set test variable     &{HCDetails}
    Given user navigates to menu Configuration | Reference Data | Holidays
    When user creates holiday calendar
    And holiday calendar created successfully with message 'Record created successfully'
    Then user navigates back to listing page

2 - Able to Create Holiday Calender with random data
    [Documentation]    Able to create Holiday calender by using random data
    [Tags]     hqadm  9.1   TC_02
    ${HCDetails}=    create dictionary
    ...    type=random
    ...    description=random
    ...    date=random
    set test variable     &{HCDetails}
    Given user navigates to menu Configuration | Reference Data | Holidays
    When user creates holiday calendar
    And holiday calendar created successfully with message 'Record created successfully'
    Then user navigates back to listing page

