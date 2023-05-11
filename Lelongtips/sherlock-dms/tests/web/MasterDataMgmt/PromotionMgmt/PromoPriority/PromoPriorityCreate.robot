*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/PromoPriority/PromoPriorityAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/PromoPriority/PromoPriorityListPage.py

*** Test Cases ***
1 - Create new promotion priority with RandomData
    [Documentation]    To test creating new promotion priority with Random Data
    [Tags]      sysimp   hqadm   hquser    9.0
    Given user navigates to menu Master Data Management | Promotion Management | Promotion Priority
    When user creates promo priority using random data
    Then promotion priority created successfully with message 'Record created successfully'
    When user selects promo priority to delete
    Then promotion priority deleted successfully with message 'Record deleted'

2 - Create new promotion priority with FixedData
    [Documentation]    To test creating new promotion priority with Fixed Data
    [Tags]      sysimp   hqadm   hquser    9.0
    ${PromoPriorityDetails}=    create dictionary
    ...    priorityDesc=Test priority desc
    Given user navigates to menu Master Data Management | Promotion Management | Promotion Priority
    When user creates promo priority using fixed data
    Then promotion priority created successfully with message 'Record created successfully'
    When user selects promo priority to delete
    Then promotion priority deleted successfully with message 'Record deleted'
