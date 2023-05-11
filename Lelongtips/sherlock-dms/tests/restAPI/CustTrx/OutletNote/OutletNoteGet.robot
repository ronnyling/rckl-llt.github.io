*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/CustTrx/OutletNote/OutletNoteGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py

Test Setup        run keywords
...    user retrieves token access as distadm
...    AND    user gets distributor by using code 'DistEgg'
...    AND    user retrieves cust by using name 'CXTESTTAX'

*** Test Cases ***
1 - Able to retrieve all outlet note by customer
    [Documentation]    Able to retrieve all outlet note
    [Tags]    telesales    hqtelesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves all outlet note
    Then expected return status code 200

2 - Able to retrieve outlet note by customer with date filtering
    [Documentation]    Able to retrieve outlet note with date
    [Tags]    telesales    hqtelesales    9.3
    ${note_details}=    create dictionary
    ...     dateTo=2021-10-20
    ...     dateFrom=2021-10-20
    set test variable   &{note_details}
    Given user retrieves token access as ${user_role}
    When user retrieves outlet note by date
    Then expected return status code 200

3 - Validate no outlet note is returned when no matching record found
    [Documentation]    Able to retrieve all outlet note
    [Tags]    telesales    hqtelesales    9.3
    ${note_details}=    create dictionary
    ...     dateTo=2021-08-01
    ...     dateFrom=2021-08-01
    set test variable   &{note_details}
    Given user retrieves token access as ${user_role}
    When user retrieves outlet note by date
    Then expected return status code 204