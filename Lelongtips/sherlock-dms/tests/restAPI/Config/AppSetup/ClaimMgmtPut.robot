*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/ClaimMgmtGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/ClaimMgmtPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update the App Setup - Claim Management records
    [Documentation]    Able to update the App Setup - Claim Management records
    [Tags]     hqadm   9.1      9.1.1    NRSZUANQ-41908
    ${AppSetupDetails}=    create dictionary
    ...     CM_ENBL_STK_OUT_DMG_CLAIM=${True}
    ...     CM_ENBL_CLAIM_ACK=${True}
    ...     CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    ...     CM_PROMO_AUTO_CLAIM=${True}
    ...     CM_PROMO_DAY_CLAIM_GEN=${7}
    ...     CM_AUTO_PROMO_CLAIM_TYPE=Single
    ...     CM_DMG_AUTO_CLAIM=${True}
    ...     CM_DMG_DAY_CLAIM_GEN=${3}
    ...     CM_OTHERS_DAY_CLAIM_GEN=${7}
    ...     CM_AUTO_CLAIM_STAT=Confirmed
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup claim management details using fixed data
    Then expected return status code 200