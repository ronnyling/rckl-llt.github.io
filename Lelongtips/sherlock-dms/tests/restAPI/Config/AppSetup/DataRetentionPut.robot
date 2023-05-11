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
1 - Able to update the App Setup - Account payable records
    [Documentation]    Able to update the App Setup - Account payable records
    [Tags]     sysimp   9.1
    ${App_Setup_details}=    create dictionary
    ...     ORDER_STATUS=${7}
    ...     SALES_HISTORY=${1}
    ...     STOCK_TAKE_HISTORY=${90}
    ...     PAST_ROUTE_PLAN=${7}
    ...     FUTURE_ROUTE_PLAN=${7}
    ...     MISSED_CALL=${5}
    ...     MISSED_CALL_REMINDER=${5}
    ...     COUNT_OF_VISITS_TO_CONSIDER_FOR_AVG_SALES=${5}
    ...     NO_DISTRIBUTION_LIMIT_FOR_STOCK_TAKE_CONSIDERATION=${7}
    ...     PURGE_BATCH_CODE=${180}
    ...     MSL_COMPLIANCE=${60}
    ...     LOAD_INVOICE_FROM_PAST_DAYS=${3}
    ...     REF_DOC_PERIOD_SFA=${90}
    ...     REF_DOC_PERIOD_DMS=${90}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200