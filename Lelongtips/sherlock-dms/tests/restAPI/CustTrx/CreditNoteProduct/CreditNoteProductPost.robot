*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/CreditNoteProduct/CreditNoteProductPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library          ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/AppSetup/GeneralPut.py

Test Setup       run keywords
...    user retrieves token access as distadm
...    AND       user gets distributor by using code 'DistEgg'
...    AND       user gets route by using code 'Rchoon'
...    AND       user gets route plan by using code 'CY0000000417'
...    AND       user creates prerequisite for reason 'Return - Good Stock'
...    AND       user assigns Prime warehouse to reason
...    AND       user retrieves reason warehouse
...    AND       user retrieves prd by prd code 'A1001'

*** Test Cases ***
1 - Able to post prime credit note and return 200
    [Documentation]    Able to post prime credit note
    [Tags]    distadm    9.1     NRSZUANQ-31698
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:2'
    And user creates credit note with fixed data
    Then expected return status code 200

2 - Able to post non prime credit note and return 200
    [Documentation]    Able to post non prime credit note
    [Tags]    distadm    9.1     NRSZUANQ-31697
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves prd by prd code 'testNp123'
    And user retrieves token access as ${user_role}
    When user intends to insert product 'testNp123' with uom 'CS:2'
    And user creates credit note with fixed data
    Then expected return status code 200

3 - Unable to post credit note with hq acess and return 403
    [Documentation]    Unable to post credit note with hqadm access
    [Tags]    hqadm    9.1     NRSZUANQ-31704
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=CXTESTTAX
    Given user retrieves prd by prd code 'testNp123'
    set test variable      ${user_role}    hqadm
    And user retrieves token access as ${user_role}
    When user intends to insert product 'testNp123' with uom 'CS:2'
    And user creates credit note with fixed data
    Then expected return status code 403

4 - Unable to post using Non-Prime Product in Prime Credit Note and get 404
    [Documentation]     Unable to post credit note using non-prime product in prime credit note
    [Tags]    distadm    9.1    NRSZUANQ-31702
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ...    PRD=testNp123
#    ${cn_body_details}=     create dictionary
#    ...    PRD_ID=D34A04AD:AB0B0E78-A993-49AD-92FF-F191499E73CC
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'A1001' with uom 'EA:2'
    And user creates credit note with non prime data
    Then expected return status code 404

5 - Unable to post using Prime Invoice in Non-Prime Credit Note and get 404
    [Documentation]     Unable to post credit note using prime invoice in non prime credit note
    [Tags]    distadm    9.1    NRSZUANQ-31703
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=NON_PRIME
    ...    CUST=CXTESTTAX
    ...    INV_ID=AEB3F490:5CB2F73B-F2C8-4356-8E6E-5C773CFD8B37
    ...    INV_NO=INV0000000407
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'testNp123' with uom 'CS:2'
    And user creates credit note with prime data
    Then expected return status code 404

6 - Unable to POST CN with product which not in distributor product sector and get 404 Not Found
    [Documentation]    Unable to post credit note using product which not assign to product sector
    [Tags]       distadm    9.1.1    NRSZUANQ-40145     prdSector
    [Teardown]  run keywords
    ...    user retrieves token access as hqadm
    ...    user assigned product sector using fixed data
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PRPRDSC
    ${AppSetupdetails}=    create dictionary
    ...     PRODUCT_ASSIGNMENT_TO_DISTRIBUTOR=${False}
    set test variable   &{AppSetupdetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    And user updates app setup general details using fixed data
    Then expected return status code 200
    When user retrieves prd by prd code 'AdActPS'
    And user unassigned product sector using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdActPS' with uom 'PC1:3'
    And user creates credit note with fixed data
    Then expected return status code 404
    When user retrieves token access as hqadm
    Then user revert to previous setting

7 - Able to POST CN with inactive product and get 200 OK
    [Documentation]    Able to post credit note using inactive product
    [Tags]    distadm    9.1.1     NRSZUANQ-40146   NRSZUANQ-40208
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    set test variable     ${user_role}   hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'PRDInc'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable     ${user_role}   distadm
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'PRDInc' with uom 'EA:3'
    And user creates credit note with fixed data
    Then expected return status code 200

8 - Unable to POST CN with blocked product and get 404 Not Found
    [Documentation]    Unable to post credit note using block product
    [Tags]    distadm    9.1.1     NRSZUANQ-40152
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    ${cn_header_details}=    create dictionary
    ...    PRIME_FLAG=PRIME
    ...    CUST=CXTESTTAX
    set test variable     ${user_role}   hqadm
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    set test variable     ${user_role}   distadm
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdeBlo1' with uom 'PC1:3'
    And user creates credit note with fixed data
    Then expected return status code 404

#----------------------------TAX------------------------------------#
1 - Able to create Credit Note with tax on gross and verify tax details
    [Documentation]    Able to post prime credit note with tax on gross
    [Tags]    distadm    9.1.1    NRSZUANQ-42292
    ${cn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdPrdTGross' with uom 'PC1:2'
    And user creates credit note with fixed data
    Then expected return status code 200

2 - Able to create Credit Note with tax on net and verify tax details
    [Documentation]    Able to post prime credit note with tax on net
    [Tags]    distadm    9.1.1    NRSZUANQ-42292
    ${cn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    When user intends to insert product 'AdPrdTNet' with uom 'PC1:2'
    And user creates credit note with fixed data
    Then expected return status code 200
