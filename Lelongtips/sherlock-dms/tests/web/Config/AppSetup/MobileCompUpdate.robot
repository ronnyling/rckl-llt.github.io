*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/MobileCompEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Able to update mobile comms using random data
    [Documentation]    Able to update inventory using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Mobile Comms tab
    Then user updates mobile comm using random data
    And Mobile Comms updated successfully with message 'Record updated successfully'

2 - Able to update mobile comms using fixed data
    [Documentation]    Able to update inventory using given data
    [Tags]    sysimp    9.1
    ${MobileCommDetails}=    create dictionary
    ...    HHT_Validate_Device Hardware ID=${False}
    ...    Check_Profile_Match=${True}
    ...    Check_SafetyNet_Error=${False}
    ...    API_Key=Abcd1234
    ...    Validation_Timeout_(Days)=7
    ...    JWS_Timeout_(Hours)=10
    set test variable    &{MobileCommDetails}
    When user navigates to menu Configuration | Application Setup
    And user navigates to Mobile Comms tab
    Then user updates mobile comm using fixed data
    And Mobile Comms updated successfully with message 'Record updated successfully'