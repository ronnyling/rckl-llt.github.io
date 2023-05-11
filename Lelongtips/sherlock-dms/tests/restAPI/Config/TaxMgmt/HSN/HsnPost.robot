*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/TaxMgmt/HSN/HsnPost.py

*** Test Cases ***
1 - Able to create HSN with random data
    [Documentation]    Able to retrieve created Hsn and return status code 200
    [Tags]     hqadm   mrp    9.0
    Given user retrieves token access as ${user_role}
    When user creates hsn using random data
    Then expected return status code 200

