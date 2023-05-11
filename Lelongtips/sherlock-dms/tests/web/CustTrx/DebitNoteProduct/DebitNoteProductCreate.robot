*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/components/RadioButton.py
Library         ${EXECDIR}${/}resources/components/Pagination.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py

*** Test Cases ***
1 - Able to create debit note product using fixed data
    [Documentation]    To create debit note product using fixed data
    [Tags]    distadm    9.1
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Salted Egg
    ...    product=AdNP1001
    ...    productUom=D01:5
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Non-Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'

2 - Able to create debit note product using random data
    [Documentation]    To create debit note product using random data
    [Tags]    distadm    9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using random data
    Then debit note created successfully with message 'Record added'

3 - Verify Principal default to Prime in debit note product when Multi Principal = On
    [Documentation]    Verify debit note product having Principal default to Prime when multi principal = On
    [Tags]     distadm    9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Debit Note (Product)
    And user creates new debit note product
    Then principal field displaying in debit note product

4 - Verify Principal not displaying in debit note product when Multi Principal = Off
    [Documentation]    Verify debit note product not having Principal field when multi principal = Off
    [Tags]     distadm    9.1
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Debit Note (Product)
    And user creates new debit note product
    Then principal field not displaying in debit note product
    And user switches On multi principal

5 - Verify principal flag enabled after product is deleted from grid
    [Documentation]     Verify the principal flag is enabled back when product in details being deleted
    [Tags]     distadm    9.1
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Product)
    When user deletes product from grid
    Then principal in debit note product showing enabled

6 - Able to select confirmed prime invoice only when principal=Prime
    [Documentation]    To validate on confirmed Prime invoice is showing in listing
    [Tags]     distadm    9.1
    [Setup]     run keywords
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
    ...    status=Invoiced
    ...    customer_code=CT0000001074
    ...    customer=Vege Tan
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Customer Transaction | Sales Invoice
    user filters invoice with given data
    invoice principal listed successfully with Prime data
    Reload Page
    [Teardown]    user logouts and closes browser
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates new debit note product
    And user fills up header section with Prime selection using fixed data
    Then user validates Prime invoice listed correctly
    And invoice listed with all Prime invoice

7 - Able to select confirmed non-prime invoice only when principal=Non-Prime
    [Documentation]    To validate on confirmed Non-Prime invoice is showing in listing
    [Tags]     distadm    9.1
    [Setup]     run keywords
    ${FilterDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    status=Invoiced
    ...    customer_code=CT0000001074
    ...    customer=Vege Tan
    set test variable     &{FilterDetails}
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Customer Transaction | Sales Invoice
    user filters invoice with given data
    invoice principal listed successfully with Non-Prime data
    Reload Page
    [Teardown]    user logouts and closes browser
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=AdeNPProdF1
    ...    productUom=CTN:2
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates new debit note product
    And user fills up header section with Non-Prime selection using fixed data
    And user validates Non-Prime invoice listed correctly
    Then invoice listed with all Non-Prime invoice

8 - Validate product shown when product is added to product sector
    [Documentation]    To validate product shown in product listing when it is added to product sector and assigned to distributor
    [Tags]     distadm    9.1.1    NRSZUANQ-39209    NRSZUANQ-40308
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector
    user assigned product sector using fixed data
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'

9 - Validate product is hidden when product didn't added to product sector
    [Documentation]    To validate product is hidden in product listing when it is unassigned from product sector
    [Tags]     distadm    9.1.1    NRSZUANQ-39208    NRSZUANQ-40025
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector
    user switches On multi principal
    user unassigned product sector using fixed data
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates new debit note product
    And user fills up fields in header section with Prime selection using fixed data
    Then selected product hidden successfully from product selection

10 - Validate product is hidden when product is block
    [Documentation]    To validate product is hidden in product listing when it is inactive
    [Tags]     distadm    9.1.1    NRSZUANQ-40045
    ${update_product_details}=    create dictionary
    ...    product=LCPdt
    ...    status=Block
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates new debit note product
    And user fills up fields in header section with None selection using fixed data
    Then selected product hidden successfully from product selection

11 - Validate product is shown when product is inactive
    [Documentation]    To validate product is shown in product listing when it is inactive
    [Tags]     distadm    9.1.1    BUG:NRSZUANQ-41276
    ${update_product_details}=    create dictionary
    ...    PRD_CD=LCPdt
    ...    status=Inactive
    ...    SELLING_IND=1
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'
