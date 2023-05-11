*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library          ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPut.py

*** Test Cases ***
1 - Able to update customer group discount
    [Documentation]    Able to update customer group discount
    [Tags]    hqadm    9.3
    [Setup]      run keywords
    ...     user retrieves token access as ${user_role}
    ...     user get hierarchy id by giving hierarchy structure name General Customer Hierarchy
    ...     user retrieves customer hierarchy structure with valid data
    ${GroupDiscountDetails}=   create dictionary
    ...    GRPDISC_DESC=Group Disc Description Update
    ...    REF_NO=Testing@123
    Given user retrieves token access as ${user_role}
    When user creates customer group discount
    Then expected return status code 201
    When user update customer group discount
    Then expected return status code 201