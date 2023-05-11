*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/VSScoreCardEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

#not applicable to hqadm
*** Test Cases ***
1 - Able to update vs score card using random data
    [Documentation]    Able to update vs score card using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to VS Score Card tab
    Then user updates vs score card using random data
    And vs score card updated successfully with message 'Record updated successfully'

2 - Able to update vs score card using fixed data
    [Documentation]    Able to update vs score card using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to VS Score Card tab
    ${VSScoreCardDetails}=    create dictionary
    ...    Van_Sales_MSL_Compliance_based_on=Van Sales
    ...    Merchandiser_MSL_Compliance_based_on=Distribution Check
    set test variable    &{VSScoreCardDetails}
    Then user updates vs score card using fixed data
    And vs score card updated successfully with message 'Record updated successfully'
