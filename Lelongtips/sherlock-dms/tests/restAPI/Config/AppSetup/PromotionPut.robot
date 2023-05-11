*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PromotionGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PromotionPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

#not applicable to sysimp
*** Test Cases ***
1 - Able to update promotion using fixed data
    [Documentation]    Able to update promotion using fixed data
    [Tags]     hqadm   9.1
    ${AppSetupDetails}=    create dictionary
    ...    APPLY_PROMOTIONS=${False}
    ...    ALLOW_MULTIPLE_PROMO_APPLICATION_FOR_A_LINE=${True}
    ...    ALLOW_PROMOTION_FOR_UNAPPROVED_CUSTOMERS=${False}
    ...    APPLY_PROMOTION_BASED_ON=Sales Order Date
    ...    QPS_OPN_INV_CHK=Alert and Block
    ...    QPS_ELG_BASED_ON=Confirmation Date
    set test variable    &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup promotion details using fixed data
    Then expected return status code 200