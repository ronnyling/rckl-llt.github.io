*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoiceGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

Test Setup       run keywords
...    user retrieves token access as ${user_role}
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets cust by using code 'CT0000001074'
...    AND       user creates prerequisite for reason 'Return - Good Stock'
...    AND       user assigns both warehouse to reason
...    AND       user retrieves reason warehouse
...    AND       user retrieves prd by prd code 'AdNP1001'

*** Test Cases ***
1 - Able to post non-prime return with fixed data
    [Documentation]    Able to post non-prime return with fixed data
    [Tags]       distadm    9.1     NRSZUANQ-33573
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=Vege Tan
    ...    REMARK=testing return
    ...    CN_TYPE=G
    ${AppSetupDetails}=    create dictionary
    ...    MAKE_REFERENCE_NUMBER_MANDATORY=${False}
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    Given user retrieves token access as hqadm
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    And user switches On multi principal
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200

2 - Able to post non-prime return with random data
    [Documentation]    Able to post non-prime return with random data
    [Tags]       distadm    9.1    NRSZUANQ-33604
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=Vege Tan
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user post return with random data
    Then expected return status code 200

#Comment out due to developer mention removed validation from API due to slowness on the validation part and only validates in UI side
3 - Unable to POST Prime Return using Non-Prime Product and get 404
    [Documentation]    Unable to post prime return with non-prime product
    [Tags]    distadm    9.1    NRSZUANQ-33577
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 404

#Comment out due to developer mention removed validation from API due to slowness on the validation part and only validates in UI side
4 - Unable to POST Non-Prime Return using Prime invoice and get 404
    [Documentation]    Unable to post non-prime return with prime invoice
    [Tags]    distadm    9.1    NRSZUANQ-33588
    Given user retrieves 'CT0000001074' cust inv based on flag 'PRIME'
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=Vege Tan
    ...    INV_ID=${INV}
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 404

5 - Unable to POST Non-Prime Return using Reason with only prime warehouse
    [Documentation]    Unable to post non-prime return with reason with only prime warehouse
    [Tags]       distadm    9.1    NRSZUANQ-33591
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user gets cust by using code 'CT0000001074'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdNP1001'
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=Vege Tan
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 400

#Comment out due to developer mention removed validation from API due to slowness on the validation part and only validates in UI side
6 - Unable to POST Prime Return using Non-Prime warehouse and get 404
    [Documentation]    Unable to post non-prime return with random data
    [Tags]    distadm    9.1    NRSZUANQ-33593
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    WHS_ID=${WAREHOUSE_ID_NP}
    ${rtn_body_details}=    create dictionary
    ...    WHS_ID=${WAREHOUSE_ID_NP}
    Given user retrieves token access as ${user_role}
    When user post return with random data
    Then expected return status code 404

7 - Unable to POST Return using hq access and get 403
    [Documentation]    Unable to post return using other than distributor access
    [Tags]    hqadm    hquser   sysimp    9.1     NRSZUANQ-33598
    [Setup]    run keywords
    ...    user retrieves token access as hqadm
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'A1001'
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 403

8 - Unable to POST RTN with product which not in distributor product sector and get 404 Not Found
    [Documentation]    Unable to post return using product which not assign to product sector
    [Tags]       distadm    9.1.1    NRSZUANQ-40103     prdSector
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns Prime warehouse to reason
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdActPS'
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    CN_TYPE=G
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    And user assigned product sector using fixed data
    When user unassigned product sector using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 404

9 - Able to POST RTN with inactive product and get 200 OK
    [Documentation]    Able to post return using inactive product
    [Tags]    distadm    9.1.1     NRSZUANQ-40105     NRSZUANQ-40258
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
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    CN_TYPE=G
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200

10 - Unable to POST RTN with blocked product and get 404 Not Found
    [Documentation]    Unable to post return using block product
    [Tags]    distadm    9.1.1     NRSZUANQ-40107
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
    ...    STATUS=Block
    ...    SELLING_IND=1
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    CN_TYPE=G
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 404

11 - Able to create Return without invoice and verify taxable amount
    [Documentation]    Able to post prime return with tax
    [Tags]       distadm    9.1.1    NRSZUANQ-42291
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    And user retrieves prd by prd code 'AdPrdTTax'
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then expected return status code 200

12 - Able to create Return with invoice and verify taxable amount
    [Documentation]    Able to post prime return with invoice and verify tax
    [Tags]       distadm    9.1.1    NRSZUANQ-42291
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
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user post return with random data
    Then expected return status code 200

13 - Able to POST draft return
    [Documentation]    Able to create open return and patch the status to draft
    [Tags]       distadm    9.3
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user switches On multi principal
    And user retrieves prd by prd code 'AdPrdTTax'
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then update return to draft status

14 - Able to POST sales return with customer group disc
    [Documentation]    Able to create sales return with customer group discount
    [Tags]      distadm    9.3
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdePP1
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    And user retrieves prd by prd code 'AdePP1'
    When user post return with random data
    Then expected return status code 200
