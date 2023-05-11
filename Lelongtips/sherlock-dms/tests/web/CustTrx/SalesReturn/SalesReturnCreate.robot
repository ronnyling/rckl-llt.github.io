*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/web/Config/ReferenceData/ReasonType/ReasonTypeAllPage.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

*** Test Cases ***
1 - Able to Create Sales Return using given data
    [Documentation]    Able to create SalesReturn by using given data
    [Tags]     distadm  9.1    9.2  NRSZUANQ-33460    NRSZUANQ-44311
     ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    reason=GOOD1
    ...    product=ProdAde1
    ...    productUom=PC:2
     set test variable     &{ReturnDetails}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'

2 - Verify Principal default to Prime in Return when Multi Principal = On
    [Documentation]    Verify the principal flag is default to Prime when multi principal = on
    [Tags]     distadm  9.1    NRSZUANQ-33452
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Return
    Then principal field displaying in return

3 - Verify Principal not displaying in SalesReturn when Multi Principal = Off
    [Documentation]    Verify the principal flag is not showing when multi principal = off
    [Tags]     distadm  9.1    NRSZUANQ-33453
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Sales Return
    Then principal field not displaying in return
    And user switches On multi principal

4 - Able to select confirmed prime SalesInvoice only when principal=Prime
    [Documentation]    To validate on confirmed Prime SalesInvoice is showing in listing
    [Tags]     distadm    9.1     NRSZUANQ-33454
    [Setup]     run keywords
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
    ...    status=Invoiced
    ...    customer_code=CT0000001074
    ...    route_code=Rchoon
    set test variable     &{FilterDetails}
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Customer Transaction | Sales Invoice
    user filters invoice with given data
    invoice principal listed successfully with Prime data
    Reload Page
    [Teardown]    user logouts and closes browser
    Given user navigates to menu Customer Transaction | Sales Return
    When user creates new return
    And user validates Prime invoice listed correctly
    Then invoice listed with all Prime invoice

5 - Able to select confirmed Non-Prime SalesInvoice only when Principal=Non-Prime
    [Documentation]    To validate on confirmed Non-Prime SalesInvoice is showing in listing
    [Tags]     distadm  9.1    NRSZUANQ-33455
    [Setup]     run keywords
    ${FilterDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    customer_code=CT0000001074
    ...    route_code=Rchoon
    ...    status=Invoiced
    set test variable     &{FilterDetails}
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Customer Transaction | Sales Invoice
    user filters invoice with given data
    invoice principal listed successfully with Non-Prime data
    Reload Page
    [Teardown]    user logouts and closes browser
    Given user navigates to menu Customer Transaction | Sales Return
    When user creates new return
    And user validates Non-Prime invoice listed correctly
    Then invoice listed with all Non-Prime invoice

6 - Verify only Reason with Non-Prime Warehouse is showing in reason dropdown
    [Documentation]
    [Tags]     distadm  9.1    NRSZUANQ-33456
    [Setup]     run keywords
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Configuration | Reference Data | Reason Type
    user searches for reason Return - Good Stock
    user sorts non prime table listing
    [Teardown]    user logouts and closes browser
    ${ReturnDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    type=Good Return
    ...    returnMode=Full
    set test variable     &{ReturnDetails}
    Given user navigates to menu Customer Transaction | Sales Return
    When user validates reason showing for full return
    Then warehouse displayed successfully

7 - Verify Warehouse is showing correctly for Full Reversal
    [Documentation]
    [Tags]     distadm  9.1    NRSZUANQ-33457
    ${ReturnDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    type=Good Return
    ...    returnMode=Full
    ...    reason=GOOD1
    set test variable     &{ReturnDetails}
    Given user navigates to menu Customer Transaction | Sales Return
    When user validates warehouse showing for full return
    Then warehouse displayed successfully

8 - Unable to add product which not in distributor product sector
    [Documentation]    Unable to create Sales Return using product which not linked to product sector
    [Tags]     distadm     9.1.1    NRSZUANQ-40065
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PS A Test
    When user gets distributor by using code 'DistEgg'
    Then user unassigned product sector using fixed data
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    warehouse=CCCC
    ...    product=AdActPS
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user provides return header using fixed data
    Then product not showing in dropdown
    When user retrieves token access as hqadm
    Then user revert to previous setting

9 - Able to add inactive product
    [Documentation]    Able to create Sales Return using inactive product
    [Tags]     distadm     9.1.1    NRSZUANQ-40072   NRSZUANQ-40242    NRSZUANQ-41374    NRSZUANQ-41172
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdInAct1'
    Then user updates product with fixed data
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=AdInAct1
    ...    productUom=EA:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'

10 - Unable to add blocked product
    [Documentation]    Unable to create Sales Return using blocked product
    [Tags]     distadm     9.1.1    NRSZUANQ-40076
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    Then user updates product with fixed data
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    warehouse=CCCC
    ...    product=AdeBlo1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user provides return header using fixed data
    Then product not showing in dropdown

11 - Claimable indicator hidden from header
    [Documentation]    Validate claimable indicator is removed from header
    [Tags]     distadm     9.2     NRSZUANQ-44310
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user navigates to menu Customer Transaction | Sales Return
    When user creates new return
    And user validates claimable is not visible
    Then claimable is not visible

12 - Verify invoice listing is showing based on customer and route selection
    [Documentation]    Validate invoice list based on customer and route selection
    [Tags]     distadm     9.2    NRSZUANQ-44314
    ${FilterDetails}=    create dictionary
    ...    customer_code=CT0000001074
    ...    route_code=Rchoon
    ...    status=Invoiced
    set test variable     &{FilterDetails}
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Customer Transaction | Sales Invoice
    user filters invoice with given data
    invoice principal listed successfully with Prime data
    Reload Page
    [Teardown]    user logouts and closes browser
    Given user navigates to menu Customer Transaction | Sales Return
    When user creates new return
    And user validates Prime invoice listed correctly
    Then invoice listed with all Prime invoice

13 - Able to calculate tax and store correctly (Tax on Net) when create Return
    [Documentation]    Able to create Return with tax on net
    [Tags]     distadm     9.1.1    NRSZUANQ-42298
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    route=Rchoon
    ...    Type=Damage Return
    ...    returnMode=Partial
    ...    reason=Expired
    ...    product=AdPrdTNet
    ...    productUom=PC1:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'

14 - Able to calculate tax and store correctly (Tax on Gross) when create Return
    [Documentation]    Able to create Return with tax on gross
    [Tags]     distadm     9.1.1    NRSZUANQ-42298
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    route=Rchoon
    ...    Type=Damage Return
    ...    returnMode=Partial
    ...    reason=Expired
    ...    product=AdPrdTGross
    ...    productUom=PC1:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'

15 - Able to calculate tax and store correctly (Tax on Tax) when create Return
    [Documentation]    Able to create Return with tax on tax
    [Tags]     distadm     9.1.1    NRSZUANQ-42298
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    route=Rchoon
    ...    Type=Damage Return
    ...    returnMode=Partial
    ...    reason=Expired
    ...    product=AdPrdTTax
    ...    productUom=PC1:3
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'

16 - Validate product index in product details storing correctly
    [Documentation]    Validating the product index storing correctly
    [Tags]     distadm     9.1.1    NRSZUANQ-42298
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    route=Rchoon
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    reason=GOOD1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user intends to insert product 'AdePrd4' with uom 'PC:3'
    And user intends to insert product 'A1001' with uom 'EA:1'
    And user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    And verifies product index saved in return database correctly

17 - Verify taxable details saved in DB correctly
    [Documentation]    Validating the product tax details storing correctly
    [Tags]     distadm     9.1.1    NRSZUANQ-42298
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    route=Rchoon
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    reason=GOOD1
    ...    product=AdPrdTTax
    ...    productUom=PC1:3
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    And verifies product tax saved in return database correctly

18 - Able to create Return with invoice and verify tax details
    [Documentation]    Validating the return with invoice is getting product and tax from invoice
    [Tags]     distadm     9.1.1    NRSZUANQ-42298
    [Setup]    run keywords
     ${ReturnDetails}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    user open browser and logins using user role ${user_role}
    user intends to insert product 'AdPrdTTax' with uom 'PC1:3'
    user retrieves token access as ${user_role}
    user creates invoice with fixed data
    expected return status code 200
    [Teardown]    user logouts and closes browser
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    route=Rchoon
    ...    Type=Damage Return
    ...    returnMode=Full
    ...    reason=Expired
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'

19 - Validate sampling invoice is not visible in return header level
    [Documentation]    Validate sampling invoice is not visible in return header level
    [Tags]     distadm    9.3
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
    Given user switches On multi principal
    And user sets the feature setup for sampling to on passing with 'SAMPLING' value
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    And user retrieves valid sampling program by customer
    And user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates invoice with fixed data
    When user navigates to menu Customer Transaction | Sales Return
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    Then user validates sampling invoice is not visible in header level

20 - Validate sampling invoice is not visible in return details level
    [Documentation]    Validate sampling invoice is not visible in return details level
    [Tags]     distadm    9.3
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
    Given user switches On multi principal
    And user sets the feature setup for sampling to on passing with 'SAMPLING' value
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    And user retrieves valid sampling program by customer
    And user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates invoice with fixed data
    When user navigates to menu Customer Transaction | Sales Return
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    product=AdePP1
    ...    productUom=EA:1
    Then user validates sampling invoice is not visible in details level

21 - Able to create return with customer group discount
    [Documentation]    Able to create return with group discount
    [Tags]     distadm    9.3
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Vege Tan
    ...    PROD_CD=ProdAde1
    Given user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user navigates to menu Customer Transaction | Sales Return
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    reason=ReasonGoodB01
    ...    product=ProdAde1
    ...    productUom=PC:1
    set test variable     &{ReturnDetails}
    Then user creates return with customer group discount
