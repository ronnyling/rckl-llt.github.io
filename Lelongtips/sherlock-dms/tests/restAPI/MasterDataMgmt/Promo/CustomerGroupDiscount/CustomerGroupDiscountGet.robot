*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/CustomerGroupDiscount/CustomerGroupDiscountGet.py

*** Test Cases ***
1 - Able to retrieve all customer group disc
    [Documentation]    To retrieve all customer group disc
    [Tags]     distadm      hqadm    9.3
    Given user retrieves token access as ${user_role}
    When user gets all customer group disc
    Then expected return status code 200

2 - Able to retrieve customer group disc by id
    [Documentation]    To retrieve customer group disc by id
    [Tags]     distadm      hqadm    9.3
    Given user retrieves token access as ${user_role}
    When user gets all customer group disc
    Then expected return status code 200
    When user gets customer group disc by id
    Then expected return status code 200