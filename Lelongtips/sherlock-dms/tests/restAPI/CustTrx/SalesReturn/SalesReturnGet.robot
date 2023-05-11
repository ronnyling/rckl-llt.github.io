*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to retrieve all Return
    [Documentation]    Able to retrieve all return
    [Tags]    distadm    9.1     NRSZUANQ-33192
    Given user retrieves token access as ${user_role}
    When user retrieves all return
    Then expected return status code 200

2 - Able to retrieve Return using ID
    [Documentation]    Able to retrieve return transactions using id
    [Tags]    distadm    9.1     NRSZUANQ-33194
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user retrieves return by id
    Then expected return status code 200

3 - Unable to GET Return using HQ access and get 403
    [Documentation]    Unable to retrieve return using other than distributor user
    [Tags]    hqadm   hquser   sysimp    9.1     NRSZUANQ-33260
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves all return
    Then expected return status code 403

4 - Able to GET Return quantity for product which not in distributor product sector and get 200 OK
    [Documentation]    Able to get Return using product which not assigned at product sector
    [Tags]       distadm    9.1.1   NRSZUANQ-40112
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user gets reason by using code 'RG06' and 'RG'
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdActPS'
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${AppSetupDetails}=    create dictionary
    ...    MAKE_REFERENCE_NUMBER_MANDATORY=${False}
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    Given user retrieves token access as hqadm
    When user assigned product sector using fixed data
    And user retrieves details of application setup
    And user updates app setup details using fixed data
    ${rtn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    And user post return with fixed data
    Then expected return status code 200
    And user unassigned product sector using fixed data
    Given user retrieves token access as ${user_role}
    When user retrieves return product by id with id validation
    Then expected return status code 200

5 - Able to GET Return with inactive product and get 200 OK
    [Documentation]    Able to get Return using inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40113
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user gets reason by using code 'RG06' and 'RG'
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'PRDInc'
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
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
    When user retrieves return product by id with id validation
    Then expected return status code 200

6 - Able to GET Return with blocked product and get 200 OK
    [Documentation]    Able to get Return using blocked product
    [Tags]      distadm    9.1.1   NRSZUANQ-40115
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user gets reason by using code 'RG06' and 'RG'
    ...    AND       user retrieves reason warehouse
    ...    AND       user retrieves prd by prd code 'AdeBlo1'
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user assigned product sector using fixed data
    And user updates product with fixed data
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
    When user retrieves return product by id with id validation
    Then expected return status code 200

7 - Able to retrieve Return and verify taxable amount
    [Documentation]    Able to get prime return with tax
    [Tags]       distadm    9.1.1    NRSZUANQ-42291
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user retrieves cust by using name 'CXTESTTAX'
    ...    AND       user retrieves token access as distadm
    ...    AND       user gets reason by using code 'RG06' and 'RG'
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
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user post return with random data
    Then expected return status code 200
    When user retrieves return product by id with id validation
    Then expected return status code 200

8 - Able to retrieve draft Return using ID
    [Documentation]    Able to retrieve draft return transactions using id
    [Tags]    distadm    9.3
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
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then update return to draft status
    When user retrieves return by id
    Then expected return status code 200

9 - Validate customer group discount amount on sales return header level
    [Documentation]    Validate customer group discount amount on sales return header level
    [Tags]      distadm    9.3
    [Setup]    run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user gets distributor by using code 'DistEgg'
    ...    AND       user gets route by using code 'Rchoon'
    ...    AND       user gets cust by using code 'CT0000001549'
    ...    AND       user creates prerequisite for reason 'Return - Good Stock'
    ...    AND       user assigns both warehouse to reason
    ...    AND       user retrieves reason warehouse
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
    When user retrieves return by id
    And validate the customer group discount is retrieved correctly

10 - Able to retrieve all return invoice
    [Documentation]    Able to retrieve all return invoice
    [Tags]    distadm    9.3
    Given user retrieves token access as ${user_role}
    And user retrieves cust by using name 'CXTESTTAX'
    When user retrieves all return invoice
    Then expected return status code 200
