*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/AccountPayableEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py


*** Test Cases ***
1 - Updates the field in Account Payable with random data
    [Documentation]    Updates the field in Account Payable
    [Tags]     hqadm    9.1
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Accounts Payable tab
    Then user updates account payable using random data
    And account payable update updated successfully with message 'Record updated successfully'

2 - Updates the field in Account Payable with fixed data
    [Documentation]    Updates the field in Account Payable
    [Tags]     hqadm    9.1
    ${AccountPayableDetails}=    create dictionary
    ...    Make_Reference_Number_Mandatory=${False}
    set test variable    &{AccountPayableDetails}
     Given user navigates to menu Configuration | Application Setup
    When user navigates to Accounts Payable tab
    Then user updates account payable using fixed data
    And account payable updated successfully with message 'Record updated successfully'