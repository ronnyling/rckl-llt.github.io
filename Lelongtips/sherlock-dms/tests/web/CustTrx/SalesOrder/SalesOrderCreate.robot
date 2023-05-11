*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/TaxationPut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

*** Test Cases ***
1 - Able to Create Sales Order without promotion using given data
    [Documentation]    Able to create Sales Order without applying promotion by using given data
    [Tags]     distadm     9.0    NRSUANQ-33902
    ${fixedData}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    ...    sellingPrice=30.00
    ...    gross=540.00
    ...    customerDisc=27.00
    ...    taxAmt=32.40
    ...    netAmt=545.40
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

2 - Able to Create Sales Order without promotion using random data
    [Documentation]    Able to create Sales Order without applying promotion by using random generated data
    [Tags]     distadm  9.0   NRSUANQ-33902
    ${fixedData}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=random
    ...    productUom=random
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with random data
    Then sales order created successfully with message 'Record created'

3 - Verify Principal default to Prime in Sales Order when Multi Principal = On
    [Documentation]    Verify Sales Order havinng Principal = Prime when multi principal = On
    [Tags]     distadm    9.1   NRSZUANQ-30033
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Order
    Then principal field displaying in sales order

4 - Verify Principal not displaying in Sales Order when Multi Principal = Off
    [Documentation]    Verify Sales Order not having Principal field when multi principal = Off
    [Tags]     distadm    9.1   NRSZUANQ-30034
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Sales Order
    Then principal field not displaying in sales order
    And user switches On multi principal

5 - Verify Principal set to Prime and warehouse only have Prime Warehouse
    [Documentation]    Verify Sales Order Warehouse only have prime record when principal = prime
    [Tags]     distadm    9.1   NRSZUANQ-30035    NRSZUANQ-30037
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=random
    ...    productUom=random
     set test variable     &{fixedData}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

6 - Verify Principal set to Non-Prime and warehouse only have Non-Prime Warehouse
    [Documentation]    Verify Sales Order Warehouse only have non-prime record when principal = non-prime
    [Tags]     distadm    9.1   NRSZUANQ-30036   NRSZUANQ-30038
    ${fixedData}=    create dictionary
    ...    principal=Non-Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=Tesla
    ...    product=random
    ...    productUom=random
     set test variable     &{fixedData}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

7 - Verify save button disabled when new product added
    [Documentation]    Verify save button disabled when new product added
    [Tags]     distadm    9.1   NRSZUANQ-32289
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=ProdAde1
    ...    productUom=PC:1
    Given user navigates to menu Customer Transaction | Sales Order
    And user creates sales order and apply promo
    Then save button showing enabled
    When user adds random product
    Then save button showing disabled

8 - Verify save button disabled when any product removed
    [Documentation]    Verify save button disabled when new product added
    [Tags]     distadm    9.1   NRSZUANQ-33290
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=ProdAde1
    ...    productUom=PC:1
    Given user navigates to menu Customer Transaction | Sales Order
    And user creates sales order and apply promo
    Then save button showing enabled
    When user removes random product
    Then save button showing disabled

9 - Verify save button disabled when product quantity changed
    [Documentation]    Verify save button disabled when new product added
    [Tags]     distadm    9.1   NRSZUANQ-33291
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    ...    product=ProdAde1
    ...    productUom=PC:1
    Given user navigates to menu Customer Transaction | Sales Order
    And user creates sales order and apply promo
    Then save button showing enabled
    When user changes random product quantity
    Then save button showing disabled

10 - Validate $ icon only show in header
    [Documentation]   Validate the currency is removed from product details value fields
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    Given user navigates to menu Customer Transaction | Sales Order
    When user intends to insert product 'ProdAde1' with uom 'PC:4,PCK:2'
    And user inserts sales order with fixed data
    Then validate dollar sign is removed from details

11 - Able to calculate tax and store correctly (Tax on Net) when create sales order
    [Documentation]    Able to create Sales Order with tax on net
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdPrdTNet
    ...    productUom=PC1:2
    ...    sellingPrice=86.21
    ...    gross=28.74
    ...    customerDisc=1.44
    ...    taxAmt=0.55
    ...    netAmt=27.85
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

12 - Able to calculate tax and store correctly (discount impact on customer) when create sales order
    [Documentation]    Able to create Sales Order with tax on gross and with discount impact on customer discount
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
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
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdPrdTGross
    ...    productUom=PC1:2
    ...    sellingPrice=31.73
    ...    gross=63.46
    ...    customerDisc=3.17
    ...    taxAmt=1.90
    ...    netAmt=62.19
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

13 - Able to calculate tax and store correctly (discount impact on promo) when create sales order
    [Documentation]    Able to create Sales Order with tax on gross and with discount impact on promo discount
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
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
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdPrdTGross
    ...    productUom=PC1:5
    ...    sellingPrice=31.73
    ...    gross=158.65
    ...    customerDisc=7.83
    ...    taxAmt=4.70
    ...    netAmt=153.52
    ...    promo=PromoT1
    ...    promoAmt=2
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

14 - Able to calculate tax and store correctly (discount impact on customer and promo) when create sales order
    [Documentation]    Able to create Sales Order with tax with discount impact on promo discount & cust discount
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
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
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdPrdTGross
    ...    productUom=PC1:5
    ...    sellingPrice=31.73
    ...    gross=158.65
    ...    customerDisc=7.83
    ...    taxAmt=4.46
    ...    netAmt=153.28
    ...    promo=PromoT1
    ...    promoAmt=2
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

15 - Able to calculate tax and store correctly (Tax on Tax) when create sales order
    [Documentation]    Able to create Sales Order with tax on tax
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdPrdTTax
    ...    productUom=PC1:3
    ...    sellingPrice=62.80
    ...    gross=12.56
    ...    customerDisc=0.63
    ...    taxAmt=0.52
    ...    netAmt=12.45
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'

16 - Validate product index will be correct when sales order have multiple product
    [Documentation]    Validate the product index saved is correct when there are multiple product
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    Given user navigates to menu Customer Transaction | Sales Order
    When user intends to insert product 'AdePrd4' with uom 'PC:3'
    And user intends to insert product 'ProdAde1' with uom 'PC:2'
    And user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'
    And verifies product index saved in order database correctly

17 - Validate tax amt return from tax engine is correct when create sales order
    [Documentation]    Validate the tax engine is save correctly after the order creation
    [Tags]     distadm     9.1.1    NRSZUANQ-42296
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    warehouse=CCCC
    ...    product=AdPrdTNet
    ...    productUom=PC1:2
    ...    sellingPrice=86.21
    ...    gross=28.74
    ...    customerDisc=1.44
    ...    taxAmt=0.55
    ...    netAmt=27.85
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'
    And verifies product tax saved in order database correctly

18 - Able to Create Sampling type Sales Order using given data
    [Documentation]    Able to create Sampling type Sales Order with given data
    [Tags]     distadm     9.3
    [Setup]  user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
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
    And user navigates to menu Customer Transaction | Sales Order
    And user creates sales order with sampling data
    Then sales order created successfully with message 'Record created'

19 - Able to create Combine type Sales Order using given data
    [Documentation]    Able to create Combine type Sales Order with given data
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    [Teardown]  run keywords
    ...    user updates app setup details using fixed data
    ...    AND     user logouts and closes browser
    ${fixedData}=    create dictionary
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
    And user navigates to menu Customer Transaction | Sales Order
    And user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${False}

20 - Unable to save Combine Sales Order without selling product
    [Documentation]    Unable to save combine type sales order without selling product
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    [Teardown]  run keywords
    ...    user updates app setup details using fixed data
    ...    AND     user logouts and closes browser
    ${fixedData}=    create dictionary
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
    And user navigates to menu Customer Transaction | Sales Order
    And user inserts sales order with fixed data
    Then validate unable to save the transaction

21 - Unable to select two product types when Combine = No
    [Documentation]    Unable to select two both selling and sampling order when Combine Selling / Sampling = No
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
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
    And user navigates to menu Customer Transaction | Sales Order
    And user inserts sales order with fixed data
    Then validate unable to select different product type

22 - Validate product type selection is only Selling for Non Prime order
    [Documentation]    Validate product type selection is default to Selling on Non Prime order
    [Tags]     distadm     9.3
    [Setup]  run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
    ${fixedData}=    create dictionary
    ...    principal=Non-Prime
    ...    route=REgg02
    ...    customer=CXTESTTAX
    ...    warehouse=Tesla
    ...    product=NPCollection01
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
    And user navigates to menu Customer Transaction | Sales Order
    And user inserts sales order with fixed data
    Then validate unable to select different product type

23 - Able to create sales order with customer group discount
    [Documentation]    Able to create sales order with customer group discount
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Joy Groceria
    ...    warehouse=CCCC
    ...    product=AdePP1
    ...    productUom=EA:2
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy Groceria
    ...    PROD_CD=AdePP1
    Given user navigates to menu Customer Transaction | Sales Order
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user creates sales order with fixed data
    And user click save
    Then sales order created successfully with message 'Record created'

24 - Verify the customer group discount amount on product level
    [Documentation]    Verify the customer group discount amount on product level
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Joy Groceria
    ...    warehouse=CCCC
    ...    product=AdePP1
    ...    productUom=EA:2
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy Groceria
    ...    PROD_CD=AdePP1
    Given user navigates to menu Customer Transaction | Sales Order
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user creates sales order with fixed data
    And user verify cust group discount on product level
    Then sales order created successfully with message 'Record created'

25 - Validate customer group discount is displayed correctly on footer level
    [Documentation]    Verify the customer group discount amount on footer level
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Joy Groceria
    ...    warehouse=CCCC
    ...    product=AdePP1
    ...    productUom=EA:2
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy Groceria
    ...    PROD_CD=AdePP1
    Given user navigates to menu Customer Transaction | Sales Order
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user creates sales order with fixed data
    And user verify cust group discount on footer level
    Then sales order created successfully with message 'Record created'

26 - Validate no customer group discount is displayed when there is no matching setup
    [Documentation]    Validate no customer group discount is displayed when there is no matching setup
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=ShamCust
    ...    warehouse=CCCC
    ...    product=ShamFNN
    ...    productUom=SHM:1
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy ShamCust
    ...    PROD_CD=ShamFNN
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order with fixed data
    And user verify customer group discount not applied
    And user click save
    Then sales order created successfully with message 'Record created'
