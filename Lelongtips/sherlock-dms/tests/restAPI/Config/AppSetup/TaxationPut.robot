*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/TaxationGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/TaxationPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application_setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

#not applicable to hqadm
*** Test Cases ***
1 - Able to update taxation using fixed data
    [Documentation]    Able to update taxation using fixed data
    [Tags]     sysimp   9.1
    ${AppSetupDetails}=    create dictionary
    ...    TAX_MODEL=Product Taxation
    ...    TAX_CONFIGURATIONS_ACCUMULATIVE=${false}
    ...    TAX_CONFIGURATION_ENABLE_MULTI_SELECTION=${false}
    ...    DISCOUNT_IMPACT_FOR_TAX_COMPUTATION=${true}
    ...    DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION=Customer Disc,Promo Disc
    ...    ENABLE_SERVICE_TAX_FOR_SPACE_BUY_PROMOTION=${true}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup taxation details using fixed data
    Then expected return status code 200
