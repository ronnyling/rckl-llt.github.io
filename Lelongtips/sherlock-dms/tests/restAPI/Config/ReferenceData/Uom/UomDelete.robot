*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomDelete.py

*** Test Cases ***
1 - Able to delete uom with created data
    [Documentation]  To delete uom by passing in id via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates uom with random data
    Then expected return status code 201
    When user deletes uom with created data
    Then expected return status code 200
