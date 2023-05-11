*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitDelete.py

*** Test Cases ***
1 - Able to delete an dimension unit
    [Documentation]    To Delete the dimension unit
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates valid dimension unit with random data
    Then expected return status code 201
    When user deletes dimension unit with created data
    Then expected return status code 200