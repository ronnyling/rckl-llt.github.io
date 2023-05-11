*** Settings ***

Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnEntitlementPost.py
Library           ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnApplyPost.py
Library           Collections


*** Test Cases ***
1 - Able to post invoice with non FOC promo for return entitlement
    [Documentation]    User sends payload with non FOC promotion to return entitlement API
    [Tags]     distadm2    9.1     NRSZUANQ-26651     NRSZUANQ-26633
    Given user retrieve test data from "ReturnEntitlementDataAPI.csv" located at "CustTrx" folder
    ${return_details}=   get from dictionary   ${file_data}     Non-FOC Invoice
    Set test variable   &{return_details}
    And user retrieves token access as ${user_role}
    When user sends invoice with non foc promo to return entitlement
    ${Status_Code}=     get from dictionary    ${return_details}    Expected_Status_Code
    ${Status_Code}=     Convert to string   ${Status_Code}
    Then expected return status code ${Status_Code}     # assertion is performed on string values

#2 - Able to post invoice with entitled promotions for return entitlement via data file
#    [Documentation]    User sends payload with non FOC promotion to return entitlement API
#    [Tags]     distadm2    9.1     NRSZUANQ-26651     NRSZUANQ-26633
#    Given user retrieves token access as ${user_role}
#    When user retrieve test data from "ReturnEntitlementDataAPI.csv" located at "CustTrx" folder
#    :FOR     ${each_set}     IN      @{file_data}
#    \   ${return_details}=    set variable     ${file_data["${each_set}"]}
#    \   set test variable   &{return_details}
#    \   user sends invoice with non foc promo to return entitlement
#    \   ${Status_Code}=     get from dictionary    ${return_details}    Expected_Status_Code
#    \   ${Status_Code}=     Convert to string   ${Status_Code}
#    \   expected return status code ${Status_Code}
