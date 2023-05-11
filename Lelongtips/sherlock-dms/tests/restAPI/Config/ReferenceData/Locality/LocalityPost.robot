*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py


*** Test Cases ***
1 - Able to create Locality with random data
    [Documentation]  To create valid locality with random generated data via API
    [Tags]    sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates locality with random data
    Then expected return status code 201
    When user deletes locality with created data
    Then expected return status code 200

2- Able to create Locality with fixed data
    [Documentation]  To create valid locality with fixed data via API
    [Tags]    sysimp     9.0
    ${locality_details}=    create dictionary
    ...    CITY_CD=KTN
    ...    CITY_NAME=Kuantan
    set test variable   &{locality_details}
    Given user retrieves token access as ${user_role}
    When user creates locality with fixed data
    Then expected return status code 201
    When user deletes locality with created data
    Then expected return status code 200

3- Able to create Locality and relate to Country
    [Documentation]  To create valid Locality and link relationship with State via API
    [Tags]     sysimp     9.0
    Given user retrieves token access as ${user_role}
    When user creates state with random data
    Then expected return status code 201
    When user creates locality with random data
    Then expected return status code 201
    When user deletes locality with created data
    Then expected return status code 200
    When user deletes state with created data
    Then expected return status code 200
