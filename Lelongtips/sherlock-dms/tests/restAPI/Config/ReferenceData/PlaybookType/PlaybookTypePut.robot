*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypePut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypeDelete.py

*** Test Cases ***
1 - Able to PUT Playbook Type and get 200
    [Documentation]  To update Playbook Type with random data via api
    [Tags]    hqadm     9.2    NRSZUANQ-43741
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    When user updates playbook type with random data
    Then expected return status code 200
    When user deletes playbook type with created data
    Then expected return status code 200

2 - Able to PUT Playbook Type using fixed data and get 200
    [Documentation]  To update Playbook Type with fixed data via api
    [Tags]    hqadm     9.2
    Given user retrieves token access as ${user_role}
    When user creates playbook type with fixed data
    Then expected return status code 201
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_DESC=Playbook Auto 1001
    ...    PLAYBOOK_PRD_HIER_REQ=1                #either 0 for No or 1 for Yes
    When user updates playbook type with fixed data
    Then expected return status code 200
    When user deletes playbook type with created data
    Then expected return status code 200

3 - Unable to PUT Playbook Type with invalid data and get 400
    [Documentation]  To update Playbook Type with invalid data via api
    [Tags]    hqadm     9.2    NRSZUANQ-43752
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_DESC=Playbook Auto 1001
    ...    PLAYBOOK_PRD_HIER_REQ=123                #invalid data as either 0 and 1 allows
    When user updates playbook type with invalid data
    Then expected return status code 400
    When user deletes playbook type with created data
    Then expected return status code 200

4 - Unable to PUT Playbook Type using distributor access and get 403
    [Documentation]  To update Playbook Type using distributor access via api
    [Tags]    distadm     9.2    NRSZUANQ-43754
    Given user retrieves token access as hqadm
    When user creates playbook type with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user updates playbook type with random data
    Then expected return status code 403
    Given user retrieves token access as hqadm
    When user deletes playbook type with created data
    Then expected return status code 200
