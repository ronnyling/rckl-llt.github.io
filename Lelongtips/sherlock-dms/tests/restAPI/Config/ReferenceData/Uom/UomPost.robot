*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomDelete.py

*** Test Cases ***
1 - Able to create Uom with random data
    [Documentation]  To create valid uom with random generated data via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates uom with random data
    Then expected return status code 201
    When user deletes uom with created data
    Then expected return status code 200

2- Able to create Uom with given data
    [Documentation]  To create valid uom with given data via API
    [Tags]    sysimp     9.0
    ${uom_details}=    create dictionary
    ...    UOM_CD=U11
    ...    UOM_DESCRIPTION=United pack
    Given user retrieves token access as ${user_role}
    When user creates uom with fixed data
    Then expected return status code 201
    When user deletes uom with created data
    Then expected return status code 200
