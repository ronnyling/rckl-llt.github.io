*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceOverdueInv.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceAddPage.py

*** Test Cases ***
1 - Validate SalesInvoice not allow to select customer which have overdue SalesInvoice
    [Documentation]  Dist Overdue SalesInvoice = block, customer overdue invoice on
    [Tags]     distadm    9.1     NRSZUANQ-30445
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Warning Only condition
    When user navigates to menu Customer Transaction | Sales Invoice
    Then Verified blocking prompt appear when select cust CreditLimitTest and route Rchoon

2 - Validate SalesInvoice will prompt warning when select customer that have overdue SalesInvoice
    [Documentation]   Dist Overdue invoice = Warning, customer overdue invoice on
    [Tags]     distadm    9.1     NRSZUANQ-30441
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Block condition
    When user navigates to menu Customer Transaction | Sales Invoice
    Then Verified warning prompt appear when select cust CreditLimitTest and route Rchoon

3 - Able to Create SalesInvoice When customer have overdue invoice[Overdue = off, warning only]
    [Documentation]    Dist Overdue invoice = Warning only, customer overdue invoice checking Off
    [Tags]     distadm  9.1    NRSZUANQ-30448
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned off invoice overdue and set to Warning Only condition
    ${InvDetails}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    warehouse=UMNPWHCC
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice without promotion
    Then invoice created successfully with message 'Record created'

4 - Able to Create SalesInvoice When customer have overdue invoice[Overdue = off, block]
    [Documentation]    Dist Overdue invoice = Block, customer overdue invoice checking Off
    [Tags]     distadm  9.1    NRSZUANQ-30447
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned off invoice overdue and set to Block condition
    ${InvDetails}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    warehouse=UMNPWHCC
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{InvDetails}
    Given user navigates to menu Customer Transaction | Sales Invoice
    When user creates invoice without promotion
    Then invoice created successfully with message 'Record created'