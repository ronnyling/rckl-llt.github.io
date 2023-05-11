*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/RoundOffEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

#not applicable to sysimp
*** Test Cases ***
1 - Able to update round off using random data
    [Documentation]    Able to update round off using random data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Round Off tab
    Then user updates round off using random data
    And round off updated successfully with message 'Record updated successfully'

2 - Able to update round off using fixed data
    [Documentation]    Able to update round off using fixed data
    [Tags]    hqadm    9.1
    When user navigates to menu Configuration | Application Setup
    And user navigates to Round Off tab
    ${RoundOffDetails}=    create dictionary
    ...    Currency_Setting=$
    ...    Currency_Name=Dollar
    ...    Round_Off_Decimal_(Data_Storage)=${4}
    ...    Round_Off_Decimal_(Display)=${2}
    ...    Round_Off_Value=0.5    #string
    ...    Round_Off_to_the=Nearest
    ...    Payment_Adjustment=${1}
    ...    Invoice_Adjustment_Method=No Adjustment
    set test variable    &{RoundOffDetails}
    Then user updates round off using fixed data
    And round off updated successfully with message 'Record updated successfully'
