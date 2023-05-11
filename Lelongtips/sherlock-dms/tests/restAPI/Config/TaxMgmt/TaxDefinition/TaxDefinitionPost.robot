*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxDefinition/TaxDefinitionPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/TaxDefinition/TaxDefinitionDelete.py

*** Test Cases ***
1 - Able to create tax definition using random data
    [Documentation]    Able to create tax definition and return status code 201
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates tax definition using random data
    Then expected return status code 200
    And verified created data is matching with the response body
    When user deletes created tax definition
    Then expected return status code 200
