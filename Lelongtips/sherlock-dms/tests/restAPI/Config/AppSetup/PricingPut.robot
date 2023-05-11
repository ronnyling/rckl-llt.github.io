*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PricingGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/PricingPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200
#not applicable to hqadm
*** Test Cases ***
1 - Able to update pricing using fixed data
    [Documentation]    Able to update pricing using fixed data
    [Tags]     sysimp   9.1
    Given user retrieves token access as ${user_role}
    ${AppSetupDetails}=    create dictionary
    ...    MRP_MANAGED=${false}
    ...    BATCH_MANAGED=${false}
    ...    ALLOW_BATCH_CREATION_BY_DISTRIBUTOR=${true}
    ...    NO_OF_MARGIN_INPUT=${3}
    ...    MARGIN_NAMING_CONVENTION_1=Retailer Margin    # fixme: can the margin naming covention be randomized?
    ...    MARGIN_NAMING_CONVENTION_2=Sub Stockiest Margin
    ...    MARGIN_NAMING_CONVENTION_3=Distributor Margin
    set test variable   &{AppSetupDetails}
    When user updates app setup pricing details using fixed data
    Then expected return status code 200
