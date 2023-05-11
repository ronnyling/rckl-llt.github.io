*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupDelete.py

*** Test Cases ***
1 - Able to delete created attribute value setup
    [Documentation]    Able to create attribute value setup and return status code 201
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute value setup using random data
    Then expected return status code 201
    When user deletes created attribute value setup
    Then expected return status code 200
