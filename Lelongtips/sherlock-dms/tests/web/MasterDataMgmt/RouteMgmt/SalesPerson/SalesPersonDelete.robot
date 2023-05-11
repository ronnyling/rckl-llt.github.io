*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonListPage.py

*** Test Cases ***
1 - Able to Delete Salesperson
    [Documentation]    Able to delete Salesperson with random data
    [Tags]     distadm    9.0
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user creates salesperson with random data
    Then salesperson created successfully with message 'Record created'
    And user clicks cancel
    When user selects salesperson to delete
    Then salesperson deleted successfully with message 'Record deleted'

2 - Able to delete telesales salesperson
    [Documentation]    Able to delete telesales salesperson
    [Tags]     hqadm    9.3
    [Setup]      run keywords
    ...     set salesperson prerequisites
    ${name} =  Generate Random String      12  [NUMBERS][LOWER]
    ${code} =   Generate Random String      6  [NUMBERS]
    ${salesperson_details}=    create dictionary
    ...    salesperson_cd=${code}
    ...    salesperson_name=${name}
    ...    id_number=12352
    ...    status=Active
    ...    follow_work_days=${True}
    ...    follow_holidays=${True}
    ...    handheld=${False}
    ...    telesales=${True}
    ...    add_1=The Gardens
    ...    add_2=North Tower, 35
    ...    add_3=Lingkaran Syed Putra
    ...    post_code=59200
    ...    num=0123463554
    ...    mobile=0123463554
    ...    email=${name}@gmail.com
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user creates salesperson with fixed data
    Then salesperson created successfully with message 'Record Added'
    When user selects salesperson to delete
    Then salesperson deleted successfully with message 'Record deleted'