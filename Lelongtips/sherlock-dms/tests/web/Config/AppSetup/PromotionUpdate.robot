*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/PromotionEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

#not applicable to sysimp
*** Test Cases ***
1 - Able to update promotion using random data
    [Documentation]    Able to update promotion using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Promotion tab
    Then user updates promotion using random data
    And promotion updated successfully with message 'Record updated successfully'

2 - Able to update promotion using fixed data
    [Documentation]    Able to update promotion using fixed data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Promotion tab
    ${PromotionDetails}=    create dictionary
    ...    Apply_Promotion_(Auto/Manual)=${False}
    ...    Allow_Multiple_Promotion_-_SKU=${True}
    ...    Allow_Promotion_-_Unapproved_Customers=${False}
    ...    Apply_Promotion_based_on=Sales Order Date
    ...    QPS_Open_Invoice_Check=Alert and Block
    ...    QPS_Eligibility_based_on=Confirmation Date
    set test variable    &{PromotionDetails}
    Then user updates promotion using fixed data
    And promotion updated successfully with message 'Record updated successfully'
