*** Settings ***
Resource         ${EXECDIR}${/}tests/restAPI/common.robot
Library          ${EXECDIR}${/}resources/restAPI/Telesales/OutletNote/OutletNoteGet.py
Library          ${EXECDIR}${/}resources/restAPI/Telesales/OutletNote/OutletNoteDelete.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py
Library          ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py

Test Setup        run keywords
...    user retrieves token access as distadm
...    AND    user gets distributor by using code 'DistEgg'
...    AND    user retrieves cust by using name 'CXTESTTAX'

*** Test Cases ***
1 - Unable to delete outlet note
    [Documentation]    Unable to delete outlet note
    [Tags]    telesales    hqtelesales    9.3
    Given user retrieves token access as ${user_role}
    When user retrieves outlet note for CXTESTTAX
    Then expected return status code 200
    When user deletes valid outlet note
    Then expected return status code 404