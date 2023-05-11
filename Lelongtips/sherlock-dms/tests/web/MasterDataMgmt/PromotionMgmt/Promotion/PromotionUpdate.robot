*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionEditPage.py

*** Test Cases ***
1 - Able to update created promotion successfully
    [Documentation]    Able to update created promotion
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_code=EDPROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user updates the selected promotion
    Then promotion updated successfully with message 'Record updated'

2 - Unable to update promotion created by HQ
    [Documentation]    Unable to update promotion created by HQ
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_code=HQPROMO2
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to edit
    Then user validates unable to edit the promotion

3- Unable to update promotion that has started
    [Documentation]    Unable to update promotion with past start date
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=DIST_PROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to edit
    Then user validates unable to edit the promotion

4- Able to update promotion overall budget
    [Documentation]    Able to update promotion overall budget
    [Tags]    distadm    9.2     test
    ${PromoDetails}=    create dictionary
    ...    promo_cd=BDG_PROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to edit
    And user updates the overall budget
    Then promotion updated successfully with message 'Record updated'

5- Able to update promotion budget based on route
    [Documentation]    Able to update promotion budget based on route
    [Tags]    distadm    9.2
   ${PromoDetails}=    create dictionary
    ...    promo_cd=BDG_PROMO
    ...    route_budget=50
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to view
    And user navigates to Budget Allocation tab
    And user updates the route budget allocation
    Then promotion updated successfully with message 'Record updated'

6- Unable to update route budget assignment over than overall promotion budget
    [Documentation]    Able to update promotion budget based on route
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=BDG_PROMO
    ...    route_budget=2500
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to view
    And user navigates to Budget Allocation tab
    And user updates the route budget allocation
    Then route budget exceeded successfully with message 'Sum of Route Budget cannot exceed Distributor Budget DistEgg'

7- Unable to update budget after promotion has ended
    [Documentation]    Able to update promotion budget based on route
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=Disteggbudget
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to view
    Then user validates Promotion Budget field is disabled

8- Able to view budget allocation for promotion with budget
    [Documentation]    Able to update promotion budget based on route
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=BDG_PROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to view
    Then user validates budget tab is enabled

9- Unable to view budget allocation for promotion without budget
    [Documentation]    Unable to view budget allocation for promotion without budget
    [Tags]    distadm    9.2
    ${PromoDetails}=    create dictionary
    ...    promo_cd=DIST_PROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user searches created promotion
    And user selects promotion to view
    Then user validates budget tab is disabled