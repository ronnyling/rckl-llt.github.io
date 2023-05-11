*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteProduct/DebitNoteProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteProduct/DebitNoteProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

Test Setup       user creates Prime debit note as prerequisite


*** Test Cases ***
1 - Unable to update DN by adding product which not in distributor product sector and get 404 Not Found
    [Documentation]    Unable to update debit note using product which not assign to product sector
    [Tags]    distadm    9.1.1    NRSZUANQ-40277    prdSector
    [Teardown]  run keywords
    ...    user assigned product sector using fixed data
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${uom_details}=  create dictionary
    ...   UOM=PC1
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdActPS
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    When user unassigned product sector using fixed data
    Given user retrieves token access as ${user_role}
    When user updates debit note with fixed data
    Then expected return status code 404
    When user retrieves token access as hqadm
    Then user revert to previous setting

2 - Able to update DN by adding inactive product and get 200 OK
    [Documentation]    Able to update debit note using inactive product
    [Tags]    distadm    9.1.1     NRSZUANQ-40278    NRSZUANQ-46183
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdInAct1
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves prd by prd code 'AdInAct1'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user updates debit note with fixed data
    Then expected return status code 200

3 - Unable to update DN by adding blocked product and get 404 Not Found
    [Documentation]    Unable to update debit note using block product
    [Tags]    distadm    9.1.1     NRSZUANQ-40281
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    ${uom_details}=  create dictionary
    ...   UOM=PC1
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdeBlo1
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user updates debit note with fixed data
    Then expected return status code 404

4 - Able to update Debit Note and verify taxable amount
    [Documentation]    Able to update debit note with tax correctly
    [Tags]    distadm    9.1.1     NRSZUANQ-42293
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdeCP001
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    Given user retrieves token access as ${user_role}
    When user updates debit note with fixed data
    Then expected return status code 200
