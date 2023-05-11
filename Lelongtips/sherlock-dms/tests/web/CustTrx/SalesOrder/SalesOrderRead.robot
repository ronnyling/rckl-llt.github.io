*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderAddPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderEditPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesOrder/SalesOrderListPage.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

*** Test Cases ***
1 - Able to edit/view Sales Order
    [Documentation]    Able to edit/view Sales Order and validates header being disabled
    [Tags]     distadm  9.0
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    warehouse=WHAd2
    set test variable     &{fixedData}
    Given user navigates to menu Customer Transaction | Sales Order
    When user intends to insert product 'A1002' with uom 'EA:1'
    And user creates sales order with fixed data
    Then sales order created successfully with message 'Record created'
    When user selects sales order to view
    Then validates sales order header disabled

2 - Validate unable to save order with invalid sampling product
    [Documentation]    Unable to save order with invalid sampling product
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SMSO0000000020
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates unable to save with invalid sampling product

3 - Validate Apply Promo is disabled for sampling type order
    [Documentation]    Validate Apply Promo button is disabled for sampling sales order
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SMSO0000000020
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates Apply Promo is disabled

4 - Validate Apply Promo is enabled for selling/combined type order
    [Documentation]    Validate Apply Promo button is disabled for selling/combine sales order
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SO0000000058
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates Apply Promo is enabled

5 - Validate Product Type toggle is disabled for sampling product during edit
    [Documentation]    Validate product type button is disabled for sampling sales order during edit
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SMSO0000000020
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates Selling is disabled

6 - Validate Product Type toggle is enabled for combine product during edit
    [Documentation]    Validate product type button is enabled for combined sales order during edit
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SO0000000058
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates Selling is enabled
    And validates Sampling is enabled

7 - Able to edit/view sampling Sales Order
    [Documentation]    Able to edit/view sampling type Sales Order
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SMSO0000000020
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates sales order header disabled

8 - Able to edit/view combined Sales Order
    [Documentation]    Able to edit/view combine type Sales Order
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SO0000000058
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates sales order header disabled

9 - Validate Save button is enabled without Apply Promo for Sampling Type
    [Documentation]    Validate Save button is enabled without Apply Promo for selling/combine order
    [Tags]     distadm  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SMSO0000000020
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates Apply Promo is disabled
    And validates Save is enabled

10 - Validate Save button is enabled only after Apply Promo for Selling & Combine Type
    [Documentation]    Validate Save button is enabled only after Apply Promo for selling/combine order
    [Tags]     distadm5  9.3
    ${FilterDetails}=    create dictionary
    ...    txn_no=SO0000000058
    set test variable     &{FilterDetails}
    Given user navigates to menu Customer Transaction | Sales Order
    When user selects sales order to view
    Then validates Save is disabled
    When user clicks on Apply Promotion button
    And user clicks on Apply button
    Then validates Save is enabled

11 - Validate customer group discount is shown on sales order edit
    [Documentation]    Validate customer group discount is shown on sales order edit
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Vege Tan
    ...    warehouse=CCCC
    ...    product=TP002
    ...    productUom=BX:2
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Vege Tan
    ...    PROD_CD=TP002
    Given user navigates to menu Customer Transaction | Sales Order
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user creates sales order with fixed data
    And user verify cust group discount on footer level
    Then sales order created successfully with message 'Record created'
    When user opens created sales order
    And user verify cust group discount on product level
    Then user verify cust group discount on footer level

12 - Add more product quantity to validate customer group discount is recalculated
    [Documentation]    Add more product quantity to validate customer group discount is recalculated
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=prime
    ...    customer=Vege Tan
    ...    warehouse=CCCC
    ...    product=TP002
    ...    productUom=BX:2
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Vege Tan
    ...    PROD_CD=TP002
    Given user navigates to menu Customer Transaction | Sales Order
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user creates sales order with fixed data
    And user verify cust group discount on footer level
    Then sales order created successfully with message 'Record created'
    And user opens created sales order
    When user updated the product uom quantity
    Then customer group discount amount should also be updated