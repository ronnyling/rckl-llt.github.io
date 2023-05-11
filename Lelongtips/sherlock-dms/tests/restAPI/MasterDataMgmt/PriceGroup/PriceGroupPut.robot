*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupDelete.py

Test Setup      run keywords
...    user retrieves token access as ${user_role}
...    AND    user creates price group with random data
Test Teardown   user deletes price group

*** Test Cases ***
1 - Able to update Price Group using random data
    [Documentation]    To update Price Group using random data via API
    [Tags]     hqadm
    Given user retrieves token access as ${user_role}
    When user updates price group with random data
    Then expected return status code 200

2 - Able to update Price Group using fixed data
    [Documentation]    To update Price Group using fixed data via API
    [Tags]     hqadm
    ${update_price_group_details}=    create dictionary
    ...    PRICE_GRP_DESC=MyPriceGroup
    ...    PRICE_STATUS=${True}
    Given user retrieves token access as ${user_role}
    And user creates price group with random data
    Then expected return status code 201
    When user updates price group with fixed data
    Then expected return status code 200