*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypeDelete.py

*** Test Cases ***
1 - Able to POST Playbook Type and get 201
    [Documentation]  To create Playbook Type with random data via api
    [Tags]    hqadm     9.2    NRSZUANQ-43740    NRSZUANQ-43687
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    When user deletes playbook type with created data
    Then expected return status code 200

2 - Able to POST Playbook Type using fixed data and get 201
    [Documentation]  To create Playbook Type with fixed data via api
    [Tags]    hqadm     9.2    NRSZUANQ-43740
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_DESC=Playbook Auto 1001
    ...    PLAYBOOK_PRD_HIER_REQ=1                #either 0 for No or 1 for Yes
    Given user retrieves token access as ${user_role}
    When user creates playbook type with fixed data
    Then expected return status code 201
    When user deletes playbook type with created data
    Then expected return status code 200

3 - Unable to POST Playbook Type with Existing Code and get 409
    [Documentation]  To validate unable to create Playbook Type with existing data via api
    [Tags]    hqadm     9.2    NRSZUANQ-43749
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    When user creates playbook type with existing data
    Then expected return status code 409
    When user deletes playbook type with created data
    Then expected return status code 200

4 - Unable to POST Playbook Type with Empty data and get 400
    [Documentation]  To validate unable to create Playbook Type with empty data via api
    [Tags]    hqadm     9.2     NRSZUANQ-43750
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_CD=${EMPTY}
    ...    PLAYBOOK_TYPE_DESC=${EMPTY}
    ...    PLAYBOOK_PRD_HIER_REQ=1
    Given user retrieves token access as ${user_role}
    When user creates playbook type with empty data
    Then expected return status code 400

5 - Unable to POST Playbook Type with invalid data and get 400
    [Documentation]  To validate unable to create Playbook Type with invalid data via api
    [Tags]    hqadm     9.2     NRSZUANQ-43750
    ${playbook_details}    create dictionary
    ...    PLAYBOOK_TYPE_CD=PBAutoInv
    ...    PLAYBOOK_TYPE_DESC=PB Auto Inv
    ...    PLAYBOOK_PRD_HIER_REQ=1234     #Invalid as it will only allow 0 or 1
    Given user retrieves token access as ${user_role}
    When user creates playbook type with invalid data
    Then expected return status code 400

6 - Unable to POST Playbook Type using distributor access and get 403
    [Documentation]  To validate unable to create Playbook Type using distributor admin
    [Tags]    distadm     9.2     NRSZUANQ-43753
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 403


