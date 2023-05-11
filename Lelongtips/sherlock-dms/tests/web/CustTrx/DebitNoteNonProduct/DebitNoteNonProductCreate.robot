*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteNonProduct/DebitNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to create debit note non product using fixed data
    [Documentation]    To create debit note non product using fixed data
    [Tags]    distadm    9.1
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Salted Egg
    ...    product=AdNP1001
    ...    productUom=D01:5
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user creates Non-Prime debit note non product using fixed data
    Then debit note created successfully with message 'Record added'

2 - Able to create debit note non product using random data
    [Documentation]    To create debit note non product using random data
    [Tags]    distadm    9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user creates Prime debit note non product using random data
    Then debit note created successfully with message 'Record added'

3 - Verify Principal default to Prime in debit note non product when Multi Principal = On
    [Documentation]    Verify debit note non product having Principal default to Prime when multi principal = On
    [Tags]     distadm    9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Debit Note (Non Product)
    And user creates new debit note non product
    Then principal field displaying in debit note non product

4 - Verify Principal not displaying in debit note non product when Multi Principal = Off
    [Documentation]    Verify debit note non product not having Principal field when multi principal = Off
    [Tags]     distadm    9.1
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Debit Note (Non Product)
    And user creates new debit note non product
    Then principal field not displaying in debit note non product
    And user switches On multi principal

5 - Verify principal flag enabled after product is deleted from grid
    [Documentation]     Verify the principal flag is enabled back when product in details being deleted
    [Tags]     distadm    9.1
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user deletes service from grid
    Then principal in debit note non product showing enabled

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
    Given user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user creates new debit note non product
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
    Given user navigates to menu Customer Transaction | Debit Note (Non Product)
    When user creates new debit note non product
    And user fills up header section with Non-Prime selection using fixed data
    And user validates Non-Prime invoice listed correctly
    Then invoice listed with all Non-Prime invoice
