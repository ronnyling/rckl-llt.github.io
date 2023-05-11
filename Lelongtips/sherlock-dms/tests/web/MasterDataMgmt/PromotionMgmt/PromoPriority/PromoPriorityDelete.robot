*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/PromoPriority/PromoPriorityAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/PromoPriority/PromoPriorityListPage.py

*** Test Cases ***
1 - Able to delete promotion priority
    [Documentation]    To test able to delete promotion priority
    [Tags]      sysimp   hqadm   hquser    9.0
    Given user navigates to menu Master Data Management | Promotion Management | Promotion Priority
    When user creates promo priority using random data
    Then promotion priority created successfully with message 'Record created successfully'
    When user selects promo priority to delete
    Then promotion priority deleted successfully with message 'Record deleted'
