*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePut.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderProcess.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

*** Test Cases ***
1 - Able to update Invoice and return 200
    [Documentation]    Able to update Invoice successfully
    [Tags]    distadm    9.1
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    When user updates invoice with random data
    Then expected return status code 200

2 - Able to update INV quantity for product which not in distributor product sector and get 200 OK
    [Documentation]    Able to update Invoice quantity for product which not assigned at product sector
    [Tags]      distadm    9.1.1   NRSZUANQ-40088    NRSZUANQ-40251
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    And user gets distributor by using code 'DistEgg'
    Then user assigned product sector using fixed data
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=WHAUB
    ...    shipTo=CXTESTTAX
    ...    product=AdActPS
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    When user post fixed sales order as prerequisite
    And user process the sales order
    Then expected return status code 202
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as hqadm
    When user unassigned single product sector
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdActPS' with uom 'PC1:2'
    And user updates invoice with fixed data
    Then expected return status code 200
    When user retrieves token access as hqadm
    Then user revert to previous setting

3 - Able to update INV quantity for inactive product and get 200 OK
    [Documentation]    Able to update Invoice quantity for inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40089
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=WHAUB
    ...    shipTo=CXTESTTAX
    ...    product=AdeBlo1
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user post fixed sales order as prerequisite
    And user process the sales order
    Then expected return status code 202
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    When user updates invoice with random data
    Then expected return status code 200

4 - Able to update INV quantity for blocked product and get 200 OK
    [Documentation]    Able to update Invoice quantity for blocked product
    [Tags]     distadm    9.1.1   NRSZUANQ-40090
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=WHAUB
    ...    shipTo=CXTESTTAX
    ...    product=AdeBlo1
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    When user post fixed sales order as prerequisite
    And user process the sales order
    Then expected return status code 202
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    set test variable    ${user_role}       hqadm
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    set test variable    ${user_role}       distadm
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    When user updates invoice with random data
    Then expected return status code 200
