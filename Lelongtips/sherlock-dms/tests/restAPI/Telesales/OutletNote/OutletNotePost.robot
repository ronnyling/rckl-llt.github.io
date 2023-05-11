*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/Telesales/OutletNote/OutletNotePost.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/RouteMgmt/Route/RouteGet.py

Test Setup        run keywords
...    user retrieves token access as distadm
...    AND    user gets distributor by using code 'DistEgg'
...    AND    user retrieves cust by using name 'CXTESTTAX'
...    AND    user gets customer contacts
...    AND    user gets route by using code 'DSTELE10'

*** Test Cases ***
1 - Able to post outlet note with fixed data
    [Documentation]    Able to create new outlet note with fixed data
    [Tags]    telesales    hqtelesales    9.3
    ${note_details}=    create dictionary
    ...     NOTES=This is new outlet note from API
    set test variable   &{note_details}
    Given user retrieves token access as ${user_role}
    When user creates outlet note with fixed data
    Then expected return status code 201

2 - Able to post outlet note with random data
    [Documentation]    Able to create new outlet note with random data
    [Tags]    telesales    hqtelesales    9.3
    Given user retrieves token access as ${user_role}
    When user creates outlet note with random data
    Then expected return status code 201