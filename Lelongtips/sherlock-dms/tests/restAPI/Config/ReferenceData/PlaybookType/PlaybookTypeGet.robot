*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypePost.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypeGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypeDelete.py

*** Test Cases ***
1 - Able to GET Playbook Type and get 200
    [Documentation]  To retrieve all Playbook Type via api
    [Tags]    hqadm     9.2     NRSZUANQ-43742
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    When user gets all playbook type data
    Then expected return status code 200
    When user deletes playbook type with created data
    Then expected return status code 200

2 - Able to GET Playbook Type using id and get 200
    [Documentation]  To retrieve Playbook Type with id via api
    [Tags]    hqadm     9.2     NRSZUANQ-43742
    Given user retrieves token access as ${user_role}
    When user creates playbook type with random data
    Then expected return status code 201
    When user gets playbook type by using id
    Then expected return status code 200
    When user deletes playbook type with created data
    Then expected return status code 200

3 - Able to GET Playbook Type using distributor access and get 200
    [Documentation]  To retrieve Playbook Type with id using distributor access
    [Tags]    distadm     9.2    NRSZUANQ-43755
    Given user retrieves token access as hqadm
    When user creates playbook type with random data
    Then expected return status code 201
    Given user retrieves token access as ${user_role}
    When user gets playbook type by using id
    Then expected return status code 200
    Given user retrieves token access as hqadm
    When user deletes playbook type with created data
    Then expected return status code 200
