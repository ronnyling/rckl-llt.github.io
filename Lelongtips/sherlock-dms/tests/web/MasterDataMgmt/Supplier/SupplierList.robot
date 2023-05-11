*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierGet.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

Test Teardown   run keywords
...    user validate created supplier is listed in the table and select to delete
...    AND     bin deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1-Able to Filter by Principal Flag in listing
    [Documentation]    To ensure user able to filter principal in supplier
    [Tags]   distadm    9.1    NRSZUANQ-27059
    [Setup]    run keywords
    ...    user switches On multi principal
    ...    AND    user open browser and logins using user role ${user_role}
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user validates is there any default supplier
    When user creates supplier with multi principal on
    Then supplier created successfully with message 'Record created successfully'
    When user filters created supplier in listing page by principal

2-Able to Search by Supplier Code in listing
    [Documentation]    To ensure user able to search supplier by supplier code
    [Tags]   distadm    9.2
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user creates supplier with multi principal on
    And supplier created successfully with message 'Record created successfully'
    When user searches created supplier in listing page by code
    Then record display in listing successfully

3-Able to Search by Supplier Name in listing
    [Documentation]    To ensure user able to search supplier by supplier name
    [Tags]   distadm    9.2
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user creates supplier with multi principal on
    And supplier created successfully with message 'Record created successfully'
    When user searches created supplier in listing page by name
    Then record display in listing successfully

4-Able to Search by Business Registration No in listing
    [Documentation]    To ensure user able to to search supplier by business registration no
    [Tags]   distadm    9.2
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user creates supplier with multi principal on
    And supplier created successfully with message 'Record created successfully'
    When user searches created supplier in listing page by businessregistration
    Then record display in listing successfully

5-Able to Search by Telephone Number in listing
    [Documentation]    To ensure user able to search supplier by telephone number
    [Tags]   distadm    9.2
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user creates supplier with multi principal on
    And supplier created successfully with message 'Record created successfully'
    When user searches created supplier in listing page by telephone
    Then record display in listing successfully

6-Able to Search by Contact Person in listing
    [Documentation]    To ensure user to search supplier by contact person
    [Tags]   distadm    9.2
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user creates supplier with multi principal on
    And supplier created successfully with message 'Record created successfully'
    When user searches created supplier in listing page by contact
    Then record display in listing successfully

7-Able to Search by Principal in listing
    [Documentation]    To ensure user able to search supplier by principal
    [Tags]   distadm    9.2
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=false
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user creates supplier with multi principal on
    And supplier created successfully with message 'Record created successfully'
    Then user searches created supplier in listing page by principal
