*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypeDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypePut.py
Library           Collections


*** Test Cases ***
1 - Able to update promotion claim type via API
    [Documentation]    To retrieve all valid claim type
    [Tags]     hqadm    9.0
    User retrieve test data from "ClaimTypeData.csv" located at "ReferenceData" folder
    ${claim_type_details}=   get from dictionary   ${file_data}     different description
    set test variable   &{claim_type_details}
    Given user retrieves token access as ${user_role}
    When user creates valid claim type with given data
    Then expected return status code 201
    When user updates claim type with ${payload}
    Then expected return status code 200
    When user deletes claim type with created data
