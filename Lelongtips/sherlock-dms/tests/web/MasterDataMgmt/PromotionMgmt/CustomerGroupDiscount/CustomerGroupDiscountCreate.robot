*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/CustomerGroupDiscount/CustomerGroupDiscountAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/CustomerGroupDiscount/CustomerGroupDiscountListPage.py

*** Test Cases ***
1 - Able to create customer group discount using random data
    [Documentation]    Able to create customer group discount using random data
    [Tags]    hqadm    9.3
    Given user navigates to menu Master Data Management | Promotion Management | Customer Group Discount
    When user creates customer group discount with random data
    Then validate customer group discount is created successfully