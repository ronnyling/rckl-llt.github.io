*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Locality/LocalityPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StatePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/State/StateDelete.py

Test Setup    run keywords
...    user retrieves token access as ${user_role}
...    AND    user creates locality with random data
...    AND    expected return status code 201

Test Teardown  run keywords
...     user deletes locality with created data
...     AND expected return status code 200

*** Test Cases ***
1 - Able to edit Locality with random data
    [Documentation]  To edit locality with random generated data by passing in id via API
    [Tags]    sysimp     9.0
    When user edits locality with random data
    Then expected return status code 200

2- Able to edit Locality with fixed data
    [Documentation]  To edit locality with fixed data by passing in id via API
    [Tags]    sysimp     9.0
    ${locality_update_details}=    create dictionary
    ...    CITY_CD=KJKIL
    ...    CITY_NAME=Klang321
    When user edits locality with fixed data
    Then expected return status code 200

3- Able to create Locality and relate to State
    [Documentation]  To edit valid locality to link relationship with State via API
    [Tags]     sysimp     9.0
    When user creates state with random data
    Then expected return status code 201
    When user edits locality with created state data
    Then expected return status code 200
    When user deletes state with created data
    Then expected return status code 200

4 - Unable to edit Locality by using invalid id
    [Documentation]  Unable to edit locality by passing in invalid ID via API
    [Tags]    sysimp     9.0
    set test variable     ${ID_TYPE}   Invalid
    When user edits locality with random data by using invalid id
    Then expected return status code 404

5 - Unable to edit Locality with invalid payload
    [Documentation]  Unable to edit locality by passing in invalid payload via API
    [Tags]    sysimp     9.0
    ${locality_update_details}=    create dictionary
    ...    CITY_CD=&@%*#^#
    ...    CITY_NAME=&%#%^&$
    When user edits locality with invalid data by using valid id
    Then expected return status code 400
