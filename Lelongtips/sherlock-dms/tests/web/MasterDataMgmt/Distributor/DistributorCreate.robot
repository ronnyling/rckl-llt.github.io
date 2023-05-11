*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorPost.py

*** Test Cases ***

1 - Able to Create Distributor with given data
    [Documentation]    Able to create distributor with given data
    [Tags]     sysimp  9.0
    ${DistDetails}=    create dictionary
    ...    DistCode=Dist12345
    ...    DistName=TestDist
    ...    PrcGrp=GANG_PRICE_GRP
    ...    OthProdTypePrcGrp=PGE2E1
    ...    Timezone=Asia/Kolkata - India Standard Time
    ...    date=today
    ...    PrcGrp=GANG_PRICE_GRP
    ...    OthProdTypePrcGrp=PGE2E1
    set test variable     &{DistDetails}
    Given user navigates to menu Master Data Management | Distributor
    When user saves the distributor by given data
    Then Distributor created successfully with message 'Record created'

2 - Able to Create Distributor with random data
    [Documentation]    Able to create distributor with random data
    [Tags]     sysimp  9.0
    ${DistDetails}=    create dictionary
    ...    DistCode=random
    ...    DistName=random
    ...    Timezone=Asia/Kolkata - India Standard Time
    ...    date=random
    ...    PrcGrp=GANG_PRICE_GRP
    ...    OthProdTypePrcGrp=PGE2E1
    set test variable     &{DistDetails}
    Given user navigates to menu Master Data Management | Distributor
    When user saves the distributor by random data
    Then Distributor created successfully with message 'Record created'

