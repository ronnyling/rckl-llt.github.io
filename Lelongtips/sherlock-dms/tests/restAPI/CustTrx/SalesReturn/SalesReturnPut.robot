*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

Test Setup       user creates Non-Prime return as prerequisite

*** Test Cases ***
1 - Able to put non prime return and return 200
    [Documentation]    Able to update return product details
    [Tags]       distadm    9.1    NRSZUANQ-33575
    [Setup]  run keywords
    ${RtnDetailsPre}=    create dictionary
    ...    route=Rchoon
    ...    customer=CT0000001074
    ...    reasontype=Return - Good Stock
    ...    product=AdNP1001
    ...    distributor=DistEgg
    ${AppSetupDetails}=    create dictionary
    ...    MAKE_REFERENCE_NUMBER_MANDATORY=${False}
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    user creates Non-Prime return as prerequisite
    Given user retrieves token access as ${user_role}
    When user updates return with fixed data
    Then expected return status code 200

2 - Unable to put return with hq acess and return 403
    [Documentation]    Unable to update return with other than distributor access
    [Tags]    hqadm    hquser   sysimp   9.1     NRSZUANQ-33600
    [Setup]  run keywords
    ${RtnDetailsPre}=    create dictionary
    ...    PRIME_FLAG=Prime
    ...    route=Rchoon
    ...    customer=CT0000001074
    ...    reasontype=Return - Good Stock
    ...    product=AdNP1001
    ...    distributor=DistEgg
    user creates Non-Prime return as prerequisite
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user updates return with random data
    Then expected return status code 403

3 - Unable to update RTN by adding product which not in distributor product sector and get status 404
    [Documentation]    Able to update Return quantity for product which not assigned at product sector
    [Tags]      distadm    9.1.1   NRSZUANQ-40109   prdSector
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'A1001'
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user assigned product sector using fixed data
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200
    When user retrieves prd by prd code 'AdActPS'
    Then user unassigned product sector using fixed data
    Given user retrieves token access as ${user_role}
    When user updates return with random data
    Then expected return status code 404

4 - Able to update RTN by adding inactive product and get 200 OK
    [Documentation]    Able to update Return quantity for inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40110
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'PRDInc'
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user updates return with random data
    Then expected return status code 200

5 - Unable to update RTN by adding blocked product and get 404 Not Found
    [Documentation]    Able to update Return quantity for blocked product
    [Tags]      distadm    9.1.1   NRSZUANQ-40111
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdeBlo1'
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user updates return with random data
    Then expected return status code 404

6 - Able to update Return and verify taxable amount
    [Documentation]    Able to update Return and verify tax
    [Tags]     distadm    9.1.1   NRSZUANQ-42291
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ${uom_details}=  create dictionary
    ...   UOM=PC1
    ...   QTY=3
    @{uom_list} =  create list
    ...    ${uom_details}
    ${prd_details}=  create dictionary
    ...   PRD_CODE=AdPrdTTax
    ...   PRD_UOM=${uom_list}
    @{prd_list} =  create list
    ...    ${prd_details}
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ...    PROD_ASS_DETAILS=${prd_list}
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200
    When user updates return with random data
    Then expected return status code 200

7 - Able to put draft return and return 200
    [Documentation]    Able to update draft return to open status
    [Tags]       distadm    9.3
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user gets cust by using code 'CT0000001549'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns both warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdPrdTTax'
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${RtnDetailsPre}=    create dictionary
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    reasontype=Return - Good Stock
    ...    product=AdPrdTTax
    ...    distributor=DistEgg
    set test variable     ${rtn_status}   T
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then update return to draft status
    When user updates return with fixed data
    Then expected return status code 200

8 - Able to PUT sales return with customer group disc
    [Documentation]    Able to update sales return with customer group discount
    [Tags]      distadm    9.3
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user gets cust by using code 'CT0000001549'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns both warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdPrdTTax'
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdePP1
    ${RtnDetailsPre}=    create dictionary
    ...    route=Rchoon
    ...    customer=CT0000001549
    ...    reasontype=Return - Good Stock
    ...    product=AdePP1
    ...    distributor=DistEgg
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    And user retrieves prd by prd code 'AdePP1'
    When user post return with random data
    Then expected return status code 200
    And user retrieves customer group discount with valid customer and product
    When user updates return with fixed data
    Then expected return status code 200
