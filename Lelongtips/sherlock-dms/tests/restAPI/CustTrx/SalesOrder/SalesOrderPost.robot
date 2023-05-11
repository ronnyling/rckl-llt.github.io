*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPut.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderGet.py

Test Setup        run keywords
...    user retrieves token access as distadm
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets route plan by using code 'CY0000000417'
...    AND       user gets cust by using code 'CT0000001549'
...    AND       user gets customer shipto by desc 'CXTESTTAX'
...    AND       user gets warehouse by WHS_CD:CCCC
...    AND       user retrieves prd by prd code 'A1001'

*** Test Cases ***
1 - Able to POST Sales Order transactions with random data
    [Documentation]    Able to post sales order transaction with random data
    [Tags]    distadm    9.1    NRSZUANQ-33324
    ${fixedData}=     create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdeCP001' with uom 'EA:2'
    And user creates sales order with random data
    Then expected return status code 200

2 - Able to POST Sales Order transactions with fixed data
    [Documentation]    Able to post sales order transaction with fixed data
    [Tags]    distadm    9.1     NRSZUANQ-33324
    ${fixedData}=     create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:2'
    And user intends to insert product 'AdPrdTGross' with uom 'PC1:1'
    And user creates sales order with fixed data
    Then expected return status code 200

3 - Unable to POST Sales order using HQ access and get 403
    [Documentation]    Able to retrieve sales order transactions using other than distributor user
    [Tags]    hqadm   hquser   sysimp    9.1
    ${so_header_details}=     create dictionary
    ...    PRIME_FLAG=PRIME
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user creates sales order with random data
    Then expected return status code 403

4 - Unable to POST Sales Order with product which not in distributor product sector and get 404 Not Found
    [Documentation]    Unable to POST Sales Order with product which not in distributor product sector and get 404 Not Found
    [Tags]      distadm      9.1.1     NRSZUANQ-40097     prdSector
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${so_header_details}=     create dictionary
    ...    PRIME_FLAG=PRIME
    ${ProductSectorDetails}=     create dictionary
   ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    And user assigned product sector using fixed data
    When user retrieves prd by prd code 'NTProd'
    And user unassigned single product sector
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user creates sales order with fixed data
    Then expected return status code 404

5 - Unable to POST Sales Order with inactive product and get 404 Not Found
    [Documentation]    Unable to POST Sales Order with inactive product and get 404 Not Found
    [Tags]     distadm  9.1.1   NRSZUANQ-40098
    ${so_header_details}=     create dictionary
    ...    PRIME_FLAG=PRIME
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    set test variable     ${user_role}    hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable     ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user creates sales order with fixed data
    Then expected return status code 404

6 - Unable to POST Sales Order with blocked product and get 404 Not Found
    [Documentation]    Unable to POST Sales Order with blocked product and get 404 Not Found
    [Tags]     distadm    9.1.1   NRSZUANQ-40099
    ${so_header_details}=     create dictionary
    ...    PRIME_FLAG=PRIME
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    set test variable     ${user_role}    hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable     ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user creates sales order with fixed data
    Then expected return status code 404

7 - Able to POST Sampling Sales Order and get 200
    [Documentation]    Able to post sampling order
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
    Given user sets the feature setup for sampling to on passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates sales order with fixed data
    Then expected return status code 200

8 - Able to POST Combine Sales Order and get 200
    [Documentation]    Able to post sampling order
    [Tags]     distadm    9.3       test
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${invType}=    create dictionary
    ...    INVOICE_TXNTYPE=S
    ${AppSetupDetails}=    create dictionary
    ...    SAMPLING_COMBINE_IN_SELLING_TXN=${True}
    Given user sets the feature setup for sampling to on passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    Then expected return status code 200
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=P
    set test variable    &prdType
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    ${prdType}=    create dictionary
    ...    PRD_SLSTYPE=S
    set test variable    &prdType
    And user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates sales order with fixed data
    Then expected return status code 200

9 - Unable to POST for order with Sampling product when Sampling = Off
    [Documentation]    Unable to post order containing sampling product when sampling = off
    [Tags]    distadm    9.3
    [Teardown]      run keywords
    ...    user sets the feature setup for sampling to on passing with 'SAMPLING' value
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
    Given user sets the feature setup for sampling to off passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'AdePP1' with uom 'EA:5'
    And user creates sales order with fixed data
    Then expected return status code 400

10 - Unable to POST order with invalid sampling product
    [Documentation]    Unable to post order with invalid sampling product
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
    Given user sets the feature setup for sampling to on passing with 'SAMPLING' value
    Given user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user retrieves valid sampling program by customer
    Then expected return status code 200
    When user intends to insert product 'A1002' with uom 'EA:5'
    And user creates sales order with fixed data
    Then expected return status code 404

11 - Unable to POST sampling order with invalid token
    [Documentation]    Able to post sampling order
    [Tags]     hqadm    9.3
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
    Given user sets the feature setup for sampling to on passing with 'SAMPLING' value
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as distadm
    When user retrieves invalid sampling program by customer
    Then expected return status code 200
    set test variable      ${user_role}    hqadm
    When user retrieves token access as ${user_role}
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    Then expected return status code 403

12 - Able to create order with customer group disc
    [Documentation]    Able to post order with group disc
    [Tags]     distadm    9.3
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdePP1
    Given user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    Then expected return status code 200

13 - Able to save sales order without customer group discount
    [Documentation]    Able to save sales order without customer group discount
    [Tags]     distadm    9.3       NRSZUANQ-55213
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    When user intends to insert product 'AdPrdTGross' with uom 'PC1:1'
    And user updates sales order with fixed data
    Then expected return status code 200

14 - Able to save edited sales order with customer group discount
    [Documentation]    Able to save sales order without customer group discount
    [Tags]     distadm    9.3       NRSZUANQ-55220
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdePP1
    Given user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    When user intends to insert product 'AdPrdTGross' with uom 'PC1:1'
    And user updates sales order with fixed data
    Then expected return status code 200