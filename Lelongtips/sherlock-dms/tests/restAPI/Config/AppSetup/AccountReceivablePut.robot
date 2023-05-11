*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update the App Setup - Account receivable records
    [Documentation]    Able to update the App Setup - Account receivable records
    [Tags]     sysimp   9.0   9.1.1    NRSZUANQ-41908
    ${App_Setup_details}=    create dictionary
    ...     RESTRICT_BILLING_IN_CASE_OF_OUTLET=${False}
    ...     ALLOW_TO_TOGGLE_CASH_CREDIT=${True}
    ...     MAKE_REFERENCE_NUMBER_MANDATORY=${False}
    ...     ALLOW_RETURN_CN_FROM_SINGLE_INVOICE_ONLY=${False}
    ...     ENABLE_PARTIAL_RETURN_PROMO_BENEFIT=${False}
    ...     RESTRICT_RETURN_INV_QTY=${False}
    ...     ALLOW_EDITING_PRICE_IN_RETURN_SFA=${True}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200