*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteProduct/CreditNoteProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteProduct/CreditNoteProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

*** Test Cases ***
1 - Able to put non prime credit note and return 200
    [Documentation]    Able to put non credit note
    [Tags]    distadm    9.1     NRSZUANQ-31700    BUG:NRSZUANQ-53079
    [Setup]      run keywords
    ${CnDetailsPre}=    create dictionary
    ...    route=Rchoon
    ...    routeplan=CY0000000417
    ...    customer=CT0000001074
    ...    reasontype=Return - Good Stock
    ...    productPrime=JunPrimeTaxableProdu
    ...    productNPrime=AdNP1001
    ...    distributor=DistEgg
    user creates Non-Prime credit note as prerequisite
    ${cn_update_header_details}=   create dictionary
    ...    REMARK=EDITED
    ${cn_update_body_details}=     create dictionary
    ...    PRD_QTY=${25}
    Given user retrieves token access as ${user_role}
    When user edits credit note with fixed data
    Then expected return status code 200

2 - Unable to put credit note with hq acess and return 403
    [Documentation]    Unable to put credit note with hqadm
    [Tags]    hqadm    9.1     NRSZUANQ-31705
    [Setup]      run keywords
    ${CnDetailsPre}=    create dictionary
    ...    route=Rchoon
    ...    routeplan=CY0000000417
    ...    customer=CT0000001074
    ...    reasontype=Return - Good Stock
    ...    productPrime=JunPrimeTaxableProdu
    ...    productNPrime=AdNP1001
    ...    distributor=DistEgg
    user creates Non-Prime credit note as prerequisite
    ${cn_update_header_details}=    create dictionary
    ...    REMARK=TRYING TO EDIT
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user edits credit note with random data
    Then expected return status code 403

3 - Unable to update CN by adding product which not in distributor product sector and get 404 Not Found
    [Documentation]    Able to update credit note quantity for product which not assigned at product sector
    [Tags]     distadm    9.1.1   NRSZUANQ-40188    prdSector
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'A1001'
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    STATUS=P
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    When user retrieves prd by prd code 'AdActPS'
    Then user unassigned product sector
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdActPS' with uom 'PC1:3'
    And user edits credit note with random data
    Then expected return status code 404
    When user retrieves token access as hqadm
    Then user revert to previous setting

4 - Able to update CN by adding inactive product and get 200 OK
    [Documentation]    Able to update credit note quantity for inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40195
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'PRDInc'
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    STATUS=P
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'PRDInc' with uom 'EA:3'
    And user edits credit note with random data
    Then expected return status code 200

5 - Unable to update CN by adding blocked product and get 404 Not Found
    [Documentation]    Able to update credit note quantity for blocked product
    [Tags]     distadm    9.1.1   NRSZUANQ-40197
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'A1001'
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    STATUS=P
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    And user edits credit note with random data
    Then expected return status code 404

6 - Able to update Credit Note and verify taxable amount
    [Documentation]    Able to update Credit Note and verify tax
    [Tags]     distadm    9.1.1   NRSZUANQ-42292
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ${cn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:2'
    And user creates credit note with fixed data
    Then expected return status code 200
    When When user intends to insert product 'AdPrdTNet' with uom 'PC1:2'
    And user edits credit note with random data
    Then expected return status code 200
