*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/PromoE2E/PromoSetup.py

*** Test Cases ***
1 - Able to delete created promotion successfully
    [Documentation]    Able to delete created promotion
    [Tags]    distadm    9.2
    [Setup]  run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user creates promotion using Discount By Value with Max Count - By Amount
    ...    AND       user open browser and logins using user role ${user_role}
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user validate created promotion is listed in the table and select to delete
    Then promotion deleted successfully with message '1 Record deleted'

2 - Unable to delete promotion created by different user
    [Documentation]    Unable to delete promotion created by different user
    [Tags]    distadm    9.2
    [Setup]  run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND       user creates promotion using Discount By Value with Max Count - By Amount
    ...    AND       user open browser and logins using user role hqadm
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    Then validate the delete icon is disabled

3 - Unable to delete promotion that has already started
    [Documentation]    Able to delete created promotion
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=DIST_PROMO
    ...    promo_desc=Distributor Promo
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    Then validate the delete icon is disabled