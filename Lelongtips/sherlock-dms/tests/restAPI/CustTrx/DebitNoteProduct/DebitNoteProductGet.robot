*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteProduct/DebitNoteProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/DebitNoteProduct/DebitNoteProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py

Test Setup     run keywords
...    user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user retrieves cust by using name 'CXTESTTAX'
...    AND       user retrieves token access as distadm
...    AND       user gets reason by using code 'JunReasonTypeCode' and 'DN'

*** Test Cases ***
1 - Able to GET DN with product which not in distributor product sector and get 200 OK
    [Documentation]    Able to get debit note with product which not assigned at product sector
    [Tags]     distadm    9.1.1   NRSZUANQ-40287
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdActPS'
    And user assigned product sector using fixed data
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
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201
    And user unassigned product sector using fixed data
    Given user retrieves token access as ${user_role}
    When user retrieves debit note by id
    Then expected return status code 200

2 - Able to GET DN with inactive product and get 200 OK
    [Documentation]    Able to get debit note with inactive product
    [Tags]      distadm    9.1.1   NRSZUANQ-40288     BUG:NRSZUANQ-46183
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    ${uom_details}=  create dictionary
    ...   UOM=PCK
    ...   QTY=1
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=PRDInc
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user retrieves debit note by id
    Then expected return status code 200

3 - Able to GET DN with blocked product and get 200 OK
    [Documentation]    Able to get debit note with blocked product
    [Tags]      distadm    9.1.1   NRSZUANQ-40289      test
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdBlock'
    And user updates product with fixed data
    Then expected return status code 200
    ${uom_details}=  create dictionary
    ...   UOM=PCK
    ...   QTY=1
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdBlock
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${dn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user creates debit note with fixed data
    Then expected return status code 201
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user retrieves debit note by id
    Then expected return status code 200

4 - Able to retrieve Debit Note and verify taxable amount
    [Documentation]    Able to retrieve debit note and verify tax
    [Tags]       distadm    9.1.1    NRSZUANQ-42293
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
    When user creates debit note with fixed data
    Then expected return status code 201
    When user retrieves debit note by id
    Then expected return status code 200
