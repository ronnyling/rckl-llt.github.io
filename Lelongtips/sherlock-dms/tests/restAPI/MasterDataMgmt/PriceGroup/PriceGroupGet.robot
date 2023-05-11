*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupDelete.py


*** Test Cases ***
1 - Able to retrieve all Price Group
    [Documentation]    To retrieve all price group via API
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user retrieves all price group
    Then expected return status code 200

2 - Able to retrieve specific price group using id
    [Documentation]    To retrieve price group using given id via API
    [Tags]     hqadm
    [Setup]      run keywords
    ...    user retrieves token access as ${user_role}
    ...    AND    user creates price group with random data
    [Teardown]   user deletes price group
    Given user retrieves token access as ${user_role}
    When get price group by id
    Then expected return status code 200
