*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypeDelete.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ClaimType/ClaimTypeGet.py
Library           Collections


*** Test Cases ***
1 - Able to get all Claim Type
    [Documentation]    To retrieve all valid claim type
    [Tags]     hqadm    9.0
    Given user retrieves token access as ${user_role}
    When user retrieves all promotion claim type

2 - Able to get Claim Type by ID
    [Documentation]    To retrieve valid claim type by ID
    [Tags]     hqadm    9.0     claim
    User retrieve test data from "ClaimTypeData.csv" located at "ReferenceData" folder
    ${claim_type_details}=   get from dictionary   ${file_data}     claim2
    Given user retrieves token access as ${user_role}
    When user retrieves promotion claim type by ID
