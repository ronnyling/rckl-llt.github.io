*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonListPage.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py

#Test Setup  set salesperson prerequisites

*** Test Cases ***
1 - Able to Create Salesperson with random data
    [Documentation]    Able to create Salesperson with random data
    [Tags]     distadm    9.0
    [Setup]      run keywords
    ...     set salesperson prerequisites
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user creates salesperson with random data
    Then salesperson created successfully with message 'Record created'
    And user clicks cancel
    When user selects salesperson to delete
    Then salesperson deleted successfully with message 'Record deleted'

2 - Able to Create Salesperson with fixed data
    [Documentation]    Able to create Salesperson with fixed data
    [Tags]     distadm    9.0
    [Setup]      run keywords
    ...     set salesperson prerequisites
    ${salesperson_details}=    create dictionary
    ...    salesperson_cd=johnDoe
    ...    salesperson_name=JohnDoeBlue
    ...    id_number=12352
    ...    status=Active
    ...    follow_work_days=${True}
    ...    follow_holidays=${True}
    ...    handheld=${False}
    ...    telesales=${False}
    ...    add_1=The Gardens
    ...    add_2=North Tower, 35
    ...    add_3=Lingkaran Syed Putra
    ...    post_code=59200
    ...    num=0123463554
    ...    mobile=0123463554
    ...    email=JohnBlue@gmail.com
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user creates salesperson with fixed data
    Then salesperson created successfully with message 'Record created'
    And user clicks cancel
    When user selects salesperson to delete
    Then salesperson deleted successfully with message 'Record deleted'

3 - Able to create telesales salesperson with random data
    [Documentation]    Able to create telesales salesperson with random data
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...     set salesperson prerequisites
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user creates salesperson with random data
    Then salesperson created successfully with message 'Record Added'

4 - Able to create telesales salesperson with fixed data
    [Documentation]    Able to create telesales salesperson with fixed data
    [Tags]     distadm    9.3
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

4 - Validate handheld is disabled when telesales is selected
    [Documentation]    Validate handheld is disabled when telesales is selected
    [Tags]     distadm    9.3
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user clicks add button
    Then handheld toggle is disabled when telesales is enabled

5 - Unable to crete telesales salesperson when feature setup is off
    [Documentation]    Unable to crete telesales salesperson when feature setup is off
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...     User sets the feature setup for telesales to off passing with 'TELESALES' value
    ...     user open browser and logins using user role ${user_role}
    [Teardown]    run keywords
    ...     User sets the feature setup for telesales to on passing with 'TELESALES' value
    ...     user logouts and closes browser
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user clicks add button
    Then Is Telesales toggle is no and disabled