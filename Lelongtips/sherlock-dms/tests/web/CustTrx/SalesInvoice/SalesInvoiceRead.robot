*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceOverdueInv.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceViewPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

*** Test Cases ***
1 - Verify Principal default to Prime in SalesInvoice when Multi Principal = On
    [Documentation]    Verify SalesInvoice having Principal = Prime when multi principal = On
    [Tags]     distadm    9.1   NRSZUANQ-31525
    #Switches off multi principal first to check if principal column showing
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
    Then user verify invoice defaults to prime

2 - Verify Principal not displaying in SalesInvoice when Multi Principal = Off
    [Documentation]    Verify SalesInvoice not having Principal field when multi principal = Off
    [Tags]     distadm    9.1   NRSZUANQ-31524
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
    Then principal field not displaying in invoice
    Then principal column not visible in invoice listing
    And user switches On multi principal

3 - Able to view existing product which not in distributor product sector
    [Documentation]    Able to view Invoice using product which not assigned at product sector
    [Tags]     distadm    9.1.1   NRSZUANQ-40042     NRSZUANQ-40228   NRSZUANQ-41321
    [Teardown]  run keywords
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user gets distributor by using code 'DistEgg'
    Then user assigned product sector using fixed data
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdAct1
    ...    productUom=PC1:2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    Given user retrieves token access as hqadm
    When user unassigned product sector using fixed data
    And user selects invoice to edit
    Then product populated in details correctly

4 - Able to view existing product which is inactive
    [Documentation]    Able to view Invoice using inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40055   NRSZUANQ-41322
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=PRDInc
    ...    productUom=EA:2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    When user selects invoice to edit
    Then product populated in details correctly

5 - Able to view blocked product
    [Documentation]    Able to view Invoice using blocked product
    [Tags]     distadm    9.1.1   NRSZUANQ-40060   NRSZUANQ-41323
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdeBlo1
    ...    productUom=PC1:2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    When user selects invoice to edit
    Then product populated in details correctly

6 - Able to view invoice and validate header being disabled
    [Documentation]    Able to view Invoice and validate header being disabled
    [Tags]     distadm    9.0
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=WHAd2
    ...    product=A1002
    ...    productUom=EA:2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    When user selects invoice to view
    Then validates sales invoice header disabled

7 - Able to select Sampling Invoice to view
    [Documentation]    Able to select Sampling Invoice view
    [Tags]     distadm    9.3
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
    And SalesInvoicePost.user creates invoice with fixed data
    Then expected return status code 200
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user selects invoice to view
    Then validates sales invoice header disabled

#8 - Able to select Combine Invoice to view
#    [Documentation]    Able to select Sampling Invoice view
#    [Tags]    distadm    9.3     test
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
#    And user retrieves token access as ${user_role}
#    When user retrieves valid sampling program by customer
#    Then expected return status code 200
#   ${prdType}=    create dictionary
#    ...    PRD_SLSTYPE=P
#    When user intends to insert product 'AdePP1' with uom 'EA:5'
#    ${prdType}=    create dictionary
#    ...    PRD_SLSTYPE=S
#    When user intends to insert product 'AdePP1' with uom 'EA:5'
#   And SalesInvoicePost.user creates invoice with fixed data
#    Then expected return status code 200
#    When user open browser and logins using user role ${user_role}
#    And user navigates to menu Customer Transaction | Sales Invoice
#    And user selects invoice to view
#    Then validates sales invoice header disabled

#9 - Validate Apply Promo is enabled for Selling | Combine Edit mode
#    [Documentation]    Validate Apply Promo is enabled for Selling | Combine Edit mode
#    [Tags]     distadm    9.3
#    [Setup]      run keywords
#    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
#    ${fixedData}=    create dictionary
#    ...    PRIME_FLAG=PRIME
#    ...    INV_CUST=CXTESTTAX
#    ...    INV_ROUTE=Rchoon
#    ...    INV_WH=CCCC
#    ${invType}=    create dictionary
#    ...    INVOICE_TXNTYPE=P
#    ${prdType}=    create dictionary
#    ...    PRD_SLSTYPE=P
#    ${AppSetupDetails}=    create dictionary
#    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
#    Given user retrieves details of application setup
#    And user updates app setup details using fixed data
#    And user retrieves token access as ${user_role}
#    When user retrieves valid sampling program by customer
#    Then expected return status code 200
#    When user intends to insert product 'AdePP1' with uom 'EA:5'
#    And SalesInvoicePost.user creates invoice with fixed data
#    Then expected return status code 200
#    When user open browser and logins using user role ${user_role}
#    And user navigates to menu Customer Transaction | Sales Invoice
#    And user selects invoice to view
#    Then validates sales invoice header disabled

10 - Validate Apply Promo is disabled for Sampling Edit mode
    [Documentation]    Validate Apply Promo is disabled for Sampling Edit mode
    [Tags]     distadm    9.3
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
    And SalesInvoicePost.user creates invoice with fixed data
    Then expected return status code 200
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user selects invoice to view
    Then SalesInvoiceViewPage.validate Apply Promo button is disabled

11 - Validate Product Type toggle is disabled in Edit and View mode
    [Documentation]    Validate Product Type is disabled in edit/view mode
    [Tags]     distadm    9.3
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
    And SalesInvoicePost.user creates invoice with fixed data
    Then expected return status code 200
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user selects invoice to view
    Then validate the product types are disabled

12 - Able to view customer group discount on created invoice
    [Documentation]    Validate customer group discount is shown on sales invoice edit
    [Tags]     distadm    9.3
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=Joy Groceria
    ...    warehouse=CCCC
    ...    product=AdPrdTNet
    ...    productUom=PC3:1
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy Groceria
    ...    PROD_CD=AdPrdTNet
    Given user navigates to menu Customer Transaction | Sales Invoice
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When SalesInvoiceAddPage.user creates invoice with fixed data
    And user verify customer group discount on sales invoice product level
    Then sales order created successfully with message 'Record created'
    And user filter listing page with customer name
    When user opens created sales invoice
    Then user verify customer group discount on sales invoice product level

13 - Unable add more product quantity on sales invoice after its created
    [Documentation]    Unable add more product quantity on sales invoice after its created
    [Tags]     distadm    9.3
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=Joy Groceria
    ...    warehouse=CCCC
    ...    product=AdPrdTNet
    ...    productUom=PC3:1
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy Groceria
    ...    PROD_CD=AdPrdTNet
    Given user navigates to menu Customer Transaction | Sales Invoice
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When SalesInvoiceAddPage.user creates invoice with fixed data
    And user verify customer group discount on sales invoice footer level
    Then sales order created successfully with message 'Record created'
    And user filter listing page with customer name
    When user opens created sales invoice
    Then verify unable to edit product details




