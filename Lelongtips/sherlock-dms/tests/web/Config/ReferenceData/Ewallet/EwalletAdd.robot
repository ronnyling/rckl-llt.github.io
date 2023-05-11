*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}setup/web/AlertCheck.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletAddPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletEditPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/Ewallet/EwalletDeletePage.py

Test Teardown    user deletes created ewallet

*** Test Cases ***
1 - Able to Create Ewallet with given data
    [Documentation]    Able to create Ewallet by using given data
    [Tags]     hqadm  9.1.1
    ${EWDetails}=    create dictionary
    ...    EwalletCode=Wallet1
    ...    description=Description1
    set test variable     &{EWDetails}
    Given user navigates to menu Configuration | Reference Data | E-wallet
    When user creates ewallet
    And e-wallet created successfully with message 'Record created successfully'
    Then user navigates back to listing page

2 - Able to Create Ewallet with random data
    [Documentation]    Able to create Ewallet by using random data
    [Tags]     hqadm    9.1.1
    ${EWDetails}=    create dictionary
    ...    type=random
    ...    description=random
    ...    date=random
    set test variable     &{EWDetails}
    Given user navigates to menu Configuration | Reference Data | Ewallet
    When user creates ewallet
    And ewallet created successfully with message 'Record created successfully'
    Then user navigates back to listing page

