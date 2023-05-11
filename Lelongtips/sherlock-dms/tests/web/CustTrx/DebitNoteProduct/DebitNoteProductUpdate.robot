*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Unable to edit principal field in edit screen
    [Documentation]    To update debit note product using fixed data
    [Tags]    distadm    9.1
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=ProdAde1
    ...    productUom=PCK:2,PC:4
    set test variable     ${DNDetails}
    Given user switches On multi principal
    And user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note product created successfully with message 'Record added'
    When user selects debit note product to edit
    Then principal in debit note product showing disabled

2 - Validate error message prompt when product is unassigned from product sector
    [Documentation]    To validate error message prompt when product is unassigned from product sector and user trying to confirm it
    [Tags]     distadm    9.1.1
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector
    user assigned product sector using fixed data
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'
    When user unassigned product sector using fixed data
    And user selects debit note product to edit
    And user clicks on save and confirm button
    Then error message prompts successfully with message 'must be removed before saving'

3 - Unable to add blocked product in existing debit note product
    [Documentation]    To validate block product is hidden from product selection
    [Tags]     distadm    9.1.1    NRSZUANQ-40050    NRSZUANQ-40047
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector1
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user assigned product sector using fixed data
    expected return either status code 201 or status code 409
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    user retrieves token access as hqadm
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    ...    SELLING_IND=1
    user retrieves token access as hqadm
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    When user selects debit note product to edit
    set test variable    ${product_code}    LCPdt
    Then block product is shown successfully on the product listing
    And user unable to add new block product successfully

4 - Able to view and add inactive product in existing debit note product
    [Documentation]    To validate existing inactive product is shown
    [Tags]     distadm    9.1.1    NRSZUANQ-40037    NRSZUANQ-40038    BUG:NRSZUANQ-41276
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    user retrieves token access as hqadm
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    ...    SELLING_IND=1
    user retrieves token access as hqadm
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    When user selects debit note product to edit
    set test variable    ${product_code}    LCPdt
    Then inactive product is shown successfully on the product listing
    And user able to add new inactive product successfully

5 - Able to view and unable to add product without product sector in existing debit note product
    [Documentation]    To validate existing inactive product is shown
    [Tags]     distadm    9.1.1    NRSZUANQ-40028    NRSZUANQ-40029
    ${update_product_details}=    create dictionary
    ...    STATUS=Active
    ...    SELLING_IND=1
    user retrieves token access as hqadm
    user switches On multi principal
    user retrieves prd by prd code 'LCPdt'
    user updates product with fixed data
    expected return status code 200
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=LC Pdt Sector1
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user assigned product sector using fixed data
    expected return either status code 201 or status code 409
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user creates Prime debit note product using fixed data
    Then debit note created successfully with message 'Record added'
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user unassigned product sector using fixed data
    expected return status code 200
    When user selects debit note product to edit
    set test variable    ${product_code}    LCPdt
    Then unassigned product sector product is shown successfully on the product listing
    And user unable to add new unassigned product sector product successfully