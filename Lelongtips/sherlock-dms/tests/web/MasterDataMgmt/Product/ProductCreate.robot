*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Product/ProductListPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py

*** Test Cases ***
1 - Able to create product using random data
    [Documentation]    Able to create product using random data
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    When user back to listing page
    And user selects product to delete
    Then product delete successfully with message 'Record deleted'

2 - Able to delete created product
    [Documentation]    Able to delete created product
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    When user back to listing page
    And user selects product to delete
    Then product delete successfully with message '1 record(s) deleted'

3 - Able to edit created product
    [Documentation]    Able to delete created product
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user creates product with random data
    Then product created successfully with message 'Record created'
    And user back to listing page
    When user selects product to edit
    And user edits product with random data
    Then product updated successfully with message 'Record updated successfully'
    When user selects product to delete
    Then product delete successfully with message 'Record deleted'

4 - Validate product priority column is removed from listing page
    [Documentation]    Able to create warehouse using given data
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    Then validated product priority is removed from listing_page

5 - Validate component is removed from product type drop down
    [Documentation]    Validate component is removed from product type drop down
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user lands on product add mode
    Then validated components is not exists in type drop down

6 - Validate product description 1 is renamed to product description
    [Documentation]    Validate component is removed from product type drop down
    [Tags]    hqadm
    Given user navigates to menu Master Data Management | Product
    When user lands on product add mode
    Then validate product description 1 is renamed to product description

7 - Able to create product using random data
    [Documentation]    Able to create product using random data
    [Tags]    hqadm    123asdsad
    Given user navigates to menu Master Data Management | Product
    ${ProductDetails} =  create dictionary
    ...   Type=POSM
    When user creates product with given data
    Then product created successfully with message 'Record created'
    And validated POSM Material tab will appear when product type = posm

8 - Validate product assignment pop up shown in table view
    [Documentation]    Able to view product assignment pop up shown in table view
    [Tags]    hqadm    9.2    NRSZUANQ-46620
    Given user navigates to menu Master Data Management | Product
    When user validates product hierarchy popup
    Then close product hierarchy pop up

9 - Able to add product hierarchy
    [Documentation]    Able to add product single product hierarchy
    [Tags]    hqadm    9.2    NRSZUANQ-46620
    Given user navigates to menu Master Data Management | Product
    When user validates product hierarchy popup
    Then user adds single product hierarchy in product master

10 - Unable to add multiple product hierarchy
    [Documentation]    Unable to add multiple product hierarchy
    [Tags]    hqadm    9.2    NRSZUANQ-46620
    Given user navigates to menu Master Data Management | Product
    When user validates product hierarchy pop up
    Then user adds multiple product hierarchy in product master
    And close product hierarchy pop up

11 - Unable to add empty product hierarchy
    [Documentation]    Unable to add multiple product hierarchy
    [Tags]    hqadm    9.2    NRSZUANQ-46620
    Given user navigates to menu Master Data Management | Product
    When user validates product hierarchy pop up
    Then user adds empty product hierarchy in product master
    And close product hierarchy pop up

12 - Able to update product hierarchy
    [Documentation]    Able to update product hierarchy
    [Tags]    hqadm    9.2    NRSZUANQ-46620
    Given user navigates to menu Master Data Management | Product
    When user validates product hierarchy pop up
    And user adds single product hierarchy in product master
    Then user updates single product hierarchy

13 - Able to search product hierarchy by inline search function
    [Documentation]    Able to search product hierarchy by inline search function
    [Tags]    hqadm    9.2    NRSZUANQ-46620
    Given user retrieves token access as ${user_role}
    When user get hierarchy id by giving hierarchy structure name General Product Hierarchy
    And user retrieves product hierarchy structure with valid data
    And user navigates to menu Master Data Management | Product
    And user validates product hierarchy pop up
    Then user validates product hierarchy inline search