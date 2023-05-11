*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoiceDeallocatePost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderProcess.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesOrder/SalesOrderPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Warehouse/WarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

Test Setup      run keywords
...    User sets the feature setup for playbook to on passing with 'DELIVERY_APP' value
...    AND       user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets route plan by using code 'CY0000000417'
...    AND       user gets cust by using code 'CT0000001549'
...    AND       user gets customer shipto by desc 'CXTESTTAX'
...    AND       user gets warehouse by WHS_CD:whtt
...    AND       user retrieves prd by prd code 'CNPD001'


Test Teardown   User sets the feature setup for playbook to off passing with 'DELIVERY_APP' value


*** Test Cases ***
1 - Able to Deallocate Invoice with fixed data
    [Documentation]    Able to Process Sales Order with fixed data
    [Tags]     distadm      9.2
    ${so_header_details}=     create dictionary
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user creates sales order with fixed data
    Then expected return status code 200
    When user process the sales order
    Then expected return status code 202
    When user deallocated invoice with delivery status = P, invoice status = P
    Then expected return status code 202
    And validated invoice delivery status is updated successfully

2 - Unable to deallocate invoice return 201
    [Documentation]    Unable to deallocate invoice which status = Downloaded and expect update
    ...    status False return from response (D = downloaded, P = Open)
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user deallocated invoice with delivery status = D, invoice status = P
    Then expected return status code 202
    And validated invoice delivery status is not updated successfully

3 - Unable to deallocate invoice return 201
    [Documentation]    Unable to deallocate invoice which status = Downloaded and expect update
    ...    status False return from response (P = Open, S = confirmed)
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user deallocated invoice with delivery status = P, invoice status = S
    Then expected return status code 202
    And validated invoice delivery status is not updated successfully

4 - Unable to deallocate invoice return 201
    [Documentation]    Unable to deallocate invoice which status = Downloaded and expect update
    ...    status False return from response (S = Confirmed, S = confirmed)
    [Tags]    distadm    9.2
    Given user retrieves token access as ${user_role}
    When user deallocated invoice with delivery status = S, invoice status = S
    Then expected return status code 202
    And validated invoice delivery status is not updated successfully
