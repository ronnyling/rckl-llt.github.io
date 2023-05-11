*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Country/CountryPut.py

Test Setup  run keywords
...    user retrieves token access as ${user_role}
...    AND    user creates country with random data
...    AND    expected return status code 201

Test Teardown  run keywords
...    user deletes country with created data
...    AND    expected return status code 200

*** Test Cases ***

1 - Able to edit Country with random data by using id
    [Documentation]  To edit country by passing in ID via API
    [Tags]    sysimp     9.0
    When user edits country with random data by using valid id
    Then expected return status code 200

2 - Able to edit Country with fixed data by using id
    [Documentation]  To edit country by passing in ID via API
    [Tags]    sysimp     9.0
    ${country_update_details} =    create dictionary
    ...    COUNTRY_CD=Moroco
    ...    COUNTRY_NAME=Moroco2
    When user edits country with fixed data by using valid id
    Then expected return status code 200

3 - Unable to edit Country by using invalid id
    [Documentation]  Unable to edit country by passing in invalid ID via API
    [Tags]    sysimp     9.0
    When user edits country with random data by using invalid id
    Then expected return status code 404