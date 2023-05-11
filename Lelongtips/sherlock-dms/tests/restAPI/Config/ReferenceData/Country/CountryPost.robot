*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py

*** Test Cases ***
1 - Able to create Country with random data
    [Documentation]  To create valid country with random generated data via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates country with random data
    Then expected return status code 201
    When user deletes country with created data
    Then expected return status code 200

2- Able to create Country with fixed data
    [Documentation]  To create valid country with fixed data via API
    [Tags]    sysimp     9.0
    ${country_details}=    create dictionary
    ...    COUNTRY_CD=InKU
    ...    COUNTRY_NAME=Indiaku
    set test variable   &{country_details}
    Given user retrieves token access as ${user_role}
    When user creates country with fixed data
    Then expected return status code 201
    When user deletes country with created data
    Then expected return status code 200
