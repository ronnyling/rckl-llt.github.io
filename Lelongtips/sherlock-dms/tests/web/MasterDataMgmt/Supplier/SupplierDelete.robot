*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Supplier/SupplierAddPage.py
*** Test Cases ***
1-Able to delete supplier
    [Documentation]    To ensure user able to delete supplier
    [Tags]   distadm    9.0
    Given user navigates to menu Master Data Management | Supplier
    When user creates supplier with randomData
    Then supplier created successfully with message 'Record created successfully'
    When user validate created supplier is listed in the table and select to delete
    Then supplier deleted successfully with message 'Record deleted'