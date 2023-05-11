*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DynamicHierarchy/HierarchyStructure/StructureGet.py

Test Teardown   run keywords
...    user logouts and closes browser

*** Test Cases ***
1 - Able to Create Customer with given data
    [Documentation]    Able to create customer with fixed data
    [Tags]     distadm    9.0    9.1     NRSZUANQ-34979   NRSZUANQ-34976
    ${CustDetails}=    create dictionary
    ...    CustName=TestDist
    ...    TaxState=004
    ...    CustType=Cash
    ...    PriceGroup=AdePG1
    ...    RegType=Unregistered
    ...    TaxExempt=Tax Exempted
    ...    TaxRegNo=91919191
    ...    TaxExemptNo=7890789
    ...    Address1=No99
    ...    Address2=testing2
    ...    Address3=testing3
    ...    Postal=45000
    set test variable     &{CustDetails}
    Given user navigates to menu Master Data Management | Customer
    When user creates customer using fixed data
    Then customer created successfully with message 'Record created'

2 - Able to Create Customer with random data
    [Documentation]    Able to create customer with random data
    [Tags]     distadm    9.0
    Given user navigates to menu Master Data Management | Customer
    When user creates customer using random data
    Then customer created successfully with message 'Record created'

3 - Able to Create Customer with credit type
    [Documentation]    Able to create customer with credit type
    [Tags]     distadm    9.1     NRSZUANQ-34980    NRSZUANQ-34977
    ${CustDetails}=    create dictionary
    ...    CustName=TestDist2
    ...    TaxState=004
    ...    CustType=Credit
    ...    Terms=3days
    ...    CreditLimit=1000
    ...    PriceGroup=AdePG1
    ...    TaxExempt=Taxable
    ...    RegType=Unregistered
    ...    TaxGroup=AdeTGC01
    ...    TaxRegNo=91919191
    ...    TaxExemptNo=7890789
    ...    Address1=No99
    ...    Address2=testing2
    ...    Address3=testing3
    ...    Postal=45000
    set test variable     &{CustDetails}
    Given user navigates to menu Master Data Management | Customer
    When user creates customer using fixed data
    Then customer created successfully with message 'Record created'

4 - Validate customer assignment pop up shown in table view
    [Documentation]    Able to view customer assignment pop up shown in table view
    [Tags]    distadm    9.2    NRSZUANQ-46621
    Given user navigates to menu Master Data Management | Customer
    When user validates customer hierarchy popup
    Then close customer hierarchy pop up

5 - Able to add customer hierarchy
    [Documentation]    Able to add single customer hierarchy
    [Tags]    distadm    9.2    NRSZUANQ-46621
    Given user navigates to menu Master Data Management | Customer
    When user validates customer hierarchy popup
    Then user adds single customer hierarchy in customer master

6 - Unable to add multiple customer hierarchy
    [Documentation]    Unable to add multiple customer hierarchy
    [Tags]    distadm    9.2    NRSZUANQ-46621
    Given user navigates to menu Master Data Management | Customer
    When user validates customer hierarchy pop up
    Then user adds multiple customer hierarchy in customer master
    And close customer hierarchy pop up

7 - Unable to add empty customer hierarchy
    [Documentation]    Unable to add multiple customer hierarchy
    [Tags]    distadm    9.2    NRSZUANQ-46621
    Given user navigates to menu Master Data Management | Customer
    When user validates customer hierarchy pop up
    Then user adds empty customer hierarchy in customer master
    And close customer hierarchy pop up

8 - Able to update customer hierarchy
    [Documentation]    Able to update customer hierarchy
    [Tags]    distadm    9.2    NRSZUANQ-46621
    Given user navigates to menu Master Data Management | Customer
    When user validates customer hierarchy pop up
    And user adds single customer hierarchy in customer master
    Then user updates single customer hierarchy

9 - Able to search customer hierarchy by inline search function
    [Documentation]    Able to search product hierarchy by inline search function
    [Tags]    distadm    9.2    NRSZUANQ-46621
    Given user retrieves token access as hqadm
    When user get hierarchy id by giving hierarchy structure name General Customer Hierarchy
    And user retrieves customer hierarchy structure with valid data
    And user navigates to menu Master Data Management | Customer
    And user validates customer hierarchy pop up
    Then user validates customer hierarchy inline search