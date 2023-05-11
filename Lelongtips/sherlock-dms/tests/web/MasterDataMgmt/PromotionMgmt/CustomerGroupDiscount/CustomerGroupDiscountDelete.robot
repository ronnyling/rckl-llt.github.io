*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/CustomerGroupDiscount/CustomerGroupDiscountAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/CustomerGroupDiscount/CustomerGroupDiscountListPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py

*** Test Cases ***
1 - Able to delete created customer group discount
    [Documentation]    Able to delete customer group disc
    [Tags]    hqadm    9.3
    [Setup]      run keywords
    ...     user retrieves token access as ${user_role}
    ...     user get hierarchy id by giving hierarchy structure name General Customer Hierarchy
    ...     user retrieves customer hierarchy structure with valid data
    ...     user creates customer group discount
    ...     user open browser and logins using user role ${user_role}
    Given user navigates to menu Master Data Management | Promotion Management | Customer Group Discount
    When user selects customer group discount to delete
    Then discount deleted successfully with message 'Delete Success'