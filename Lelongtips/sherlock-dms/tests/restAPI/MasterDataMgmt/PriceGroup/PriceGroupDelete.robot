*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupDelete.py

Test Setup      run keywords
...    user retrieves token access as ${user_role}
...    AND    user creates price group with random data

*** Test Cases ***
1 - Able to delete created price group
    [Documentation]    To delete created price group via API
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    And user creates price group with random data
    When user deletes price group
    Then expected return status code 200
