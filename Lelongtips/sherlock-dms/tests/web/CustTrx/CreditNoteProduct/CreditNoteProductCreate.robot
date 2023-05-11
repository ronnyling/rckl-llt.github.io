*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteProduct/CreditNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to create Credit Note with fixed data
    [Documentation]    To create Credit Note with fixed data
    [Tags]     distadm    9.1    NRSZUANQ-31631   NRSZUANQ-31643
    ${CNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Salted Egg
    ...    product=AdNP1001
    ...    productUom=D01:5
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Non-Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'

2 - Able to create Credit Note with random data
    [Documentation]    To create Credit Note with random data
    [Tags]     distadm    9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with random data
    Then credit note created successfully with message 'Record created'

3 - Verify Principal default to Prime in Credit Note when Multi Principal = On
    [Documentation]    Verify Credit Note having Principal default to Prime when multi principal = On
    [Tags]     distadm    9.1     NRSZUANQ-31623
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Credit Note (Product)
    And user creates new credit note
    Then principal field displaying in credit note

4 - Verify Principal not displaying in Credit Note when Multi Principal = Off
    [Documentation]    Verify Credit Note not having Principal field when multi principal = Off
    [Tags]     distadm    9.1     NRSZUANQ-31624
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Credit Note (Product)
    And user creates new credit note
    Then principal field not displaying in credit note
    And user switches On multi principal

5 - Verify principal flag enabled after product is deleted from grid
    [Documentation]     Verify the principal flag is enabled back when product in details being deleted
    [Tags]     distadm    9.1     NRSZUANQ-31634
    ${CNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user deletes product from grid
    Then principal in credit note showing enabled

6 - Verify Error prompt when user selects Reason which does not have Warehouse
    [Documentation]    Verify the error message will shown when the reason is without warehouse asssignment
    [Tags]     distadm    9.1     NRSZUANQ-31945
    ${CNDetails}=    create dictionary
    ...    principal=Prime
    ...    reason=GOOD3
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user selects reason without warehouse assigned
    Then reason unable to select successfully with message 'Warehouse is not setup'

7 - Able to select confirmed prime invoice only when principal=Prime
    [Documentation]    To validate on confirmed Prime invoice is showing in listing
    [Tags]     distadm    9.1     NRSZUANQ-31626
    [Setup]     run keywords
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
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
    ${CNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    Given user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates new credit note
    And user validates Prime invoice listed correctly
    Then invoice listed with all Prime invoice

8 - Able to select confirmed non-prime invoice only when principal=Non-Prime
    [Documentation]    To validate on confirmed Non-Prime invoice is showing in listing
    [Tags]     distadm    9.1     NRSZUANQ-31628
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
    ${CNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    Given user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates new credit note
    And user validates Non-Prime invoice listed correctly
    Then invoice listed with all Non-Prime invoice

9 - Verify invoice listing is showing based on customer and route selection
    [Documentation]    To validate invoice list is based on customer and route selection
    [Tags]     distadm    9.2    NRSZUANQ-44333
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
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
    Given user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates new credit note
    And user validates Non-Prime invoice listed correctly
    Then invoice listed with all Prime invoice

10 - Able to create Credit Note with tax on gross and verify tax details
    [Documentation]    To validate the tax on gross for credit note
    [Tags]     distadm    9.1.1    NRSZUANQ-42299
    ${CNDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    product=AdPrdTGross
    ...    productUom=PC1:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'

11 - Able to create Credit Note with tax on net and verify tax details
    [Documentation]    To validate the tax on net for credit note
    [Tags]     distadm    9.1.1    NRSZUANQ-42299
    ${CNDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    product=AdPrdTNet
    ...    productUom=PC1:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'

12 - Able to create Credit Note with tax on tax and verify tax details
    [Documentation]    To validate the tax on tax for credit note
    [Tags]     distadm    9.1.1    NRSZUANQ-42299
    ${CNDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    product=AdPrdTTax
    ...    productUom=PC1:3
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'

13 - Validate product index in product details storing correctly
    [Documentation]    To validate the product index saved correctly for credit note
    [Tags]     distadm    9.1.1    NRSZUANQ-42299
    ${prd1_details}=  create dictionary
    ...   product=A1001
    ...   productUom=EA:3
    ${prd2_details}=  create dictionary
    ...   product=AdPrdTGross
    ...   productUom=PC1:2
    @{prd_list} =  create list
    ...    ${prd1_details}    ${prd2_details}
    ${CNDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    product=@{prd_list}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'
    And verifies product index saved in credit note database correctly

14 - Verify taxable details saved in DB correctly
    [Documentation]    To validate the product tax saved correctly for credit note
    [Tags]     distadm    9.1.1    NRSZUANQ-42299
    ${CNDetails}=    create dictionary
    ...    principal=Prime
    ...    route=Rchoon
    ...    customer=CXTESTTAX
    ...    product=AdPrdTNet
    ...    productUom=PC1:3
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Product)
    When user creates Prime credit note with fixed data
    Then credit note created successfully with message 'Record created'
    And verifies product tax saved in credit note database correctly
