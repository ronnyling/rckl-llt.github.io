*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/HSN/HsnGet.py

*** Test Cases ***
1 - Able to retrieve created HSN
    [Documentation]    Able to retrieve created Hsn and return status code 200
    [Tags]     hqadm   mrp    distadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all hsn
    Then expected return status code 200

2 - Able to retrieve created HSN by code
    [Documentation]    Able to retrieve created Hsn and return status code 200
    [Tags]     hqadm   mrp    distadm    9.0
    Given user retrieves token access as ${user_role}
    When user get hsn by code   HSNHANAF
    Then expected return status code 200
