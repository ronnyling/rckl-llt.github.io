*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/ReplenishmentEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Able to update Replenishment using random data
    [Documentation]    Able to update Replenishment using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Replenishment tab
    Then user updates Replenishment using random data
    And general updated successfully with message 'Record updated successfully'

2 - Able to update Replenishment using fixed data
    [Documentation]    Able to update Replenishment using given data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Replenishment tab
    ${ReplenishmentDetails}=    create dictionary
    ...    Default Replenishment Method=VMI
    ...    Replenishment AMS Months=3
    ...    Allow Edit of Replenishment Method=${False}
    ...    Validate Manual Purchase Order Qty=${False}
    set test variable    &{ReplenishmentDetails}
    Then user updates Replenishment using fixed data
    And general updated successfully with message 'Record updated successfully'
