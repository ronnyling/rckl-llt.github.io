*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnEntitlementPost.py
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnApplyPost.py
Library           Collections


*** Test Cases ***
1 - Able to post invoice with FOC promo for return apply
    [Documentation]    User sends payload with non FOC promotion to return entitlement API
    [Tags]     distadm2    9.1     NRSZUANQ-26651
    Given user retrieve test data from "ReturnApplyDataAPI.csv" located at "CustTrx" folder
    ${return_details}=   get from dictionary   ${file_data}     FOC promo 1 product
    Set test variable   &{return_details}
    And user retrieves token access as ${user_role}
    When user post invoice with foc to return apply
    ${Status_Code}=     get from dictionary    ${return_details}    Expected_Status_Code
    ${Status_Code}=     Convert to string   ${Status_Code}
    Then expected return status code ${Status_Code}     # assertion is performed on string values

2 - Able to post invoice with FOC promo for return apply
    [Documentation]    User sends payload with FOC and non FOC to return entitlement API
    [Tags]     distadm2    9.1     NRSZUANQ-26651
    Given user retrieve test data from "ReturnApplyDataAPI.csv" located at "CustTrx" folder
    ${return_details}=   get from dictionary   ${file_data}     FOC and non FOC promos 2 product
    Set test variable   &{return_details}
    And user retrieves token access as ${user_role}
    When user post invoice with foc to return apply
    ${Status_Code}=     get from dictionary    ${return_details}    Expected_Status_Code
    ${Status_Code}=     Convert to string   ${Status_Code}
    Then expected return status code ${Status_Code}
