*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/MerchandisingEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
#not applicable to sysimp
1 - Able to update merchandising using random data
    [Documentation]    Able to update merchandising using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Merchandising tab
    Then user updates merchandising using random data
    And merchandising updated successfully with message 'Record updated successfully'

#not applicable to sysimp
2 - Able to update merchandising using fixed data
    [Documentation]    Able to update merchandising using fixed data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Merchandising tab
    ${MerchandisingDetails}=    create dictionary
    ...    Product_Hierarchy_Level=Category
    ...    Auto_Populate_Facing_Setup=${False}
    ...    Route_Activities_-_Customer_Hierarchy_Level=Type
    ...    POSM_Inventory_Trigger=HHT
    ...    Customer_Level=${False}
    ...    Customer_Hierarchy_Level=Channel
    set test variable    &{MerchandisingDetails}
    Then user updates merchandising using fixed data
    And merchandising updated successfully with message 'Record updated successfully'

#not applicable to hqadm
3 - Able to update merchandising audit by using random data
    [Documentation]    Able to update merchandising audit by using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Merchandising tab
    Then user updates merchandising audit by using random data
    And merchandising updated successfully with message 'Record updated successfully'

#not applicable to hqadm
4 - Able to update merchandising using fixed data
    [Documentation]    Able to update merchandising using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Merchandising tab
    ${MerchandisingDetails}=    create dictionary
    ...    Merchandising_Audit_by=Category
    set test variable    &{MerchandisingDetails}
    Then user updates merchandising audit by using fixed data
    And merchandising updated successfully with message 'Record updated successfully'
