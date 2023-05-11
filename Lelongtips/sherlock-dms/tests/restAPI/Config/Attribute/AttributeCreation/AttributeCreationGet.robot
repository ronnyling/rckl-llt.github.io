*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/Attribute/AttributeCreation/AttributeCreationGet.py

*** Test Cases ***
1 - Able to retrieve all Attribute Creation
    [Documentation]  To retrieve all Attribute Creation record via API
    [Tags]    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all attribute creation
    Then expected return status code 200

2 - Able to retrieve Attribute Creation by using id
    [Documentation]  To retrieve attribute creation by passing in ID via API
    [Tags]    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all attribute creation
    Then expected return status code 200
    When user retrieves attribute creation by valid id
    Then expected return status code 200
