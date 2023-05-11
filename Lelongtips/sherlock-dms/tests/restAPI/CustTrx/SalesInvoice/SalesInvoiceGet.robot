*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoiceGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/SalesInvoice/SalesInvoicePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

Test Setup        run keywords
...               user retrieves token access as distadm
...               AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to retrieve all Invoice
    [Documentation]    Able to retrieve all invoice
    [Tags]    distadm    9.1     NRSZUANQ-31565
    Given user retrieves token access as ${user_role}
    When user retrieves all invoice
    Then expected return status code 200

2 - Able to retrieve Invoice using ID
    [Documentation]    Able to retrieve invoice transactions using id
    [Tags]    distadm    9.1     NRSZUANQ-31567
    Given user switches On multi principal
    And user retrieves token access as ${user_role}
    When user retrieves all invoice
    Then expected return status code 200
    When user retrieves invoice by id
    Then expected return status code 200

3 - Unable to GET Invoice using HQ access and get 403
    [Documentation]    Unable to retrieve invoice using other than distributor user
    [Tags]    hqadm   hquser   sysimp    9.1     NRSZUANQ-31568
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves all invoice
    Then expected return status code 403

4 - Able to GET INV quantity for product which not in distributor product sector and get 200 OK
    [Documentation]    Able to get Invoice using product which not assigned at product sector
    [Tags]       distadm    9.1.1   NRSZUANQ-40091
    [Teardown]  run keywords
    ...    user assigned product sector using fixed data
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    When user gets distributor by using code 'DistEgg'
    Then user assigned product sector using fixed data
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdActPS' with uom 'PC1:2'
    When user creates invoice with fixed data
    Then expected return status code 200
    And user unassigned single product sector
    Given user retrieves token access as ${user_role}
    When user retrieves invoice product by id
    Then expected return status code 200
    When user retrieves token access as hqadm
    Then user revert to previous setting

5 - Able to GET INV with inactive product and get 200 OK
    [Documentation]    Able to get Invoice using inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40092
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'PRDInc' with uom 'PCK:3'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user retrieves invoice product by id
    Then expected return status code 200

6 - Able to GET INV with blocked product and get 200 OK
    [Documentation]    Able to get Invoice using blocked product
    [Tags]     distadm    9.1.1   NRSZUANQ-40093
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    When user creates invoice with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user retrieves invoice product by id
    Then expected return status code 200

7 - Able to retrieve created invoice and validate delivery status is returned from api
    [Documentation]    Validate newly added column delivery status is returned from api
    [Tags]    distadm    9.2   NRSZUANQ-45479
    ${fixedData}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    INV_CUST=CXTESTTAX
    ...    INV_ROUTE=Rchoon
    ...    INV_WH=CCCC
    Given user retrieves token access as ${user_role}
    And user intends to insert product 'CNPD001' with uom 'EA:5'
    When user creates invoice with fixed data
    Then expected return status code 200
    When user retrieves created invoice
    Then expected return status code 200
    And validated delivery status is returned

8 - Validate no group discount amount is retrieved when no discount is involved
    [Documentation]    Validate no customer group discount amount is retrieved when no discount is applied
    [Tags]    distadm    9.3
    ${fixedData}=    create dictionary
    ...    INV_CUST=CXTESTTAX
    ...    INV_NO=INV0000011245
    Given user retrieves token access as ${user_role}
    When user retrieves invoice by customer and inv no
    Then validate amount retrieved without discount

9 - Validate group discount details amount is retrieved correctly when discount is applied
    [Documentation]    Validate no customer group discount amount is retrieved when no discount is applied
    [Tags]    distadm    9.3
    ${fixedData}=    create dictionary
    ...    INV_CUST=CXTESTTAX
    ...    INV_NO=INV0000011246
    Given user retrieves token access as ${user_role}
    When user retrieves invoice by customer and inv no
    Then validate amount retrieved with discount

10 - Validate no group discount details is retrieved for product without discount
    [Documentation]    Validate no customer group discount details retrieved for product without discount applied
    [Tags]    distadm    9.3
    ${fixedData}=    create dictionary
    ...    INV_CUST=CXTESTTAX
    ...    INV_NO=INV0000011245
    ...    PROD_CD=AdPrdTGross
    Given user retrieves token access as ${user_role}
    When user retrieves invoice by customer and inv no
    Then validate discount details for product without discount

11 - Validate group discount details on product is retrieved correctly
    [Documentation]    Validate customer group discount details are retrieved correctly when discount is applied on product
    [Tags]    distadm    9.3
    ${fixedData}=    create dictionary
    ...    INV_CUST=CXTESTTAX
    ...    INV_NO=INV0000011246
    ...    PROD_CD=AdPrdTGross
    Given user retrieves token access as ${user_role}
    When user retrieves invoice by customer and inv no
    Then validate discount details for product with discount



