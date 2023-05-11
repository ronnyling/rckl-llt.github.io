*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/GeneralEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Able to update General using random data
    [Documentation]    Able to update General using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to General tab
    Then user updates general using random data
    And general updated successfully with message 'Record updated successfully'

2 - Able to update General using fixed data
    [Documentation]    Able to update General using given data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to General tab
    ${GeneralDetails}=    create dictionary
    ...    Company Name=Company Name
    ...    Business Registration Number=100
    ...    Product Sector Assignment=${True}
    ...    Active SKU (3-12 Months)=12
    ...    Auto CN Adjustment in Invoice=${False}
    set test variable    &{GeneralDetails}
    Then user updates general using fixed data
    And general updated successfully with message 'Record updated successfully'

3 - Able to update General(HHT) using given data
    [Documentation]    Able to update General(HHT) using given data
    [Tags]    hqadm    9.1    ABCD1234
    When user navigates to menu Configuration | Application Setup
    And user navigates to General tab
    ${GeneralDetails}=    create dictionary
    ...    HHT Product Hierarchy=all
    ...    HHT Product Grouping Feature Level=1
    ...    HHT Order UI Template=Inline
    ...    HHT End Visit Sync=${False}
    ...    HHT Landing Page=My Stores
    ...    HHT Allow Show Route Plan Desc=${True}
    ...    HHT Signature Control=${True}
    ...    HHT Signature Control Screens=all
    ...    HHT POSM Filter by=all
    ...    Enable Distributor Transaction Number=${False}
    set test variable    &{GeneralDetails}
    Then user updates general using fixed data
    And general updated successfully with message 'Record updated successfully'

#Sysimp
4 - Able to update General using given data
    [Documentation]    Able to update General using given data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to General tab
    ${GeneralDetails}=    create dictionary
    ...    Product Hierarchy for Display=Brand
    ...    Customer Hierarchy for Display=Type
    ...    Enable Multi Principal=${True}
    ...    Time Zone=Asia/Kuala_Lumpur - Malaysia Time
    set test variable    &{GeneralDetails}
    Then user updates general using fixed data
    And general updated successfully with message 'Record updated successfully'
