*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonEditPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonPost.py
Library         ${EXEC_DIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/SalesPerson/SalesPersonDelete.py

Test Setup  run keywords
...    user creates salesperson as prerequisite
...    AND    user open browser and logins using user role ${user_role}

Test Teardown  run keywords
...     user deletes created salesperson as teardown
...     AND    user logouts and closes browser



*** Test Cases ***
1 - Able to Update Salesperson with fixed data
    [Documentation]    Able to update Salesperson with fixed data
    [Tags]     distadm    9.0
   ${update}=    create dictionary
   ...    update=${True}
    ${update_salesperson_details}=    create dictionary
    ...    salesperson_cd=BohnDoe
    ...    salesperson_name=BohnDoeBlue
    ...    id_number=165352
    ...    status=Active
    ...    follow_work_days=${True}
    ...    follow_holidays=${True}
    ...    handheld=${False}
    ...    add_1=The Gardens
    ...    add_2=North Tower, 35
    ...    add_3=Lingkaran Syed Putra
    ...    post_code=59200
    ...    num=0123463554
    ...    mobile=0123463554
    ...    email=JohnBlue@gmail.com
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user selects salesperson to edit
    And user updates salesperson with fixed data
    Then salesperson updated successfully with message 'Record updated successfully'

2 - Able to Update Salesperson with random data
    [Documentation]    Able to update Salesperson with random data
    [Tags]     distadm    9.0
   ${update}=    create dictionary
   ...    update=${True}
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user selects salesperson to edit
    And user updates salesperson with random data
    Then salesperson updated successfully with message 'Record updated successfully'

3 - Able to Update telesales salesperson with fixed data
    [Documentation]    Able to update telesales salesperson with fixed data
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...    user creates telesales salesperson as prerequisite
    ...    AND    user open browser and logins using user role ${user_role}
    [Teardown]    run keywords
    ...     AND    user logouts and closes browser
    ${email} =  Generate Random String      12  [NUMBERS][LOWER]
    ${update}=    create dictionary
    ...    update=${True}
    ${update_salesperson_details}=    create dictionary
    ...    salesperson_name=BohnDoeBlue
    ...    id_number=165352
    ...    status=Inactive
    ...    handheld=${False}
    ...    follow_work_days=${True}
    ...    follow_holidays=${True}
    ...    add_1=The Valley
    ...    add_2=South Tower, 35
    ...    add_3=Lingkaran Syed Putra
    ...    post_code=69200
    ...    num=0123463554
    ...    mobile=0123463554
    ...    email=${email}@gmail.com
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user selects salesperson to edit
    And user updates salesperson with fixed data
    Then salesperson updated successfully with message 'Record updated'

4 - Unable to update telesales user to enable handheld release flag
    [Documentation]    Unable to update telesales user to enable handheld release flag
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...    user creates telesales salesperson as prerequisite
    ...    AND    user open browser and logins using user role ${user_role}
    [Teardown]    run keywords
    ${email} =  Generate Random String      12  [NUMBERS][LOWER]
    ${update}=    create dictionary
    ...    update=${True}
    ${update_salesperson_details}=    create dictionary
    ...    salesperson_name=BohnDoeBlue
    ...    id_number=165352
    ...    status=Inactive
    ...    handheld=${True}
    ...    follow_work_days=${True}
    ...    follow_holidays=${True}
    ...    add_1=The Valley
    ...    add_2=South Tower, 35
    ...    add_3=Lingkaran Syed Putra
    ...    post_code=69200
    ...    num=0123463554
    ...    mobile=0123463554
    ...    email=${email}@gmail.com
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user selects salesperson to edit
    And user updates salesperson with fixed data
    Then salesperson updated successfully with message 'Update Failed'

5 - Verify telesales toogle is disabled in edit mode
    [Documentation]     Verify telesales toogle is disabled in edit mode
    [Tags]     distadm    9.3
    [Setup]      run keywords
    ...    user creates telesales salesperson as prerequisite
    ...    AND    user open browser and logins using user role ${user_role}
    [Teardown]    run keywords
    ...    user logouts and closes browser
    Given user navigates to menu Master Data Management | Route Management | Salesperson
    When user selects salesperson to edit
    Then telesales toggle is set yes and disabled
