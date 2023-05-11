*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/FieldForcePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
1 - Able to update app setup and set Telesales Control By Distributor
    [Documentation]    Able to update app setup and set Telesales Control By Distributor
    [Tags]     hqadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=DIST
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200

2 - Able to update app setup and set Telesales Control By HQ
    [Documentation]    Able to update app setup and set Telesales Control By HQ
    [Tags]     hqadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    TELE_SALES_CONTROL_BY=HQ
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200

3 - Able to update app setup and set Call Plan for Telesales to Common
    [Documentation]    Able to update app setup and set Call Plan for Telesales to Common
    [Tags]     hqadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    CALL_PLAN_FOR_TELESALES=COMMON
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200

4 - Able to update app setup and set Call Plan for Telesales to Individual
    [Documentation]    Able to update app setup and set Call Plan for Telesales to Individual
    [Tags]     hqadm    9.3
    ${AppSetupDetails}=    create dictionary
    ...    CALL_PLAN_FOR_TELESALES=INDIVIDUAL
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200

5 - Able to update app setup and update Sales Order Product Filter Level
    [Documentation]    Able to update app setup and update Sales Order Product Filter Level
    [Tags]     hqadm    9.3     NRSZUANQ-57016
    ${AppSetupDetails}=    create dictionary
    ...    SO_PROD_FILTER_LEVEL=Brand
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200

6 - Able to update app setup and update Sales Order History Count
    [Documentation]    Able to update app setup and update Sales Order History Count
    [Tags]     hqadm    9.3     NRSZUANQ-57017
    ${AppSetupDetails}=    create dictionary
    ...    SO_HISTORY_COUNT=${50}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200

7 - Able to update app setup and update My Store Call Plan Days
    [Documentation]    Able to update app setup and update My Store Call Plan Days
    [Tags]     hqadm    9.3     NRSZUANQ-57019
    ${AppSetupDetails}=    create dictionary
    ...    CALL_DAYS=${80}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup field force details using fixed data
    Then expected return status code 200