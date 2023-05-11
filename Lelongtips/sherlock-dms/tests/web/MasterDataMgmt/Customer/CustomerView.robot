*** Settings ***
Resource          ${EXECDIR}${/}tests/web/common.robot
Library           ${EXECDIR}${/}resources/web/MasterDataMgmt/Customer/CustomerListPage.py
Library           Collections


*** Test Cases ***
1 - Able to view specified Customer's POSM data
    [Documentation]    Able to view Customer's POSM data
    [Tags]    hqadm    distadm2     9.1
    ${CUSTOMER}=    create dictionary
    ...     CD=CT0000001547
    ...     POSMCD=POSM0056
    set test variable  &{CUSTOMER}
    Given user navigates to menu Master Data Management | Customer
    When user searches customer with code
    And user go to POSM tab
    Then user validates the POSM data
