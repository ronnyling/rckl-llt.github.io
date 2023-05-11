*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/VanInventory/VanReplenishment/VanReplenishmentAddPage.py
Library         ${EXECDIR}${/}resources/web/VanInventory/VanReplenishment/VanReplenishmentListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPut.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorProductSectorDelete.py

*** Test Cases ***
1 - Validate orange colour shown for product without product sector during EDIT
    [Documentation]    Validate orange colour shown for product without product sector during EDIT
    [Tags]     distadm    9.1.1    NRSZUANQ-40891
    ${ProductSectorDetails}=     create dictionary
    ...    productSector=Van Prod PS02
    user retrieves token access as hqadm
    user gets distributor by using code 'DistEgg'
    user assigned product sector using fixed data
    ${RepDetails}=    create dictionary
    ...    principal=Prime
    ...    route=RTVB05
    ...    warehouse=VBWH01
    ...    product=VBProd009
    ...    productUom=pr1:2
     set test variable     &{RepDetails}
    And user navigates to menu Van Inventory | Van Replenishment
    When user creates van replenishment with fixed data
    Then return created successfully with message 'Record created successfully'
    user unassigned product sector using fixed data
    When user selects created van replenishment to edit
    Then orange colour shown successfully in product selection

