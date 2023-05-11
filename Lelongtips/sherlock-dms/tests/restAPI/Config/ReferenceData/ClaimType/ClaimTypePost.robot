*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypeDelete.py
Library           Collections

*** Test Cases ***
1 - Able to create Claim Type with random data
    [Documentation]    To create valid claim type with random generate data
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates valid claim type with random data
    Then expected return status code 201
    When user deletes claim type with created data

2 - Able to create Claim Type with given data
    [Documentation]    To create valid claim type with given data
    [Tags]     hqadm    9.0
    ${claim_type_details}=    create dictionary
    ...    CLAIM_TYPE_DESC=Testing 12345
    set test variable   &{claim_type_details}
    Given user retrieves token access as ${user_role}
    When user creates valid claim type with given data
    Then expected return status code 201
    When user deletes claim type with created data

3 - Able to create Claim Type with data from file
    [Documentation]    To create valid claim type with given data
    [Tags]     hqadm    9.0
    User retrieve test data from "ClaimTypeData.csv" located at "ReferenceData" folder
    ${claim_type_details}=   get from dictionary   ${file_data}     random description
    set test variable   &{claim_type_details}
    Given user retrieves token access as ${user_role}
    When user creates valid claim type with given data
    Then expected return status code 201
    When user deletes claim type with created data
    Then expected return status code 200
