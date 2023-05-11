*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteProduct/DebitNoteProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

Test Setup       run keywords
...    user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets cust by using code 'CT0000001549'
...    AND       user gets reason by using code 'JunReasonTypeCode' and 'DN'

*** Test Cases ***
1 - Able to post prime debit note and return 200
    [Documentation]    Able to post prime debit note
    [Tags]    distadm    9.1
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=A1001
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    set test variable     ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves prd by prd code 'A1001'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable     ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201

2 - Able to post non prime debit note and return 200
    [Documentation]    Able to post non prime debit note
    [Tags]    distadm    9.111
    ${uom_details}=  create dictionary
    ...   UOM=CS
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=testNp123
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=NON_PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201

3 - Unable to POST DN with product which not in distributor product sector and get 404 Not Found
    [Documentation]    Unable to post debit note using product which not assign to product sector
    [Tags]    distadm    9.1.1    NRSZUANQ-40265    prdSector
    [Teardown]  run keywords
    ...    user assigned product sector using fixed data
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
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    When user retrieves prd by prd code 'AdActPS'
    And user unassigned product sector using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 404
    When user retrieves token access as hqadm
    Then user revert to previous setting

4 - Able to POST DN with inactive product and get 200 OK
    [Documentation]    Able to post debit note using inactive product
    [Tags]    distadm    9.1.1     NRSZUANQ-40267   NRSZUANQ-40290
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=2
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
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdInAct1'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201

5 - Unable to POST DN with blocked product and get 404 Not Found
    [Documentation]    Unable to post debit note using block product
    [Tags]    distadm    9.1.1     NRSZUANQ-40275
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
    When user creates debit note with fixed data
    Then expected return status code 404

#----------------------------TAX------------------------------------#
6 - Able to create Debit Note with tax on gross and verify tax details
    [Documentation]    Able to post prime debit note with tax on gross
    [Tags]    distadm    9.1.1    NRSZUANQ-42293
    ${uom_details}=  create dictionary
    ...   UOM=PC1
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdPrdTGross
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201

7 - Able to create Debit Note with tax on net and verify tax details
    [Documentation]    Able to post prime debit note with tax on net
    [Tags]    distadm    9.1.1    NRSZUANQ-42293    adtax
    ${uom_details}=  create dictionary
    ...   UOM=EA
    ...   QTY=1
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
    When user creates debit note with fixed data
    Then expected return status code 201
