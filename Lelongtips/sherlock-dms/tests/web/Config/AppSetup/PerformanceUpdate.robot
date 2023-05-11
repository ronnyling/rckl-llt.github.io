*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/PerformanceEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
#not applicable to sysimp
1 - Able to update performance using random data
    [Documentation]    Able to update performance using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Performance tab
    Then user updates performance using random data
    And performance updated successfully with message 'Record updated successfully'

#not applicable to hqadm
2 - Able to update vs score card section in performance using random data
    [Documentation]    Able to update  vs score card section in performance using random data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Performance tab
    Then user updates vs score card in performance using random data
    And vs score card in performance updated successfully with message 'Record updated successfully'

#not applicable to sysimp
3 - Able to update performance using fixed data
    [Documentation]    Able to update performance using fixed data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Performance tab
    ${PerformanceDetails}=    create dictionary
    ...    Daily_Visit_Target_Formula=Roll Over
    ...    Allow_Editing_Current_Month=${True}
    ...    Allow_Editing_Target_for_(Days)=${26}
    ...    Sales_Performance_Value_based_on=Nett
    ...    Red_<_(%)=60.00
    ...    Amber_<_(%)=80.00
    set test variable    &{PerformanceDetails}
    Then user updates performance using fixed data
    And performance updated successfully with message 'Record updated successfully'

#not applicable to hqadm
4 - Able to update vs score card section in performance using fixed data
    [Documentation]    Able to update vs score card section in performance using fixed data
    [Tags]    sysimp    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Performance tab
    ${PerformanceDetails}=    create dictionary
    ...    Enable_Max_Score_Limit=${True}
    ...    Max_Score=${100}
    set test variable    &{PerformanceDetails}
    Then user updates vs score card in performance using fixed data
    And vs score card in performance updated successfully with message 'Record updated successfully'
