*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PerformanceGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PerformancePut.py


Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***

1 - Able to update performance using fixed data
    [Documentation]    Able to update performance using fixed data
    ...    This is not applicable to sysimp
    [Tags]     hqadm   9.1
    ${AppSetupDetails}=    create dictionary
    ...    DAILY_VISIT_TARGET_FORMULA=Roll Over
    ...    ALLOW_EDITING_CURRENT_MONTH=${True}
    ...    ALLOW_EDITING_CURRENT_MONTH_TGT_FOR_DAYS=${26}
    ...    SALES_PERFORMANCE_VALUE_BASED_ON=Nett
    ...    PERFORMANCE_INDICATOR_CONDITIONS_RED=${60.00}
    ...    PERFORMANCE_INDICATOR_CONDITIONS_AMBER_MAX=${80.00}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup performance details using fixed data
    Then expected return status code 200


2 - Able to update vs score card section in performance using fixed data
    [Documentation]    Able to update vs score card section in performance using fixed data
    ...    not applicable to sysimp
    [Tags]     sysimp   9.1
    ${AppSetupDetails}=    create dictionary
    ...    VSSC_ENABLE_SCORE_LIMIT=${True}
    ...    VSSC_MAX_SCORE=${100}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200