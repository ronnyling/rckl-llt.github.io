*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletEditPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletDeletePage.py

*** Test Cases ***
1 - Able to Delete Ewallet using random data
    [Tags]    sysimp    9.1.1
    Given user navigates to menu Configuration | Reference Data | E-wallet
    When user creates ewallet with random data
    Then ewallet created successfully with message 'Record created successfully'
    When user selects ewallet to delete
    Then ewallet deleted successfully with message 'Record deleted'