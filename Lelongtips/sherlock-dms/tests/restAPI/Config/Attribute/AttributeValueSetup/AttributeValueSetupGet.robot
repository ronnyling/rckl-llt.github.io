*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupGet.py

*** Test Cases ***
1 - Able to retrieve all Attribute Value Setup
    [Documentation]  To retrieve all Attribute Value Setup record via API
    [Tags]    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all attribute value setup
    Then expected return status code 200

2 - Able to retrieve Attribute Value Setup by using id
    [Documentation]  To retrieve attribute value setup by passing in ID via API
    [Tags]    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all attribute value setup
    Then expected return status code 200
    When user retrieves attribute value setup by valid id
    Then expected return status code 200
