*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanReplenishment/VanReplenishmentPost.py
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanReplenishment/VanReplenishmentPut.py

*** Test Cases ***
1 - Able to put van replenishment
    [Documentation]    To put van replenishment
    [Tags]       distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user posts to van replenishment
    Then expected return status code 201
    When user puts to save van replenishment
    Then expected return status code 200
    When user puts to confirm van replenishment
    Then expected return status code 200
