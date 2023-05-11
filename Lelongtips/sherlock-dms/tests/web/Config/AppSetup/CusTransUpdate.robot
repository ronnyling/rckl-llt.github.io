*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/CusTransEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Updates the field in Customer Transfer with random data
    [Documentation]    Updates the field in Customer Transfer
    [Tags]     hqadm    9.1
    set test variable     ${tab_label}    Customer Transfer
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Customer Transfer tab
    Then user updates customer transfer using random data
    And Customer Transfer updated successfully with message 'Record updated successfully'

2 - Updates the field in Customer Transfer with fixed data
    [Documentation]    Updates the field in Customer Transfer
    [Tags]     hqadm    9.1
    set test variable     ${tab_label}    Customer Transfer
    ${Cus_Trans_Details}=    create dictionary
    ...    Customer with Outstanding Collection=${False}
    ...    Customer with Open Order=${True}
    ...    Customer with Unconfirmed Invoice=${True}
    ...    Customer with Unconfirmed Return=${False}
    ...    Customer with Unconfirmed Exchange=${True}
    ...    Customer with Unconfirmed CN / DN=${True}
    ...    Customer with Assigned Trade Asset=${False}
    set test variable    &{Cus_Trans_Details}
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Customer Transfer tab
    Then user updates customer transfer using fixed data
    And Customer Transfer updated successfully with message 'Record updated successfully'