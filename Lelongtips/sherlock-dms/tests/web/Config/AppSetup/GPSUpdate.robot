*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/GPSEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

#not applicable to sysimp
*** Test Cases ***
1 - Able to update GPS using random data
    [Documentation]    Able to update GPS using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to GPS tab
    Then user updates GPS using random data
    And GPS updated successfully with message 'Record updated successfully'

2 - Able to update GPS using fixed data
    [Documentation]    Able to update GPS using fixed data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to GPS tab
    ${GPSDetails}=    create dictionary
    ...    Enable_GPS_Restriction=${False}
    ...    Customer_GPS_Variance=${True}
    ...    GPS_Variance_Distance_(Metres)=${500}
    ...    On_GPS_During_Visit=${True}
    set test variable    &{GPSDetails}
    Then user updates GPS using fixed data
    And GPS updated successfully with message 'Record updated successfully'
