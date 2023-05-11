*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountPost.py
Library          ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructurePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/HierarchyStructureDelete.py

*** Test Cases ***
1 - Able to retrieve customer group discount with active setup
    [Documentation]    Able to retrieve customer group setup for customer and product with active setup
    [Tags]    distadm    9.3
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdPrdTGross
    Given user retrieves token access as ${user_role}
    When user retrieves customer group discount with valid customer and product
    Then expected return status code 200

2 - Validate no customer group discount is retrieved without active setup
    [Documentation]    Able to retrieve customer group setup for customer and product without active setup
    [Tags]    distadm    9.3
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CGDX
    ...    PROD_CD=AdPrdTGross
    Given user retrieves token access as ${user_role}
    When user retrieves customer group discount with valid customer and product
    Then expected return status code 204

3 - Validate no customer group discount is retrieved when setup is off
    [Documentation]    Unable to retrieve customer group setup when setup is off
    [Tags]    distadm    9.3
    [Setup]    user sets the feature setup for cust group discount to off passing with 'CUST_GRP_DISC' value
    [Teardown]    user sets the feature setup for cust group discount to on passing with 'CUST_GRP_DISC' value
    ${discountDetails}=    create dictionary
    ...    CUST_NAME=CXTESTTAX
    ...    PROD_CD=AdPrdTGross
    Given user retrieves token access as ${user_role}
    When user retrieves customer group discount with valid customer and product
    Then expected return status code 204

4 - Validate no customer group discount retrieved for invalid id
    [Documentation]    Able to retrieve customer group setup for customer and product with active setup
    [Tags]    distadm    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves customer group discount with invalid customer and product
    Then expected return status code 204

5 - Able to create customer group discount with random data
    [Documentation]    Able to create new customer group disc with random data
    [Tags]    hqadm    9.3
    [Setup]      run keywords
    ...     user retrieves token access as ${user_role}
    ...     user get hierarchy id by giving hierarchy structure name General Customer Hierarchy
    ...     user retrieves customer hierarchy structure with valid data
    Given user retrieves token access as ${user_role}
    When user creates customer group discount
    Then expected return status code 201