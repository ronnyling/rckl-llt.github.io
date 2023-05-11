*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/TaxationEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
# not applicable for hqadm
1 - Able to update taxation using random data
    [Documentation]    Able to update taxation using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Taxation tab
    Then user updates taxation using random data
    And taxation updated successfully with message 'Record updated successfully'

2 - Able to update taxation using fixed data
    [Documentation]    Able to update taxation using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Taxation tab
    ${TaxationDetails}=    create dictionary
    ...    Tax_Model=Product Taxation
    ...    Accumulative_Tax_Enable=${false}
    ...    Tax_Setting_Apply_On_-_Multi_Select=${false}
    ...    Discount_Impact=${true}
    ...    Discounts_to_Be_Considered=Customer Disc
    ...    Enable_Service_Tax_-_Space_Buy=${true}
    set test variable    &{TaxationDetails}
    Then user updates taxation using fixed data
    And taxation updated successfully with message 'Record updated successfully'
