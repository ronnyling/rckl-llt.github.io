*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationDelete.py
Library           Collections


*** Test Cases ***
1 - Able to update attribute creation via API
    [Documentation]    To update created attribute creation and delete
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates attribute creation using random data
    Then expected return status code 201
    When user retrieves attribute creation by valid id
    Then expected return status code 200
    When user update created attribute creation
    Then expected return status code 200