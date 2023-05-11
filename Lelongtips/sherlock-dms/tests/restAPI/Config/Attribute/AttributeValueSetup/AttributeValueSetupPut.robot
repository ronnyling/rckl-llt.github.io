*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeValueSetup/AttributeValueSetupDelete.py
Library           Collections


*** Test Cases ***
1 - Able to update attribute value setup via API
    [Documentation]    To update created attribute value setup and delete
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute value setup using random data
    Then expected return status code 201
    When user retrieves attribute value setup by valid id
    Then expected return status code 200
    When user update created attribute value setup
    Then expected return status code 200
