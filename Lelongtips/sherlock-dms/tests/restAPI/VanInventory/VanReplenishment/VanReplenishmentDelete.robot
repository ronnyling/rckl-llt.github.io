*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanReplenishment/VanReplenishmentPost.py
Library           ${EXECDIR}${/}resources/restAPI/VanInventory/VanReplenishment/VanReplenishmentDelete.py

*** Test Cases ***
1 - Able to delete created van replenishment
    [Documentation]    To delete created van replenishment
    [Tags]     distadm
    [Setup]  run keywords
    ...     user gets distributor by using code 'DistEgg'
    Given user retrieves token access as ${user_role}
    When user posts to van replenishment
    Then expected return status code 201
    When user deletes created van replenishment
    Then expected return status code 200
