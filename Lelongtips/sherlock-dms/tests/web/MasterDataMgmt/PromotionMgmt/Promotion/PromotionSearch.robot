*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py


*** Test Cases ***
1 - Able to search created promotion successfully
    [Documentation]    Able to search promotion on promotion listing
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=DIST_PROMO
    ...    promo_desc=Distributor Promo
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    Then promotion listed successfully in listing