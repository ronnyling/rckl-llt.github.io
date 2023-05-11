*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Distributor/DistributorTrxNumAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/Config/DistConfig/DistConfigPost.py

Test Teardown   run keywords
...    user selects distributor transaction number to delete
...    AND     distributor transaction number deleted successfully with message 'Record deleted'
...    AND     user logouts and closes browser

*** Test Cases ***
1 - Able to create Distributor Transaction number with random data
    [Documentation]    Able to create Distributor transaction number using random data
    [Tags]    distadm   9.0
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user creates distributor transaction number with random data
    Then distributor transaction number created successfully with message 'Record created'

2 - Able to create Distributor Prime Transaction number with fixed data
    [Documentation]    Able to create Distributor prime transaction number using fixed data
    [Tags]    distadm   9.1     NRSZUANQ-29996
    ${DistTrxNumDetails}=      create dictionary
    ...    TXN_TYPE=Invoice
    ...    PRIME_FLAG=Prime
    ...    PREFIX=TIN
    ...    START_NUM=100
    ...    END_NUM=999
    set test variable    ${DistTrxNumDetails}
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user creates distributor transaction number with fixed data
    Then distributor transaction number created successfully with message 'Record created'

3 - Able to create Distributor Non-Prime Transaction number with fixed data
    [Documentation]    Able to create Distributor non-prime transaction number using fixed data
    [Tags]    distadm   9.1     NRSZUANQ-30002
    ${DistTrxNumDetails}=      create dictionary
    ...    TXN_TYPE=Invoice
    ...    PRIME_FLAG=Non-Prime
    ...    PREFIX=TIN
    ...    START_NUM=100
    ...    END_NUM=999
    set test variable    ${DistTrxNumDetails}
    Given user switches On multi principal
    And user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user creates distributor transaction number with fixed data
    Then distributor transaction number created successfully with message 'Record created'

4 - Unable to View Prime/Non-Prime field in Transaction Number when Multi Principal = Off
    [Documentation]    Unable to view principal field in Distributor transaction number during creation
    [Tags]    distadm   9.1    NRSZUANQ-30009
    Given user switches Off multi principal
    And user navigates to menu Master Data Management | Distributor
    When user selects distributor to edit
    And user creates distributor transaction number with random data
    Then distributor transaction number created successfully with message 'Record created'
    And user switches On multi principal
