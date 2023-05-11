*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/DimensionUnit/DimensionUnitDelete.py

*** Test Cases ***
1 - Able to update dimension unit via API
    [Documentation]    To update a created dimension unit
    [Tags]     sysimp    9.2
    ${dimension_unit_details_put}=    create dictionary
    ...    DIMENSION_DESC=Dimension Description by given data PUT
    set test variable   &{dimension_unit_details_put}
    Given user retrieves token access as ${user_role}
    When user creates valid dimension unit with random data
    Then expected return status code 201
    When user updates the created dimension unit
    Then expected return status code 200
    When user deletes dimension unit with created data
    Then expected return status code 200