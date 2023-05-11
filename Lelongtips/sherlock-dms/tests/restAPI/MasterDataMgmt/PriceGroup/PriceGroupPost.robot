*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/PriceGroup/PriceGroupDelete.py
Library           Collections

Test Teardown      user deletes price group

*** Test Cases ***
1 - Able to post Price Group with random data
    [Documentation]    Able to post Price Group with random data
    [Tags]    hqadm
    Given user retrieves token access as ${user_role}
    When user creates price group with random data
    Then expected return status code 201

2. Able to post Price Group with fixed data
    [Documentation]    Able to post Price Group with fixed data
    [Tags]    hqadm
    ${price_group_details}=     create dictionary
    ...    PRICE_GRP_DESC=MyPriceGroup
    ...    PRICE_STATUS=${True}
    Given user retrieves token access as ${user_role}
    When user creates price group with random data
    Then expected return status code 201