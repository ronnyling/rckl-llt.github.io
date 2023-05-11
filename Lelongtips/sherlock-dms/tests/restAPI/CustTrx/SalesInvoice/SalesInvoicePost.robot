*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

*** Test Cases ***
1 - Able to post prime Invoice and return 200
    [Documentation]    Able to post prime Invoice
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

2 - Unable to POST INV with product which not in distributor product sector and get 404 Not Found
    [Documentation]    Unable to post Invoice using product which not assigned at product sector
    [Tags]     distadm    9.1.1   NRSZUANQ-40084    prdSector
    [Setup]        run keywords
    ...    user retrieves token access as distadm
    ...    user gets distributor by using code 'DistEgg'
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    Given user retrieves token access as hqadm
    Then user unassigned product sector using fixed data
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdActPS' with uom 'PC1:2'
    When user creates invoice with fixed data
    Then expected return status code 404
    When user retrieves token access as hqadm
    Then user revert to previous setting

3 - Unable to POST INV with inactive product and get 404 Not Found
    [Documentation]    Unable to post Invoice using inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40085
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'PRDInc' with uom 'EA:3'
    When user creates invoice with fixed data
    Then expected return status code 404

4 - Unable to POST INV with blocked product and get 404 Not Found
    [Documentation]    Unable to post Invoice using blocked product
    [Tags]      distadm    9.1.1   NRSZUANQ-40086
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    When user creates invoice with fixed data
    Then expected return status code 404

5 - Able to post Invoice and validate DELIVERY_STATUS will default to O which is Open status
    [Documentation]    Able to post prime Invoice
    [Tags]    distadm    9.2   NRSZUANQ-45566
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    And validated delivery status column is added and default to open status

6 - Able to post Sampling Invoice and return 200
    [Documentation]    Able to post Sampling Invoice
    [Tags]    distadm    9.3      test
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${invType}=    create dictionary
    ...    INVOICE_TXNTYPE=P
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=P
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates invoice with fixed data
    Then expected return status code 200

#7 - Able to post Combine Invoice and return 200
#    [Documentation]    Able to post Sampling Invoice
#    [Tags]    distadm    9.3     test   sampling
#    [Setup]      run keywords
#    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
#    ${fixedData}=    create dictionary
#    ...    PRIME_FLAG=PRIME
#    ...    INV_CUST=CXTESTTAX
#    ...    INV_ROUTE=Rchoon
#    ...    INV_WH=CCCC
#    ${invType}=    create dictionary
#    ...    INVOICE_TXNTYPE=S
#    ${AppSetupDetails}=    create dictionary
#    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${True}
#    Given user retrieves details of application setup
#    And user updates app setup details using fixed data
#    Then expected return status code 200
#    And user retrieves token access as ${user_role}
#    When user retrieves valid sampling program by customer
#    Then expected return status code 200
#   ${prdType}=    create dictionary
#    ...    PRD_SLSTYPE=P
#    When user intends to insert product 'AdePP1' with uom 'EA:5'
#    ${prdType}=    create dictionary
#    ...    PRD_SLSTYPE=S
#    When user intends to insert product 'AdePP1' with uom 'EA:5'
#    And user creates invoice with fixed data
#    Then expected return status code 200

8 - Unable to POST for Invoice with Sampling product when Sampling = Off
    [Documentation]    Unable to post invoice containing sampling product when sampling = off
    [Tags]    distadm    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${invType}=    create dictionary
    ...    INVOICE_TXNTYPE=P
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=P
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    And user sets the feature setup for sampling to off passing with 'SAMPLING' value
    And user creates invoice with fixed data
    Then expected return status code 400

9 - Unable to POST Sales Invoice with invalid sampling product
    [Documentation]    Unable to post invoice containing invalid sampling product
    [Tags]    distadm    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${invType}=    create dictionary
    ...    INVOICE_TXNTYPE=P
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=P
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'TP001' with uom 'BT:3'
    And user creates invoice with fixed data
    Then expected return status code 404

10 - Unable to POST Sales Invoice with invalid sampling program
    [Documentation]    Unable to post invoice with sampling program
    [Tags]    distadm    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${invType}=    create dictionary
    ...    INVOICE_TXNTYPE=P
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=P
    ${samplingDetails}=    create dictionary
    ...    TYPE=INVALID
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves invalid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates invoice with fixed data
    Then expected return status code 404

11 - Unable to post Sales Invoice using invalid token
    [Documentation]    Unable to post Sampling Invoice
    [Tags]    hqadm    9.3
    [Setup]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${invType}=    create dictionary
    ...    INVOICE_TXNTYPE=P
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=P
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as distadm
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    set test variable      ${user_role}    hqadm
    And user retrieves token access as ${user_role}
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates invoice with fixed data
    Then expected return status code 200

12 - Able to create invoice with customer group disc
    [Documentation]    Able to post invoice with group disc
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdePP1
    Given user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates invoice with fixed data
    Then expected return status code 200