*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/Sampling/SamplingAssignmentPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py


*** Test Cases ***
1 - User able to create assignment for sampling using hq admin login
    [Documentation]  To validate user able to create assignment for sampling using hq admin login
    [Tags]    hqadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Sampling
    When user selects sampling to edit
    And user creates Level:Country assignment for sampling
    Then sampling assignment created successfully with message 'Record added successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'

2 - User able to create assignment for sampling using distributor login
    [Documentation]  To validate user able to create assignment for sampling using distributor login
    [Tags]    distadm    9.3
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Sampling
    When user selects sampling to edit
    And user creates Level:Sales Office assignment for sampling
    Then sampling assignment created successfully with message 'Record added successfully'
    When user selects sampling to delete
    Then sampling deleted successfully with message 'Record deleted'