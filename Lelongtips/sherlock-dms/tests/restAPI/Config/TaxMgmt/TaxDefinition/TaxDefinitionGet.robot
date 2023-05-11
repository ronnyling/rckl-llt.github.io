*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxDefinition/TaxDefinitionPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxDefinition/TaxDefinitionGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxDefinition/TaxDefinitionDelete.py

*** Test Cases ***
1 - Able to retrieve created tax definition
    [Documentation]    Able to retrieve created tax definition and return status code 200
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates tax definition using random data
    Then expected return status code 200
    When user retrieves all tax definition
    Then expected return status code 200
    When user deletes created tax definition
    Then expected return status code 200

2 - Able to retrieve created tax definition by code
    [Documentation]    Able to retrieve filtered tax definition by code
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user_get_tax_definition_by_code    NPTC0001
    Then expected return status code 200
