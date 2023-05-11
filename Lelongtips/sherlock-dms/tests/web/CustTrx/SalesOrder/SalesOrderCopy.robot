*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXEC_DIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

*** Test Cases ***
#DISCLAIMER: If there is dirty data (Products not having UOM/Price etc) - Might cause automation failure
#PRD_LISTPRC error is caused by product not set up correctly
1 - Able to Copy Sales Order using fixed data and save
    [Documentation]    Able to copy Sales Order that was created as prerequisite and save
    [Tags]     distadm     9.1    NRSZUANQ-33132    NRSZUANQ-36190
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    shipTo=Kelantan Packaging
    ...    warehouse=WH ade2
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    And user applies promotion
    And user click save
    Then sales order created successfully with message 'Record created'

2. Able to Copy Sales Order using random data and save
    [Documentation]    Able to copy a random sales order and save
    [Tags]     distadm  9.1     NRSZUANQ-33132   NRSZUANQ-36190
    [Setup]     run keywords
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001074
    ...    warehouse=WHAd2
    ...    product=JunPrimeTaxableProdu
    ...    shipTo=Kelantan Packaging
    ...    status=P
    ...    selling=S
    ...    distributor=DistEgg
    user post random sales order as prerequisite
    user open browser and logins using user role ${user_role}
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ...    shipTo=Kelantan Packaging
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies random sales order
    And user applies promotion
    And user click save
    Then sales order created successfully with message 'Record created'

3. Copy Order button only shows sales order from last 30 days
    [Documentation]    Copy order only shows sales order from last 30 days
    [Tags]     distadm  9.1    NRSZUANQ-33124
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ...    shipTo=Kelantan Packaging
    Given user navigates to menu Customer Transaction | Sales Order
    Then user verify only last 30 days shown

4. Able to remove products after copying sales order
    [Documentation]    Able to remove products after copying sales order
    [Tags]     distadm  9.1    NRSZUANQ-33128   NRSZUANQ-34845
    [Setup]     run keywords
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001074
    ...    warehouse=WHAd2
    ...    product=JunPrimeTaxableProdu
    ...    shipTo=Kelantan Packaging
    ...    status=P
    ...    selling=S
    ...    distributor=DistEgg
    user post random sales order as prerequisite
    user open browser and logins using user role ${user_role}
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ...    shipTo=Kelantan Packaging
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    When user removes random product
    Then user applies promotion
    And user click save

5. Able to change product quantity after copying sales order
    [Documentation]    Able to change product quantity after copying sales order
    [Tags]     distadm  9.1    NRSZUANQ-33128    NRSZUANQ-34846
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ...    shipTo=Kelantan Packaging
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    When user changes random product quantity
    Then user applies promotion
    And user click save

6. Able to add product after copying sales order and save
    [Documentation]    Able to add random product after copying sales order
    [Tags]     distadm  9.1   NRSZUANQ-33128   NRSZUANQ-34844
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ...    shipTo=Kelantan Packaging
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    When user adds random product
    Then user applies promotion
    And user click save

7. Verify that copied products are using latest price values
    [Documentation]  Verify that copied products are using latest price values
    [Tags]    distadm    9.1    NRSZUANQ-33617   NRSZUANQ-34852
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ...    shipTo=Kelantan Packaging
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    Then user verify product price

7. Verify that copied products are using latest tax values
    [Documentation]  Verify that copied products are using latest tax values
    [Tags]    distadm    9.1   NRSUANQ-34852
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    Then user verify product tax

8. Verify that product quantity is merged if copy multiple sales order
    [Documentation]  Verify that copied products are using latest tax values
    [Tags]    distadm    9.1   NRSUANQ-34852
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=Vege Tan
    ...    warehouse=WH ade2
    ${SOIDs}=    create list
    ...    SO0000000665
    ...    SO0000000646
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    Then user verify product quantity merged

9 - Able to copy order from Combine type Sales Order
    [Documentation]    Able to copy order from Combine type
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=rrrr
    ...    customer=NikeCust3
    ...    shipTo=NikeCust3
    ...    warehouse=whcc
    ${SOIDs}=    create list
    ...    SO0000000058
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    And user applies promotion
    And user click save
    Then sales order created successfully with message 'Record created'

10 - Validate amount of product being copied over
    [Documentation]    Validate amount of product being copied over
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=rrrr
    ...    customer=NikeCust3
    ...    shipTo=NikeCust3
    ...    warehouse=whcc
    ${SOIDs}=    create list
    ...    SO0000000058
    ${amountData}=    create dictionary
    ...    gross=66.00
    ...    net=66.00
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    Then user validates the amount of product being copied over

10 - Validate Selling | Combine type order is listed in copy listing
    [Documentation]    Validate selling and combine type order is listed to be copied
    [Tags]     distadm5    9.3
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=rrrr
    ...    customer=NikeCust3
    ...    shipTo=NikeCust3
    ...    warehouse=whcc
    ${SOIDs}=    create list
    ...    SO0000000058
    ...    SO0000000052
    Given user navigates to menu Customer Transaction | Sales Order
    When user copies fixed sales order
    And user applies promotion
    And user click save
    Then sales order created successfully with message 'Record created'

11 - Validate customer group discount from copied order is recalculated based latest valid setup
    [Documentation]    Validate customer group discount from copied order is recalculated based latest valid setup
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Joy Groceria
    ...    warehouse=CCCC
    ...    product=TP002
    ...    productUom=BX:1
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Joy Groceria
    ...    PROD_CD=TP002
    Given user navigates to menu Customer Transaction | Sales Order
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    Set Library Search Order    SalesOrderAddPage.py
    When user creates sales order with fixed data
    And user verify cust group discount on footer level
    Then sales order created successfully with message 'Record created'
    And user copies created sales order
    And user applies promotion
    And user verify cust group discount on footer level
    Then sales order created successfully with message 'Record created'
