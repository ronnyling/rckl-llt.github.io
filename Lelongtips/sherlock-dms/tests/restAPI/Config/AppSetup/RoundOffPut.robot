*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/RoundOffGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/RoundOffPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

#not applicable to sysimp
*** Test Cases ***
1 - Able to update round off using fixed data
    [Documentation]    Able to update round off using fixed data
    [Tags]     hqadm   9.1
    ${AppSetupDetails}=    create dictionary
    ...    CURRENCY_SETTING=$
    ...    CURRENCY_NAME=Dollar
    ...    ROUND_OFF_DECIMAL=${4}
    ...    ROUND_OFF_DECIMAL_DISPLAY=${2}
    ...    ROUND_OFF_VALUE=0.5    #string
    ...    ROUND_OFF_TO_THE=Nearest
    ...    PAYMENT_ADJUSTMENT=${1}
    ...    INVOICE_ADJUSTMENT_METHOD=No Adjustment
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup round off details using fixed data
    Then expected return status code 200