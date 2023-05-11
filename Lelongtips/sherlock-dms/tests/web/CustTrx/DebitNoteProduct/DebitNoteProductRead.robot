*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/DebitNoteProduct/DebitNoteProductAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/components/RadioButton.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

*** Test Cases ***
1 - Verify principal default to prime in debit note product when multi principal = On
    [Documentation]    Verify debit note product having principal default to Prime when multi principal = On
    ...    This is not applicable to hqadm, sysimp
    [Tags]    distadm    9.1
    Given user switches On multi principal
    When user navigates to menu Customer Transaction | Debit Note (Product)
    And user creates new debit note product
    Then principal field displaying in debit note product

2 - Verify principal not displaying in debit note product when multi principal = Off
    [Documentation]    Verify debit note product not having Principal field when multi principal = Off
    ...    This is not applicable to hqadm, sysimp
    [Tags]     distadm    9.1
    Given user switches Off multi principal
    When user navigates to menu Customer Transaction | Debit Note (Product)
    And user creates new debit note product
    Then principal field not displaying in debit note product

3 - Able to view blocked product in existing confirmed debit note product
    [Documentation]    To validate existing block product is shown
    [Tags]     distadm    9.1.1    NRSZUANQ-40050    NRSZUANQ-40054
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
    When user confirms Prime debit note product using fixed data after creates
    Then debit note created successfully with message 'Record added'
    ${update_product_details}=    create dictionary
    ...    STATUS=Block
    user retrieves token access as hqadm
    user updates product with fixed data
    expected return status code 200
    When user selects debit note product to edit
    set test variable    ${product_code}    LCPdt
    Then block product is shown successfully on the product listing

4 - Able to view inactive product in existing confirmed debit note product
    [Documentation]    To validate existing inactive product is shown
    [Tags]     distadm    9.1.1    NRSZUANQ-40034    NRSZUANQ-40308    NRSZUANQ-40043    BUG:NRSZUANQ-41276
    ${update_product_details}=    create dictionary
    ...    product=LCPdt
    ...    status=Inactive
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
    When user confirms Prime debit note product using fixed data after creates
    Then debit note created successfully with message 'Record added'
    When user selects debit note product to edit
    set test variable    ${product_code}    LCPdt
    Then inactive product is shown successfully on the product listing

5 - Able to view product which is not assigned in distributor product sector for existing confirmed debit note product
    [Documentation]    To validate existing product is shown after removed from product sector
    [Tags]     distadm    9.1.1    NRSZUANQ-40031
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
    user assigned product sector using fixed data
    expected return status code 200
    ${DNDetails}=    create dictionary
    ...    route=REgg02
    ...    customer=Vege Tan
    ...    product=LCPdt
    ...    productUom=pr1:5
    Given user navigates to menu Customer Transaction | Debit Note (Product)
    When user confirms Prime debit note product using fixed data after creates
    Then debit note created successfully with message 'Record added'
    user gets distributor by using code 'DistEgg'
    user unassigned product sector using fixed data
    expected return status code 200
    When user selects debit note product to edit
    set test variable    ${product_code}    LCPdt
    Then without product sector product is shown successfully on the product listing
