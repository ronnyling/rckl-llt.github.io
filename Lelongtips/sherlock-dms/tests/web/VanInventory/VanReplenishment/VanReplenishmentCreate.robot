*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/VanInventory/VanReplenishment/VanReplenishmentAddPage.py
Library         ${EXECDIR}${/}resources/web/VanInventory/VanReplenishment/VanReplenishmentListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py

*** Test Cases ***


1 - Unable to add product which not in distributor product sector
    [Documentation]    Unable to create van replenishment using product which not linked to product sector
    [Tags]     distadm     9.1.1    NRSZUANQ-40889
    ${ProductSectorDetails}=     create dictionary
    ...    productSector= Van Prod PS02
    Given user retrieves token access as hqadm
    When user gets distributor by using code 'DistEgg'
    Then user unassigned product sector using fixed data
    ${RepDetails}=    create dictionary
    ...    principal=Prime
    ...    route=RTVB05
    ...    warehouse=VBWH01
    ...    product=VBProd004
    Given user navigates to menu Van Inventory | Van Replenishment
    When user provides van replenishment header details
    Then product not populated in dropdown

2 - Unable to add inactive product
    [Documentation]    Unable to create van replenishment using inactive product
    [Tags]     distadm     9.1.1    NRSZUANQ-40893
    ${update_product_details}=    create dictionary
    ...    STATUS=Inactive
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'VBProd006'
    Then user updates product with fixed data
    ${RepDetails}=    create dictionary
    ...    principal=Prime
    ...    route=RTVB05
    ...    warehouse=VBWH01
    ...    product=VBProd006
    Given user navigates to menu Van Inventory | Van Replenishment
    When user provides van replenishment header details
    Then product not populated in dropdown

3 - Unable to add blocked product
    [Documentation]    Unable to create van replenishment using blocked product
    [Tags]     distadm     9.1.1    NRSZUANQ-40897
    ${update_product_details}=    create dictionary
    ...    STATUS=Blocked
    Given user retrieves token access as hqadm
    When user retrieves prd by prd code 'VBProd007'
    Then user updates product with fixed data
    ${RepDetails}=    create dictionary
    ...    principal=Prime
    ...    route=RTVB05
    ...    warehouse=VBWH01
    ...    product=VBProd007
    Given user navigates to menu Van Inventory | Van Replenishment
    When user provides van replenishment header details
    Then product not populated in dropdown


