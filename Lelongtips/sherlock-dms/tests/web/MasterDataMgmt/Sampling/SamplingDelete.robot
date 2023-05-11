*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingAddPage.py


*** Test Cases ***
1 - User able to delete sampling with random data
    [Documentation]  To validate user able to delete sampling with random data
    [Tags]    hqadm    distadm    9.2
    Given user navigates to menu Master Data Management | Sampling
    When user creates sampling using random data
    Then sampling created successfully with message 'Record created successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'