*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountDelete.py

*** Test Cases ***
1 - Able to delete customer group discount
    [Documentation]    Able to delete customer group discount
    [Tags]    hqadm
    [Setup]      run keywords
    ...     user retrieves token access as ${user_role}
    ...     user get hierarchy id by giving hierarchy structure name General Customer Hierarchy
    ...     user retrieves customer hierarchy structure with valid data
    Given user retrieves token access as ${user_role}
    When user creates customer group discount
    Then expected return status code 201
    When user deletes customer group discount
    Then expected return status code 200