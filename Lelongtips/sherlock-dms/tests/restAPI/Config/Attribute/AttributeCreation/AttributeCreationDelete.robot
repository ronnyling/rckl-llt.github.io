*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationDelete.py

*** Test Cases ***
1 - Able to delete created attribute creation
    [Documentation]    Able to create attribute creation and return status code 201
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute creation using random data
    Then expected return status code 201
    When user deletes created attribute creation
    Then expected return status code 200
