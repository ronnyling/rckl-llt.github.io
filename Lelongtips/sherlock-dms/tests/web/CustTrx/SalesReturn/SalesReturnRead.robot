*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py

*** Test Cases ***
1 - Verify Principal default to Prime in SalesReturn when Multi Principal = On
    [Documentation]    Verify SalesReturn having Principal = Prime when multi principal = On
    [Tags]     distadm    9.1   NRSZUANQ-33162
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Sales Return
    Then table column Principal is displaying in table listing
    When user searches return with Prime data
    And principal listed successfully in return

2 - Verify Principal not displaying in Sales Return when Multi Principal = Off
    [Documentation]    Verify SalesReturn not having Principal field when multi principal = Off
    [Tags]     distadm    9.1    NRSZUANQ-33158
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Sales Return
    Then table column not displaying when nonprime data not in listing
    And user switches On multi principal

3 - Unable to view SalesReturn listing by using HQ access
    [Documentation]    Verify SalesReturn module is not visible by hq user
    [Tags]     hqadm    9.1    NRSZUANQ-33169
    When user validates Return module is not visible
    Then menu Return not found

4 - Able to view product which not in distributor product sector
    [Documentation]    Able to view Sales Return with product which not linked to product sector
    [Tags]     distadm     9.1.1    NRSZUANQ-40065   NRSZUANQ-40067
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PS A Test
    Given user retrieves token access as hqadm
    When user gets distributor by using code 'DistEgg'
    Then user assigned product sector using fixed data
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=AdAct1
    ...    productUom=PC1:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    When user unassigned product sector using fixed data
    And user selects return to edit
    Then product displayed in details correctly

5 - Able to view existing product which is inactive
    [Documentation]    Able to create Sales Return using inactive product
    [Tags]     distadm     9.1.1    NRSZUANQ-40072   NRSZUANQ-40242
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdInAct1'
    And user updates product with fixed data
    Then expected return status code 200
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=AdInAct1
    ...    productUom=EA:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    When user selects return to edit
    Then product displayed in details correctly
    And orange colour hidden successfully in product selection

6 - Able to view blocked product
    [Documentation]    Unable to create Sales Return using blocked product
    [Tags]     distadm     9.1.1    NRSZUANQ-40076    NRSZUANQ-41375   NRSZUANQ-40079  NRSZUANQ-41172
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=AdeBlo1
    ...    productUom=PC1:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    When user selects return to edit
    Then product displayed in details correctly
    When user saves and confirm created return
    Then return created successfully with message 'Record Updated'
    When user selects return to edit
    Then orange colour hidden successfully in product selection

7 - Validate orange colour hidden for active product during ADD, EDIT, VIEW mode
    [Documentation]    Validate orange colour hidden for active product during ADD, EDIT, VIEW mode
    [Tags]     distadm    9.1   NRSZUANQ-41174    NRSZUANQ-41172    testing11
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector1
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user assigned product sector using fixed data
    expected return either status code 201 or status code 409
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    ${ReturnDetails}=    create dictionary
    ...    principal=Non-Prime
    ...    route=REgg02
    ...    customer=Salted Egg
    ...    Type=Good Return
    ...    product=AdNP1001
    ...    productUom=D01:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    When user selects return to edit
    Then orange colour hidden successfully in product selection
    And user saves and confirm created return
    Then return updated successfully with message 'Record Updated'
    When user selects return to edit
    Then orange colour hidden successfully in product selection

8 - Able to validate colour code for confirmed return with existing product which is inactive
    [Documentation]    Able to validate colour code is hidden during VIEW mode
    [Tags]     distadm     9.1.1    NRSZUANQ-4137411    NRSZUANQ-41172
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdInAct1'
    And user updates product with fixed data
    Then expected return status code 200
    ${ReturnDetails}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=AdInAct1
    ...    productUom=EA:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user confirms return with fixed data after creates
    Then return created successfully with message 'Record created successfully'
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user updates product with fixed data
    Then expected return status code 200
    When user selects return to edit
    Then orange colour hidden successfully in product selection

9 - Able to VIEW draft return
    [Documentation]    Able to view draft return
    [Tags]    distadm    9.3
    ${rtn_header_details}=    create dictionary
    ...    CUST=CXTESTTAX
    ...    PRIME_FLAG=PRIME
    Given user retrieves token access as ${user_role}
    And user gets distributor by using code 'DistEgg'
    And user gets route by using code 'Rchoon'
    And user gets cust by using code 'CT0000001074'
    And user creates prerequisite for reason 'Return - Good Stock'
    And user assigns both warehouse to reason
    And user retrieves reason warehouse
    And user retrieves prd by prd code 'AdNP1001'
    And user switches On multi principal
    And user retrieves prd by prd code 'AdPrdTTax'
    And user retrieves token access as ${user_role}
    When user post return with fixed data
    Then update return to draft status
    When user navigates to menu Customer Transaction | Sales Return
    Then user selects return to view