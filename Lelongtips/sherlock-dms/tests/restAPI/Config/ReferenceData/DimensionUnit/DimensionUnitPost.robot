*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitDelete.py

*** Test Cases ***

1 - Able to create Dimension Unit with random data
    [Documentation]    To create valid claim type with random generate data
    [Tags]     sysimp    9.2
    Given user retrieves token access as ${user_role}
    When user creates valid dimension unit with random data
    Then expected return status code 201
    When user deletes dimension unit with created data
    Then expected return status code 200

2 - Able to create Dimension Unit with given data
    [Documentation]    To create valid dimension unit with given data
    [Tags]     sysimp    9.2
    ${dimension_unit_details}=    create dictionary
    ...    DIMENSION_DESC=Testing 12345
    set test variable   &{dimension_unit_details}
    Given user retrieves token access as ${user_role}
    When user creates valid dimension unit with given data
    Then expected return status code 201
    When user deletes dimension unit with created data
    Then expected return status code 200

