*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/CreditNoteNonProduct/CreditNoteNonProductAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

*** Test Cases ***
1 - Able to create credit note non product using fixed data
    [Documentation]    To create credit note non product using fixed data
    [Tags]    distadm    9.1
    ${CNNPDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Salted Egg
    ...    product=AdNP1001
    ...    productUom=D01:5
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Non Product)
    When user creates Non-Prime credit note non product using fixed data
    Then credit note non product created successfully with message 'Record created successfully'

2 - Able to create credit note non product using random data
    [Documentation]    To create credit note non product using random data
    [Tags]    distadm    9.1
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Credit Note (Non Product)
    When user creates Prime credit note non product using random data
    Then credit note non product created successfully with message 'Record created successfully'

3 - Able to select confirmed prime invoice only when principal=Prime
    [Documentation]    To validate on confirmed Prime invoice is showing in listing
    [Tags]     distadm    9.2   NRSZUANQ-44466
    [Setup]     run keywords
    ${FilterDetails}=    create dictionary
    ...    principal=Prime
    ...    status=Invoiced
    ...    customer_code=CT0000001074
    ...    route_code=REgg02
    user open browser and logins using user role ${user_role}
    user switches On multi principal
    user navigates to menu Customer Transaction | Sales Invoice
    user filters invoice with given data
    invoice principal listed successfully with Prime data
    Reload Page
    [Teardown]    user logouts and closes browser
    ${CNNPDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    Given user navigates to menu Customer Transaction | Credit Note (Non Product)
    When user creates new credit note non product
    And user fills up header section with Prime selection using fixed data
    Then user validates Prime invoice listed correctly
    And invoice listed with all Prime invoice

4 - Route which is having same geo node with customer should listed in route selection
    [Documentation]    To validate the route displaying is correct based on customer selected
    [Tags]    distadm    9.2    NRSZUANQ-44466
    ${CNNPDetails}=    create dictionary
    ...    customer=Salted Egg
    Given user navigates to menu Customer Transaction | Credit Note (Non Product)
    When user creates new credit note non product
    And user selects customer:Salted Egg for credit note
    Then route displayed based on customer selected
