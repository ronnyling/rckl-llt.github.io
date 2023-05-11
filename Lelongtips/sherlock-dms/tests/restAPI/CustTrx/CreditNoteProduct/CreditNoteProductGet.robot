*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteProduct/CreditNoteProductGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteProduct/CreditNoteProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonTypeGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'
...    AND    user gets route by using code 'Rchoon'
...    AND    user retrieves cust by using name 'CXTESTTAX'
...    AND    user retrieves token access as distadm
...    AND    user gets reason by using code 'RG06' and 'RG'
...    AND    user retrieves reason warehouse

*** Test Cases ***
1 - Able to retrieve all Credit Note
    [Documentation]    Able to retrieve all credit note
    [Tags]    distadm    9.1     NRSZUANQ-31475
    Given user retrieves token access as ${user_role}
    When user retrieves all credit note
    Then expected return status code 200

2 - Able to retrieve Credit Note using ID
    [Documentation]    Able to retrieve credit note using id
    [Tags]       distadm    9.1     NRSZUANQ-31476     NRSZUANQ-31699
     ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:2'
    And user creates credit note with fixed data
    Then expected return status code 200
    When user retrieves credit note by id
    Then expected return status code 200

3 - Unable to GET Credit Note using HQ access and get 403
    [Documentation]    Unable to retrieve credit note using other than distributor user
    [Tags]    hqadm   hquser   sysimp    9.1     NRSZUANQ-31568
    Given user retrieves token access as hqadm
    When user retrieves all credit note
    Then expected return status code 403

4 - Unable to retrieve Credit Note by ID using HQ access and get 403
    [Documentation]    Unable to retrieve credit note by id using other than distributor user
    [Tags]    hqadm    9.1     NRSZUANQ-31706
    Given user switches On multi principal
    set test variable      ${user_role}    hqadm
    And user retrieves token access as ${user_role}
    When user retrieves credit note by id
    Then expected return status code 403

5 - Able to GET CN quantity for product which not in distributor product sector and get 200 OK
    [Documentation]    Able to get credit note using product which not assigned at product sector
    [Tags]     distadm    9.1.1   NRSZUANQ-40198
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${AppSetupDetails}=    create dictionary
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdActPS'
    And user assigned product sector using fixed data
    When user retrieves details of application setup
    Then user updates app setup details using fixed data
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdActPS' with uom 'PC1:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    And user unassigned product sector
    Given user retrieves token access as ${user_role}
    When user retrieves credit note product by id
    Then expected return status code 200

6 - Able to GET CN with inactive product and get 200 OK
    [Documentation]    Able to get credit note using inactive product
    [Tags]     distadm    9.1.1   NRSZUANQ-40203
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    ${AppSetupDetails}=    create dictionary
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    When user retrieves details of application setup
    And user updates app setup details using fixed data
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    set test variable      ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'PRDInc' with uom 'EA:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    set test variable      ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves credit note product by id
    Then expected return status code 200

7 - Able to GET CN with blocked product and get 200 OK
    [Documentation]    Able to get credit note using blocked product
    [Tags]     distadm    9.1.1   NRSZUANQ-40204
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    ${AppSetupDetails}=    create dictionary
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    When user retrieves details of application setup
    And user updates app setup details using fixed data
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    set test variable      ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    set test variable      ${user_role}    hqadm
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    set test variable      ${user_role}    distadm
    Given user retrieves token access as ${user_role}
    When user retrieves credit note product by id
    Then expected return status code 200

8 - Able to retrieve Credit Note and verify taxable amount
    [Documentation]    Able to get prime credit note with tax
    [Tags]    distadm    9.1.1    NRSZUANQ-42292
    ${cn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    ${AppSetupDetails}=    create dictionary
    ...    DOCUMENT_NO_MANDATORY_FOR_CN_DN_RETURNS=${False}
    Given user switches On multi principal
    When user retrieves token access as hqadm
    When user retrieves details of application setup
    And user updates app setup details using fixed data
    And user retrieves token access as ${user_role}
    When user intends to insert product 'AdPrdTTax' with uom 'PC1:3'
    And user creates credit note with fixed data
    Then expected return status code 200
    When user retrieves credit note product by id
    Then expected return status code 200
