*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/Uom/UomPut.py

Test Setup  run keywords
...    user retrieves token access as ${user_role}
...    AND    user creates uom with random data
...    AND    expected return status code 201

Test Teardown  run keywords
...    user deletes uom with created data
...    AND    expected return status code 200

*** Test Cases ***
1 - Able to edit Uom with random data by using id
    [Documentation]  To edit uom by passing in ID via API
    [Tags]    sysimp    hqadm    9.0
    When user edits uom with random data
    Then expected return status code 200

2 - Able to edit Uom with given data by using id
    [Documentation]  To edit uom by passing in ID via API
    [Tags]    sysimp   hqadm   9.0
    ${uom_details} =    create dictionary
    ...    UOM_DESCRIPTION=Bucket
    When user edits uom with fixed data
    Then expected return status code 200
