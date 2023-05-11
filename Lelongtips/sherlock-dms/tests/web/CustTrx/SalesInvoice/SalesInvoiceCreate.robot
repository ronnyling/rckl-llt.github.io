*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceOverdueInv.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/TaxationPut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

*** Test Cases ***

1 - Validate non-prime product is listed in product selection when principal flag = non-prime
    [Documentation]    Able to create Invoice without applying promotion by using given data
    [Tags]     distadm  9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Invoice
     ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=TWOLVLTAX
    ...    warehouse=CCCC
     set test variable     &{InvDetails}
    When user verifies non-prime product is listed in product selection when invoice is non-prime transaction
    Then verified only non-prime product are listed

2 - Validate Prime product is listed when invoice principal = prime
    [Documentation]    Able to create Invoice without applying promotion by using given data
    [Tags]     distadm  9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Invoice
      ${InvDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    route=Rchoon
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
     set test variable     &{InvDetails}
    When user verifies prime product is listed in product selection when invoice is prime transaction
    Then verified only prime product are listed

3 - Verify when multi principal is turned on pricipal flag will be display and default to prime
    [Documentation]    Able to create SalesInvoice without applying promotion by using given data
    [Tags]     distadm  9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
    Then principal field displaying in SalesInvoice

4 - Verify when multi principal is turned off pricipal flag will be hidden
    [Documentation]
    [Tags]     distadm  9.1
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
    Then principal field not displaying in SalesInvoice

5 - Verify when multi principal is turned on prime warehouse will apper when pricipal flag = prime
    [Documentation]    Able to create SalesInvoice without applying promotion by using given data
    [Tags]     distadm  9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
    Then verified only PRIME warehouse will appear when PRIME invoice is selected

6 - Verify when multi principal is turned on non prime warehouse will apper when pricipal flag = non prime
    [Documentation]    Able to create SalesInvoice without applying promotion by using given data
    [Tags]     distadm  9.1
    Given user switches On multi principal
    ${InvDetails}=    create dictionary
    ...    principal=Non-Prime
     set test variable     &{InvDetails}
    When user navigates to menu Customer Transaction | Sales Invoice
    Then verified only NON_PRIME warehouse will appear when NON_PRIME invoice is selected

7 - Verify Credit Limit and available balance able to display when principal flag = prime
    [Documentation]    Able to create SalesInvoice without applying promotion by using given data
    [Tags]     distadm  9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
     ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=CCCC
     set test variable     &{InvDetails}
    Then verified credit limit and available balance is displaying

8 - Verify Credit Limit and available balance are not displaying when principal flag = non prime
    [Documentation]    Able to create Invoice without applying promotion by using given data
    [Tags]     distadm  9.1    NRSZUANQ-31729
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Invoice
      ${InvDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=UMNPWHCC
     set test variable     &{InvDetails}
    Then verified credit limit and available balance is not displaying

9 - Able to Create SalesInvoice without promotion using given data
    [Documentation]    Able to create SalesInvoice
    [Tags]     distadm  9.1
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
    ...    product=PRDMULTINET
    ...    productUom=ABC:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'

10 - Able to Create non-prime SalesInvoice with tax first level on gross, second level on level 1 tax
    [Documentation]    verify tax calculation with with tax first level on gross, second level on level 1 tax
    [Tags]     distadm  9.1   NRSZUANQ-32678
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
    ...    product=TAXMULTIAPPLY
    ...    productUom=ABC:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'


11 - Able to Create non-prime SalesInvoice with tax first level on gross, second level on gross + tax on tax
    [Documentation]    verify tax calculation with tax first level on gross, second level on gross + tax on tax
    [Tags]     distadm  9.1
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
    ...    product=MultiApplyGross
    ...    productUom=saz:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'

12 - Able to Create non-prime SalesInvoice with correct inventory movement for unmanaged warehouse
    [Documentation]   verify non-prime managed warehouse inventory movement is correct
    [Tags]     distadm  9.1    asdasdqweqwe
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
    ...    product=MultiApplyGross
    ...    productUom=saz:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    And validated inventory movement deducted correctly

13 - Able to Create non-prime SalesInvoice with correct inventory movement for managed warehouse
    [Documentation]    Able to create SalesInvoice
    [Tags]     distadm  9.1    44556677
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=CCNPManageWH
    ...    product=TAXMULTIAPPLY
    ...    productUom=ABC:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    And validated inventory movement deducted correctly

14 - Able to Create non-prime SalesInvoice with correct inventory movement for semi-managed warehouse
    [Documentation]    Able to create SalesInvoice
    [Tags]     distadm  9.1
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=CCNPSemiWHTest
    ...    product=TAXMULTIAPPLY
    ...    productUom=ABC:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'
    And validated inventory movement deducted correctly

15 - Able to Create SalesInvoice with accumulative tax first level on gross, second level on tax 1(Discount Impact ON)
    [Documentation]    verify accumulative tax calculation
    [Tags]     distadm  9.1
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
    ...    product=AccumlativePRd
    ...    productUom=ABC:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user turn on discount impact with Customer Disc
    And user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'

16 - Able to Create SalesInvoice with accumulative tax first level on gross, second level on tax 1(Discount Impact Off)
    [Documentation]    verify accumulative tax calculation
    [Tags]     distadm  9.1
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    warehouse=UMNPWHCC
    ...    product=AccumlativePRd
    ...    productUom=ABC:3
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user turn off discount impact with no disc
    And user creates invoice with fix data
    Then Invoice created successfully with message 'Record created'


17 - Verify save button disabled when new product added
    [Documentation]    Verify save button disabled when new product added
    [Tags]     distadm    9.1   NRSZUANQ-33292
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=AdePrd5
    ...    productUom=EA:1
    ...    cust_disc=5
    ...    cust_disc_unit=percentage
    Given user navigates to menu Customer Transaction | Sales Invoice
    And user creates invoice and apply promo
    Then save button enabled
    When user adds random product
    Then save button disabled

18 - Verify save button disabled when any product removed
    [Documentation]    Verify save button disabled when new product added
    [Tags]     distadm    9.1   NRSZUANQ-33293
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=AdePrd4
    ...    productUom=PC:1
    ...    cust_disc=5
    ...    cust_disc_unit=percentage
    Given user navigates to menu Customer Transaction | Sales Invoice
    And user creates invoice and apply promo
    Then save button enabled
    When user removes random product
    Then save button disabled

19 - Verify save button disabled when product quantity changed
    [Documentation]    Verify save button disabled when new product added
    [Tags]     distadm    9.1   NRSZUANQ-33298
    [Teardown]
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    warehouse=WHAd2
    ...    customer=Vege Tan
    ...    product=random
    ...    productUom=random
    Given user navigates to menu Customer Transaction | Sales Invoice
    And user creates invoice and apply promo
    Then save button enabled
    When user changes random product quantity
    Then save button disabled


20 - Unable to add product which not in distributor product sector
    [Documentation]    Unable to create SalesInvoice using product which not linked to product sector
    [Tags]     distadm     9.1.1    NRSZUANQ-40033
    [Teardown]  run keywords
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user gets distributor by using code 'DistEgg'
    Then user unassigned product sector using fixed data
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdAct1
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user provides invoice header with ${InvDetails}
    Then product not populated in dropdown

21 - Unable to add inactive product
    [Documentation]    Unable to create SalesInvoice using inactive product
    [Tags]     distadm     9.1.1    NRSZUANQ-40044
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    Then user updates product with fixed data
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=PRDInc
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user provides invoice header with ${InvDetails}
    Then product not populated in dropdown

22 - Unable to add blocked product
    [Documentation]    Unable to create SalesInvoice using blocked product
    [Tags]     distadm     9.1.1    NRSZUANQ-40056
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    Then user updates product with fixed data
    ${InvDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdeBlo1
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user provides invoice header with ${InvDetails}
    Then product not populated in dropdown

#-----------------Tax Validation-----------------------------#
23 - Validate $ icon only show in header
    [Documentation]   Validate the $ is removed from product details value fields
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    ${uom_details1}=  create dictionary
    ...   UOM=PCK
    ...   QTY=2
    ${uom_details2}=  create dictionary
    ...   UOM=PC
    ...   QTY=4
    @{uom_list} =  create list
    ...    ${uom_details1}    ${uom_details2}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=ProdAde1
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${InvDetails}=    create dictionary
    ...    PROD_ASS_DETAILS=${prd_list}
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=UnManWH
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    ...    sellingPrice=30.00
    ...    gross=540.00
    ...    customerDisc=27.00
    ...    taxAmt=32.40
    ...    netAmt=545.40
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user inserts invoice with fix data
    Then validate currency sign is removed from details

24 - Able to calculate tax and store correctly (Tax on Net) when create sales invoice
    [Documentation]    Able to create Sales Invoice with tax on net
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=UnManWH
    ...    product=AdPrdTNet
    ...    productUom=PC1:2
    ...    sellingPrice=86.21
    ...    gross=28.74
    ...    customerDisc=1.44
    ...    taxAmt=0.55
    ...    netAmt=27.85
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then invoice created successfully with message 'Record created'

25 - Able to calculate tax and store correctly (discount impact on customer) when create sales invoice
    [Documentation]    Able to create Sales Invoice with tax on gross and with discount impact on customer discount
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    [Setup]    run keywords
    ${AppSetupDetails}=    create dictionary
    ...    DISCOUNT_IMPACT_FOR_TAX_COMPUTATION=${true}
    ...    VAL_DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION=Customer Disc
    user open browser and logins using user role ${user_role}
    user retrieves token access as sysimp
    user retrieves details of application_setup
    user updates app setup taxation details using fixed data
    [Teardown]    run keywords
    ...    user revert to previous setting
    ...    user logouts and closes browser
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=UnManWH
    ...    product=AdPrdTGross
    ...    productUom=PC1:2
    ...    sellingPrice=31.73
    ...    gross=63.46
    ...    customerDisc=3.17
    ...    taxAmt=1.90
    ...    netAmt=62.19
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then invoice created successfully with message 'Record created'

26 - Able to calculate tax and store correctly (discount impact on promo) when create sales invoice
    [Documentation]    Able to create Sales Invoice with tax on gross and with discount impact on promo discount
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    [Setup]    run keywords
    ${AppSetupDetails}=    create dictionary
    ...    DISCOUNT_IMPACT_FOR_TAX_COMPUTATION=${true}
    ...    DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION=Promo Disc
    user retrieves token access as sysimp
    user retrieves details of application setup
    user updates app setup taxation details using fixed data
    user open browser and logins using user role ${user_role}
    [Teardown]    run keywords
    ...    user revert to previous setting
    ...    user logouts and closes browser
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=UnManWH
    ...    product=AdPrdTGross
    ...    productUom=PC1:5
    ...    sellingPrice=31.73
    ...    gross=158.65
    ...    customerDisc=7.83
    ...    taxAmt=4.70
    ...    netAmt=153.52
    ...    promo=PromoT1
    ...    promoAmt=2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then invoice created successfully with message 'Record created'

27 - Able to calculate tax and store correctly (discount impact on customer and promo) when create sales invoice
    [Documentation]    Able to create Sales Invoice with tax with discount impact on promo discount & cust discount
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    [Setup]    run keywords
    ${AppSetupDetails}=    create dictionary
    ...    ENABLE_MULTI_PRINCIPAL=${true}
    ...    DISCOUNT_IMPACT_FOR_TAX_COMPUTATION=${true}
    ...    DISCOUNTS_TO_BE_INCLUDED_FOR_TAX_COMPUTATION=Promo Disc,Customer Disc
    user retrieves token access as sysimp
    user retrieves details of application setup
    user updates app setup details using fixed data
    user switches On multi principal
    user open browser and logins using user role ${user_role}
    [Teardown]    run keywords
    ...    user revert to previous setting
    ...    user logouts and closes browser
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=UnManWH
    ...    product=AdPrdTGross
    ...    productUom=PC1:5
    ...    sellingPrice=31.73
    ...    gross=158.65
    ...    customerDisc=7.83
    ...    taxAmt=4.46
    ...    netAmt=153.28
    ...    promo=PromoT1
    ...    promoAmt=2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then invoice created successfully with message 'Record created'

28 - Able to calculate tax and store correctly (Tax on Tax) when create sales invoice
    [Documentation]    Able to create Sales Invoice with tax on tax
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=UnManWH
    ...    product=AdPrdTTax
    ...    productUom=PC1:3
    ...    sellingPrice=62.80
    ...    gross=12.56
    ...    customerDisc=0.63
    ...    taxAmt=0.52
    ...    netAmt=12.45
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then invoice created successfully with message 'Record created'

29 - Validate product index will be correct when sales invoice have multiple product
    [Documentation]    Validate the product index saved is correct when there are multiple product
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=WHAd2
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user intends to insert product 'AdePrd4' with uom 'PC:3'
    And user intends to insert product 'A1001' with uom 'EA:2'
    And user creates invoice with fix data
    Then invoice created successfully with message 'Record created'
    And verifies product index saved in invoice database correctly

30 - Validate tax amt return from tax engine is correct when create sales invoice
    [Documentation]    Validate the tax engine is save correctly after the invoice created
    [Tags]     distadm     9.1.1    NRSZUANQ-42297
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=UnManWH
    ...    product=AdPrdTTax
    ...    productUom=PC1:3
    ...    sellingPrice=62.80
    ...    gross=12.56
    ...    customerDisc=0.63
    ...    taxAmt=0.52
    ...    netAmt=12.45
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice with fix data
    Then invoice created successfully with message 'Record created'
    And verifies product tax saved in invoice database correctly

31 - Able to Create Sampling type Invoice using given data
    [Documentation]    Able to create Sampling type Invoice with given data
    [Tags]     distadm     9.3
    [Setup]  user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdePP1
    ...    productUom=EA:1
    ...    productType=Sampling
    ...    sellingPrice=0.00
    ...    gross=0.00
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=0.00
    ${txnDetails}=    create dictionary
    ...    txnType=P
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user creates invoice with sampling data
    Then sales invoice created successfully with message 'Record created'

32 - Able to create Combine type Sales Invoice using given data
    [Documentation]    Able to create Combine type Sales Invoice with given data
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    [Teardown]  run keywords
    ...    user updates app setup details using fixed data
    ...    AND     user logouts and closes browser
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdePP1,AdePP2
    ...    productUom=EA:1,EA:1
    ...    productType=Sampling,Selling
    ...    sellingPrice=0.00
    ...    gross=5.50
    ...    customerDisc=0.80
    ...    taxAmt=0.17
    ...    netAmt=5.00
    ${txnDetails}=    create dictionary
    ...    txnType=S
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${True}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user creates invoice with fixed data
    Then sales invoice created successfully with message 'Record created'
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}

33 - Unable to save Combine Sales Invoice without selling product
    [Documentation]    Unable to save combine type sales invoice without selling product
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    [Teardown]  run keywords
    ...    user updates app setup details using fixed data
    ...    AND     user logouts and closes browser
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdePP1
    ...    productUom=EA:1
    ...    productType=Sampling
    ...    sellingPrice=0.00
    ...    gross=5.50
    ...    customerDisc=0.80
    ...    taxAmt=0.17
    ...    netAmt=5.00
    ${txnDetails}=    create dictionary
    ...    txnType=S
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${True}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user inserts invoice with fixed data
    Then validate unable to save the transaction

34 - Unable to select two product types when Combine = No
    [Documentation]    Unable to select two both selling and sampling invoice when Combine Selling / Sampling = No
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${InvDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdePP1
    ...    productUom=EA:1
    ...    productType=Sampling
    ...    sellingPrice=0.00
    ...    gross=0.00
    ...    customerDisc=0.80
    ...    taxAmt=0.00
    ...    netAmt=0.00
    ${txnDetails}=    create dictionary
    ...    txnType=P
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user inserts invoice with fixed data
    Then validate unable to select different product type

35 - Validate product type selection is only Selling for Non Prime invoice
    [Documentation]    Validate product type selection is default to Selling on Non Prime invoice
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${InvDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    customer=TWOLVLTAX
    ...    route=Rchoon
    ...    warehouse=UMNPWHCC
    ...    product=BenMakPCD19
    ...    productUom=EA:1
    ...    productType=Selling
    ${txnDetails}=    create dictionary
    ...    txnType=S
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}
    Given user switches On multi principal
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    When user open browser and logins using user role ${user_role}
    And user navigates to menu Customer Transaction | Sales Invoice
    And user inserts invoice with fixed data
    Then validate unable to select different product type

36 - Create sales invoice with customer group discount
    [Documentation]    Create sales invoice with customer group discount
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
    When user creates invoice with fixed data
    And user click save invoice
    Then sales invoice created successfully with message 'Record created'


37 - Verify customer group discount applied on sales order product level
    [Documentation]    Verify customer group discount applied on sales order product level
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
    When user creates invoice with fixed data
    And user verify customer group discount on sales invoice product level
    Then sales invoice created successfully with message 'Record created'

38 - Verify customer group discount applied on sales order footer level
    [Documentation]    Verify customer group discount applied on sales order footer level
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
    When user creates invoice with fixed data
    And user verify customer group discount on sales invoice footer level
    Then sales invoice created successfully with message 'Record created'
