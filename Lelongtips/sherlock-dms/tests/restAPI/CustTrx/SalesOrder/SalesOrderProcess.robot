*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderProcess.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup       run keywords
...    user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets route plan by using code 'CY0000000417'
...    AND       user gets cust by using code 'CT0000001549'
...    AND       user gets customer shipto by desc 'CXTESTTAX'
...    AND       user gets warehouse by WHS_CD:whtt
...    AND       user retrieves prd by prd code 'CNPD001'

*** Test Cases ***
1 - Able to Procecss Sales Order with fixed data
    [Documentation]    Able to Process Sales Order with fixed data
    [Tags]     distadm      9.1
    ${so_header_details}=     create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates sales order with fixed data
    Then expected return status code 200
    When user process the sales order
    Then expected return status code 202

2- Able to Procecss Sales Order with fixed data and validate temp invoice delivery status will inserted into DB
    [Documentation]    Able to Process Sales Order with fixed data, and temp invoice delivery status will be 'P'
    [Tags]     distadm      9.2     NRSZUANQ-46089
    ${SODetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    warehouse=whtt
    ...    shipTo=CXTESTTAX
    ...    product=CNPD001
    ...    distributor=DistEgg
    ...    status=P
    ...    selling=S
    Given user retrieves token access as ${user_role}
    When user post random sales order as prerequisite
    Then expected return status code 200
    When user process the sales order
    Then expected return status code 202
    And validated temp invoice delivery status is default to pending

3 - Able to process Sampling Order
    [Documentation]    Able to process sampling order
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
    When user process the sales order
    Then expected return status code 202