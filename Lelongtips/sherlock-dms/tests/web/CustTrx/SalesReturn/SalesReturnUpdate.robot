*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/SalesReturn/SalesReturnAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/CustTrx/SalesReturn/SalesReturnPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehouseGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/ReasonType/ReasonWarehousePost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py

*** Test Cases ***
1 - Validate orange colour shown for block product during EDIT
    [Documentation]    Validate orange colour shown for block product during EDIT
    [Tags]     distadm    9.1   NRSZUANQ-41169    NRSZUANQ-41172    NRSZUANQ-41375    NRSZUANQ-41172
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector1
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user assigned product sector using fixed data
    expected return either status code 201 or status code 409
    user assigned product sector using fixed data
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    Type=Good Return
    ...    product=LCPdt
    ...    productUom=pr1:5
     set test variable     &{fixedData}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    user retrieves token access as hqadm
    user updates product with fixed data
    expected return status code 200
    When user selects return to edit
    Then orange colour shown successfully in product selection

2 - Validate orange colour shown for product without product sector during EDIT
    [Documentation]    Validate orange colour shown for product without product sector during EDIT
    [Tags]     distadm    9.1   NRSZUANQ-41171    NRSZUANQ-41172
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector1
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user assigned product sector using fixed data
    expected return either status code 201 or status code 409
    user assigned product sector using fixed data
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    ${fixedData}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    Type=Good Return
    ...    product=LCPdt
    ...    productUom=pr1:5
     set test variable     &{fixedData}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    user unassigned product sector using fixed data
    expected return status code 200
    When user selects return to edit
    Then orange colour shown successfully in product selection

3 - Unable to add new product which not in distributor product sector in Edit Return
    [Documentation]    Unable to edit Sales Return using product which not linked to product sector
    [Tags]     distadm     9.1.1   NRSZUANQ-40066
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=PS A Test
    Given user retrieves token access as hqadm
    When user gets distributor by using code 'DistEgg'
    Then user assigned product sector using fixed data
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=A1001
    ...    productUom=EA:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    ${fixedData}=    create dictionary
    ...    product=AdAct1
    When user unassigned product sector using fixed data
    And user selects return to edit
    Then product not showing in dropdown

4 - Able to add new product which is inactive in Edit Return
    [Documentation]    Able to edit Sales Return using inactive product
    [Tags]     distadm     9.1.1   NRSZUANQ-40073
    ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=A1001
    ...    productUom=EA:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdInAct1'
    And user updates product with fixed data
    Then expected return status code 200
    ${fixedData}=    create dictionary
    ...    reason=GOOD1
    ...    product=AdInAct1
    ...    productUom=EA:2
    When user selects return to edit
    And user provides return details using fixed data
    And user saves return transaction
    Then return updated successfully with message 'Record Updated'

5 - Unable to add blocked product in Edit Return
    [Documentation]    Unable to edit Sales Return using blocked product
    [Tags]     distadm     9.1.1    NRSZUANQ-40078
   ${fixedData}=    create dictionary
    ...    route=Rchoon
    ...    principal=Prime
    ...    customer=CXTESTTAX
    ...    Type=Good Return
    ...    reason=GOOD1
    ...    warehouse=CCCC
    ...    product=A1001
    ...    productUom=EA:2
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Sales Return
    When user creates return with fixed data
    Then return created successfully with message 'Record created successfully'
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    ${fixedData}=    create dictionary
    ...    product=AdeBlo1
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'AdeBlo1'
    And user updates product with fixed data
    Then expected return status code 200
    When user selects return to edit
    Then product not showing in dropdown

6 - Able to update return with customer group discount
    [Documentation]    Able to update return with group discount
    [Tags]     distadm    9.3
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=Vege Tan
    ...    PROD_CD=ProdAde1
    Given user retrieves token access as ${user_role}
    And user retrieves customer group discount with valid customer and product
    When user navigates to menu Customer Transaction | Sales Return
    ${ReturnDetails}=    create dictionary
    ...    principal=Prime
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    Type=Good Return
    ...    returnMode=Partial
    ...    reason=ReasonGoodB01
    ...    product=ProdAde1
    ...    productUom=PC:1
    set test variable     &{ReturnDetails}
    Then user creates return with customer group discount
    When user selects return to edit
    Then user updates return with customer group discount

7 - Able to update draft return
    [Documentation]    Able to update draft return
    [Tags]    distadm1    9.3
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
    And user selects return to edit
    Then user updates draft return