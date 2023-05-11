*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Product/ProductDelete.py

*** Test Cases ***
1 - Able to delete created Product
    [Documentation]    To delete created Product via API
    [Tags]     distadm
    [Setup]    user creates random product as prerequisite
    Given user retrieves token access as ${user_role}
    When user deletes product
    Then expected return status code 200

2 - Able to delete created Product with product api
    [Documentation]    To delete created Product via API
    [Tags]     distadm
    [Setup]    user creates random product as prerequisite
    Given user retrieves token access as ${user_role}
    When user deletes created product
    Then expected return status code 200


