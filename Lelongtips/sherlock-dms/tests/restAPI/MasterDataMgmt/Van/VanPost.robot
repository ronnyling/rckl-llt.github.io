*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to create Van using random data
    [Documentation]    To create valid van using random data via API
    [Tags]     distadm    9.0
    Given user retrieves token access as ${user_role}
    When user creates van with random data
    Then expected return status code 201
    When user deletes van with created data
    Then expected return status code 200

2 - Able to create Van using given data
    [Documentation]    To create valid van using given data via API
    [Tags]     distadm    9.0
    ${van_details}=   create dictionary
    ...   VAN_DESC=VanDesc
    ...   PLATE_NO=PN10001
    set test variable     &{van_details}
    Given user retrieves token access as ${user_role}
    When user creates van with fixed data
    Then expected return status code 201
    When user deletes van with created data
    Then expected return status code 200