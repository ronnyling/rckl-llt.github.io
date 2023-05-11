*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonPost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonDelete.py

Test Setup        user retrieves reason type 'Return - Bad Stock'

*** Test Cases ***
1 - Able to create Reason with random data
    [Documentation]  To create valid reason with random generated data via API
    [Tags]    hqadm    hquser     9.0
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 201
    When user deletes reason with created data
    Then expected return status code 200

2 - Able to create Reason with given data
    [Documentation]  To create valid reason with given generated data via API
    [Tags]    hqadm    hquser     9.0
    ${reason_details}=    create dictionary
    ...    REASON_CD=R1001
    ...    REASON_DESC=Reason Test 1
    set test variable   &{reason_details}
    Given user retrieves token access as ${user_role}
    When user creates reason with fixed data
    Then expected return status code 201
    When user deletes reason with created data
    Then expected return status code 200

3- Unable to create the reason data with mandatory fields as blank
    [Documentation]  This test is to verify the user is unable to create reason data  information with mandatory fields with blank value
    [Tags]    hqadm    9.2
    ${reason_details}=    create dictionary
    ...    REASON_CD=${EMPTY}
    ...    REASON_DESC=${EMPTY}
    set test variable   &{reason_details}
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 400

4- Unable to create the reason data with mandatory fields as leading space
    [Documentation]  This test is to verify the user is unable to create reason data  information with mandatory fields with spaces
    [Tags]    hqadm    9.2
    ${reason_details}=    create dictionary
    ...    REASON_CD=${Space}
    ...    REASON_DESC=${Space}
    set test variable   &{reason_details}
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 400

5- Unable to create the reason data with mandatory fields as invalid values
    [Documentation]  This test is to verify the user is unable to create reason data  information with mandatory fields with invalid values
    [Tags]    hqadm    9.2
    ${reason_details}=    create dictionary
    ...    REASON_CD=-+%
    ...    REASON_DESC=agdesc$%^&^
    set test variable   &{reason_details}
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 400

6- Unable to create the reason type with characters more that the maximum limit for each field
    [Documentation]  This test is to verify that the user is unable to create reason data
    ...    information with the values execeeding the maximum characters in each field
    [Tags]    hqadm     9.2
    ${reason_details}=    create dictionary
    ...    REASON_CD=abcdefghij1234567890k
    ...    REASON_DESC=12345abcde12345fghij12345klmno12345pqrst12345uvwxy1
    set test variable   &{reason_details}
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 400

7- Unable to create the reason type with duplicate values
    [Documentation]  This test is to verify that the user is unable to create the reason type with duplicate values
    [Tags]    hqadm    9.2
    Given user retrieves token access as ${user_role}
    When user creates reason with random data
    Then expected return status code 201
    When user creates reason with existing data
    Then expected return status code 409

