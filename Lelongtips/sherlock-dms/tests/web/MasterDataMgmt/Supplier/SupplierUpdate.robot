*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierUpdatePage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Supplier/SupplierGet.py

Test Teardown  run keywords
...    user validate created supplier is listed in the table and select to delete
...    AND     supplier deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1-Unable to Edit and change Principal Flag
    [Documentation]    To ensure user unable to edit principal in supplier
    [Tags]   distadm    9.1    NRSZUANQ-27058
    [Setup]    run keywords
    ...    user switches On multi principal
    ...    AND    user open browser and logins using user role ${user_role}
    ${supplier_details}=    create dictionary
    ...    principal=Prime
    ...    default=true
    set test variable    ${supplier_details}
    Given user navigates to menu Master Data Management | Supplier
    And user validates is there any default supplier
    When user creates supplier with multi principal on
    Then supplier created successfully with message 'Record created successfully'
    When user validate created supplier is listed in the table and select to edit
    Then user validates principal toggle is disabled

2-Able to edit supplier with random data
    [Documentation]    To ensure user able to edit supplier
    [Tags]   distadm    9.0    NRSZUANQ-27495
    Given user navigates to menu Master Data Management | Supplier
    When user creates supplier with randomData
    Then supplier created successfully with message 'Record created successfully'
    When user validate created supplier is listed in the table and select to edit
    And user updates supplier with randomData
    Then supplier created successfully with message 'Record updated successfully'

