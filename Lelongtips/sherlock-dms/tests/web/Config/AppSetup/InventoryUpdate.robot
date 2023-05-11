*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/InventoryEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Able to update inventory using random data
    [Documentation]    Able to update inventory using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Inventory tab
    Then user updates Inventory using random data
    And Inventory tab updated successfully with message 'Record updated successfully'

2 - Able to update inventory using fixed data
    [Documentation]    Able to update inventory using given data
    [Tags]    sysimp    9.1
    ${InventoryDetails}=    create dictionary
    ...    Stock_Adjustment_Approval=${False}
    ...    Stock_Out_Approval=${True}
    ...    Stock_Audit_Approval=${False}
    set test variable    &{InventoryDetails}
    When user navigates to menu Configuration | Application Setup
    And user navigates to Inventory tab
    Then user updates Inventory using fixed data
    And Inventory tab updated successfully with message 'Record updated successfully'



