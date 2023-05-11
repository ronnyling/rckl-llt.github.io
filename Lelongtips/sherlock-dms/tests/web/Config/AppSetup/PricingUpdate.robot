*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/PricingEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
#not applicable for hqadm
1 - Able to update pricing using random data
    [Documentation]    Able to update pricing using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Pricing tab
    Then user updates pricing using random data
    And pricing updated successfully with message 'Record updated successfully'

2 - Able to update pricing using fixed data
    [Documentation]    Able to update pricing using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Pricing tab
    ${PricingDetails}=    create dictionary
    ...    MRP_Managed=${false}
    ...    Batch_Managed=${false}
    ...    Allow_Batch_Creation=${true}
    ...    No._of_Margin_Input=${3}
    ...    Margin_Naming_Convention_1=Retailer Margin
    ...    Margin_Naming_Convention_2=Sub Stockiest Margin
    ...    Margin_Naming_Convention_3=Distributor Margin
    set test variable    &{PricingDetails}
    Then user updates pricing using fixed data
    And pricing updated successfully with message 'Record updated successfully'

