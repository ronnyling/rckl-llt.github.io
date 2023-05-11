*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/WarehouseInventory/StockReceipt/StockReceiptListingPage.py
Library         ${EXECDIR}${/}resources/web/WarehouseInventory/StockReceipt/StockReceiptAddPage.py
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