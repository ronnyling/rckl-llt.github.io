*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypeDelete.py

*** Test Cases ***
1 - Able to DELETE Playbook Type and get 200
    [Documentation]  To delete Playbook Type using created data via api
    [Tags]    hqadm     9.2    NRSZUANQ-43748
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    When user deletes playbook type with created data
    Then expected return status code 200

2 - Unable to DELETE Playbook Type using distributor access and get 403
    [Documentation]  To delete Playbook Type using distributor access via api
    [Tags]    distadm     9.2    NRSZUANQ-43756   DeleteDebug
    Given user retrieves token access as hqadm
    When user creates playbook type with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user deletes playbook type with created data
    Then expected return status code 403
    Given user retrieves token access as hqadm
    When user deletes playbook type with created data
    Then expected return status code 200
