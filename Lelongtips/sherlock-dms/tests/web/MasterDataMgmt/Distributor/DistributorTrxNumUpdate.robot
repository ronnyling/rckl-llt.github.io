*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumEditPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

Test Setup      run keywords
...    user open browser and logins using user role ${user_role}
...    AND    user switches On multi principal
...    AND    user navigates to menu Master Data Management | Distributor
...    AND    user selects distributor to edit
...    AND    user creates distributor transaction number with given data
...    AND    distributor transaction number created successfully with message 'Record created'
Test Teardown   run keywords
...    user selects distributor transaction number to delete
...    AND     distributor transaction number deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1 - Able to update Distributor Prime Transaction number with given data
    [Documentation]    Able to create Distributor prime transaction number using given data
    [Tags]    distadm   9.1     NRSZUANQ-30003
    ${DistTrxNumDetails}=      create dictionary
    ...    TXN_TYPE=Invoice
    ...    PRIME_FLAG=Prime
    ...    PREFIX=TIN
    ...    START_NUM=100
    ...    END_NUM=999
    set test variable    ${DistTrxNumDetails}
    When user selects distributor transaction number to edit
    And user updates distributor transaction number with fixed data
    Then distributor transaction number updated successfully with message 'Record updated'

2 - Able to update Distributor Non-Prime Transaction number with given data
    [Documentation]    Able to create Distributor prime transaction number using given data
    [Tags]    distadm   9.1     NRSZUANQ-30004
    ${DistTrxNumDetails}=      create dictionary
    ...    TXN_TYPE=Invoice
    ...    PRIME_FLAG=Non-Prime
    ...    PREFIX=TIN
    ...    START_NUM=100
    ...    END_NUM=999
    set test variable    ${DistTrxNumDetails}
    When user selects distributor transaction number to edit
    And user updates distributor transaction number with fixed data
    Then distributor transaction number updated successfully with message 'Record updated'
