*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderGet.py
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

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets route plan by using code 'CY0000000417'
...    AND       user gets cust by using code 'CT0000001549'
...    AND       user gets customer shipto by desc 'CXTESTTAX'
...    AND       user gets warehouse by WHS_CD:CCCC
...    AND       user retrieves prd by prd code 'A1001'

*** Test Cases ***
1 - Able to retrieve all Sales Order transactions
    [Documentation]    Able to retrieve all sales order transactions
    [Tags]    distadm    9.1     NRSZUANQ-30057
    Given user retrieves token access as ${user_role}
    When user retrieves all sales order transaction
    Then expected return status code 200

2 - Able to retrieve Sales Order transactions using ID
    [Documentation]    Able to retrieve sales order transactions using id
    [Tags]    distadm    9.1     NRSZUANQ-30058
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user retrieves sales order transaction by id
    Then expected return status code 200

3 - Unable to GET Sales order using HQ access and get 403
    [Documentation]    Able to retrieve sales order transactions using other than distributor user
    [Tags]    hqadm   hquser   sysimp    9.1     NRSZUANQ-30059
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves all sales order transaction
    Then expected return status code 403

4 - Able to GET Sales order from past 30 days
    [Documentation]  Able to get sales order transactions from past 30 days
    [Tags]    distadm    9.1    NRSZUANQ-33216
    Given user retrieves token access as ${user_role}
    When user retrieves sales order transaction in last 30 days
    Then expected return status code 200

5 - Able to GET multiple fixed sales orders
    [Documentation]  Able to get multiple sales order transactions for copy order
    [Tags]    distadm    9.1    NRSZUANQ-34908
    ${SO_details}=   create list
    ...    CCBCDA2C:C559D67A-C77B-4B51-9A39-B16A22982983
    ...    CCBCDA2C:4958DB28-0E4C-4A65-BFEF-FC2DD1298FD4
    Given user retrieves token access as ${user_role}
    When user retrieves multiple fixed sales order transaction
    Then expected return status code 200

6 - Able to GET multiple random sales orders
    [Documentation]  Able to get multiple sales order transactions for copy order
    [Tags]    distadm    9.1    NRSZUANQ-34908
    [Setup]  run keywords
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001074
    ...    warehouse=WHAd2
    ...    product=JunPrimeTaxableProdu
    ...    shipTo=Kelantan Packaging
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    user post random sales order as prerequisite
    user post random sales order as prerequisite
    Given user retrieves token access as ${user_role}
    When user retrieves multiple random fixed sales order transaction
    Then expected return status code 200

7 - Able to retrieve Sales Order with Sampling only type
    [Documentation]    Able to retrieve sales order with sampling type
    [Tags]    distadm    9.3     NRSZUANQ-52922
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
    When user retrieves sales order transaction by id
    Then expected return status code 200

8 - Validate group discount amount on order header
    [Documentation]    Validate group discount amount on order header
    [Tags]    distadm    9.3        NRSZUANQ-55210
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdePP1
    Given user retrieves token access as ${user_role}
    When user retrieves customer group discount with valid customer and product
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    Then expected return status code 200
    When user retrieves sales order transaction by id
    Then validate the group discount is retrieved correctly

#9 - Validate group discount details on order detail
#    [Documentation]    Validate group discount details on order detail
#    [Tags]    distadm    9.3        NRSZUANQ-55211
#    ${fixedData}=    create dictionary
#    ...    PRIME_FLAG=PRIME
#    ...    INV_CUST=CXTESTTAX
#    ...    INV_ROUTE=Rchoon
#    ...    INV_WH=CCCC
#    ${discountDetails}=    create dictionary
#    ...    CUST_NAME=CXTESTTAX
#    ...    PROD_CD=AdePP1
#    Given user retrieves token access as ${user_role}
#    When user retrieves customer group discount with valid customer and product
#    And user intends to insert product 'AdePP1' with uom 'EA:1'
#    And user creates sales order with fixed data
#    Then expected return status code 200
#    When user retrieves sales order details by id
#    Then validate customer group discount details from sales order is retrieved correctly

10 - Validate no group discount details is retrieved for product without discount
    [Documentation]    Validate no group discount details is retrieved for product without discount
    [Tags]    distadm    9.3        NRSZUANQ-55218
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    Then expected return status code 200
    When user retrieves sales order details by id
    Then validate no customer group discount in sales order details


11 - Validate no group discount amount is retrieved when no discount is applied
    [Documentation]    Validate no group discount amount is retrieved when no discount is applied
    [Tags]    distadm    9.3        NRSZUANQ-55216
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdePP1' with uom 'EA:1'
    And user creates sales order with fixed data
    Then expected return status code 200
    When user retrieves sales order transaction by id
    Then validate no customer group discount in sales order header
