*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletEditPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletDeletePage.py

*** Test Cases ***
1 - Able to edit ewallet data with fixed data
    [Tags]   sysimp    9.0
    ${EW_details}=   create dictionary
    ...    ewallet_cd=ABCDGM
    ...    ewallet_name=ABCD7xG8
    set test variable    &ewallet_details
    Given user navigates to menu Configuration | Reference Data | E-wallet
    When user creates ewallet with random data
    Then ewallet created successfully with message 'Record created successfully'
    When user selects ewallet to edit
    And user edits ewallet with fixed data
    Then ewallet edited successfully with message 'Record updated successfully'
    When user selects ewallet to delete
    Then ewallet deleted successfully with message 'Record deleted'

2 - Able to edit ewallet data with random data
    [Tags]   sysimp     9.0
    Given user navigates to menu Configuration | Reference Data | E-wallet
    When user creates ewallet with random data
    Then ewallet created successfully with message 'Record created successfully'
    When user selects ewallet to edit
    And user edits ewallet with random data
    Then ewallet edited successfully with message 'Record updated successfully'
    When user selects ewallet to delete
    Then ewallet deleted successfully with message 'Record deleted'