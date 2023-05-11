*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Telesales/MyStores/InboundCustomerGet.py

*** Test Cases ***
1 - Able to GET inbound customer for telesales user
    [Documentation]  To test get inbound customer for telesales user via API
    [Tags]    telesales     hqtelesales        9.3     NRSZUANQ-57710
    Given user retrieves token access as ${user_role}
    When user retrieves inbound customer listing
    Then expected return status code 200

