** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Telesales/MyStore/TelesalesSalesOrderGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/FieldForcePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

*** Test Cases ***
1 - Able to get master product hierarchy list
    [Documentation]    Able to get master product hierarchy list
    [Tags]    telesales   9.3
    Given user retrieves token access as ${user_role}
    When user retrieves master product hierarchy list
    Then expected return status code 200

2 - Able to get master product hierarchy list based on brand hieraarchy app setup
    [Documentation]    Able to get master product hierarchy list based on brand hieraarchy app setup
    [Tags]    telesales   9.3
    [Setup]  run keywords
    ${AppSetupDetails}=    create dictionary
    ...    SO_PROD_FILTER_LEVEL=C209B33D:C29D93A3-AE1E-4C07-B770-B4FF56F99B75
    set test variable   &{AppSetupDetails}
    And user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup field force details using fixed data
    [Teardown]    run keywords
    ...   user retrieves token access as hqadm
    ...   user revert to previous setting
    ...   expected return status code 200
    Given user retrieves token access as ${user_role}
    When user retrieves master product hierarchy list
    Then expected return status code 200