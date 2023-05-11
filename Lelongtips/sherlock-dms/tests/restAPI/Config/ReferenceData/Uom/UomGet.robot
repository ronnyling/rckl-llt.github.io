*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomDelete.py

*** Test Cases ***
1 - Able to retrieve all Uom data
    [Documentation]  To retrieve all uom record via API
    [Tags]    sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates uom with RandomData
    Then expected return status code 201
    When user gets all uom data
    Then expected return status code 200
    When user deletes uom with created data
    Then expected return status code 200

2 - Able to retrieve Uom by using id
    [Documentation]  To retrieve uom by passing in ID via API
    [Tags]    sysimp    hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates uom with RandomData
    Then expected return status code 201
    When user gets uom by using id
    Then expected return status code 200
    When user deletes uom with created data
    Then expected return status code 200
