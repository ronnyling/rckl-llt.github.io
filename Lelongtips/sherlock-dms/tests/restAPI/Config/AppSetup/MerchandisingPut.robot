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
1 - Able to update merchandising using fixed data
    [Documentation]    Able to update merchandising using fixed data
    ...    not applicable to sysimp
    [Tags]     hqadm   9.1   9.2     NRSZUANQ-44187​
    ${AppSetupDetails}=    create dictionary
    ...    MDSE_PROD_HIERARCHY_LEVEL=Brand
    ...    MDSE_AUTO_POP_FACING_SETUP=${False}
    ...    MDSE_ROUTE_ACTIVITIES-_Customer_Hierarchy_Level=Type
    ...    MDSE_POSM_INV_TRIG=HHT
    ...    MDSE_CUST_LEVEL=${False}
    ...    MDSE_CUST_HIERARCHY_LEVEL=Channel
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200

2 - Able to update merchandising audit by using fixed data
    [Documentation]    Able to update merchandising audit by using fixed data
    [Tags]     sysimp   9.1
    ${AppSetupDetails}=    create dictionary
    ...    MDSE_AUDIT_BY=Category
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200

3 - Able to update merchandising product hierarchy using empty data
    [Documentation]    Able to update merchandising product hierarchy using empty data
    [Tags]     hqadm   9.2    NRSZUANQ-44189
    ${AppSetupDetails}=    create dictionary
    ...    MDSE_PROD_HIERARCHY_LEVEL=${null}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 200

4 - Able to update merchandising product hierarchy using invalid data
    [Documentation]    Able to update merchandising product hierarchy using empty data
    [Tags]     hqadm   9.2     NRSZUANQ-44191
    ${AppSetupDetails}=    create dictionary
    ...    MDSE_PROD_HIERARCHY_LEVEL=abcdef123
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup details using fixed data
    Then expected return status code 404