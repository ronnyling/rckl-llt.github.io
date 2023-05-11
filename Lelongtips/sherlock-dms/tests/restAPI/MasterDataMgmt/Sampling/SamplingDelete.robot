*** Settings ***
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Sampling/SamplingDelete.py


*** Test Cases ***
1 - Able to DELETE sampling and get 200
    [Documentation]  To delete sampling via API
    [Tags]    distadm    hqadm    9.3    NRSZUANQ-52758
    Given user retrieves token access as ${user_role}
    When ${user_role} creates sampling with random data
    Then expected return status code 201
    When user deletes sampling
    Then expected return status code 200
