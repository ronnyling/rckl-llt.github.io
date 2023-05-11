*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Van/VanDelete.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorGet.py

Test Setup        run keywords
...    user retrieves token access as ${user_role}
...    AND    user gets distributor by using code 'DistEgg'

*** Test Cases ***
1 - Able to update Van using fixed data
    [Documentation]    Able to update Van using fixed data
    [Tags]     distadm    9.0
    ${van_update}=   create dictionary
    ...   VAN_DESC=VanDescUpd
    ...   PLATE_NO=UPD1001
    Given user retrieves token access as ${user_role}
    When user creates van with random data
    Then expected return status code 201
    When user updates van with fixed data
    Then expected return status code 200
    When user deletes van with created data
    Then expected return status code 200