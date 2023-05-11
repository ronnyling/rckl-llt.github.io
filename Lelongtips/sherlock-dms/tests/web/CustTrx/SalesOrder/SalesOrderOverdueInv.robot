*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesInvoice/SalesInvoiceOverdueInv.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderAddPage.py

*** Test Cases ***
1 - Able to Create Sales Order When customer have overdue invoice[Overdue = off, warning only]
    [Documentation]    Dist Overdue invoice = Warning only, customer overdue invoice checking Off
    [Tags]     distadm  9.1    NRSZUANQ-30435
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned off invoice overdue and set to Warning Only condition
    ${fixedData}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates invoice without promotion
    Then invoice created successfully with message 'Record created'

2 - Able to Create Sales Order When customer have overdue invoice[Overdue = off, Block]
    [Documentation]    Able to create Sales Order without applying promotion by using given data
    [Tags]     distadm  9.1    NRSZUANQ-30432
     Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned off invoice overdue and set to Block condition
    ${fixedData}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates invoice without promotion
    Then invoice created successfully with message 'Record created'

3 - Validate Sales Order not allow to select customer which have overdue invoice
    [Documentation]  Dist Overdue invoice = block, customer overdue invoice on
    [Tags]     distadm    9.1
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Block condition
    When user navigates to menu Customer Transaction | Sales Order
    Then Verified blocking prompt appear when select cust CreditLimitTest and route Rchoon

4 - Validate Sales Order will prompt warning when select customer that have overdue invoice
    [Documentation]   Dist Overdue invoice = Warning, customer overdue invoice on
    [Tags]     distadm    9.1    NRSZUANQ-30433
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Warning Only condition
    When user navigates to menu Customer Transaction | Sales Order
    Then Verified warning prompt appear when select cust CreditLimitTest and route Rchoon

5 - Unable to process sales order with status overdue[Overdue = On, Warning]
    [Documentation]
    [Tags]     distadm  9.1    NRSZUANQ-30440
     Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Warning Only condition
    ${fixedData}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order without promotion
    Then invoice created successfully with message 'Record created'
    When user process created sales order
    Then validated processed sales order is in Overdue Invoice status

6 - Unable to process sales order with status overdue[Overdue = On, Block]
    [Documentation]
    [Tags]     distadm  9.1    NRSZUANQ-30440
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Warning Only condition
    ${fixedData}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order without promotion
    Then invoice created successfully with message 'Record created'
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Block condition
    When user process created sales order
    Then validated processed sales order is in Overdue Invoice status

7 - Able to process sales order with status Process-Invoice[Overdue = On, Warning]
    [Documentation]
    [Tags]     distadm  9.1    NRSZUANQ-30438
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned off invoice overdue and set to Warning Only condition
    ${fixedData}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order without promotion
    Then invoice created successfully with message 'Record created'
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Block condition
    When user process created sales order
    Then validated processed sales order is in Process-Invoice status

8 - Able to process sales order with status Process-Invoice[Overdue = On, Block]
    [Documentation]
    [Tags]     distadm  9.1    NRSZUANQ-30437
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned off invoice overdue and set to Block condition
    ${fixedData}=    create dictionary
    ...    deliveryDate=today
    ...    route=Rchoon
    ...    customer=CreditLimitTest
    ...    product=AdePrd4
    ...    productUom=CTN:2
    ...    sellingPrice=58.90
    ...    gross=117.80
    ...    customerDisc=0.00
    ...    taxAmt=0.00
    ...    netAmt=117.80
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user creates sales order without promotion
    Then invoice created successfully with message 'Record created'
    Given user navigates to menu Master Data Management | Distributor
    When user validates created distributor is in the table and select to edit
    Then turned on invoice overdue and set to Block condition
    When user process created sales order
    Then validated processed sales order is in Process-Invoice status