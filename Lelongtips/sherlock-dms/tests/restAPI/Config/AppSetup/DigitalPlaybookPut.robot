*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/DigitalPlaybookPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py

Test Setup     run keywords
...    Given user retrieves token access as ${user_role}
...    user retrieves details of application setup

Test Teardown    run keywords
...   user revert to previous setting
...   expected return status code 200

*** Test Cases ***
#not applicable to sysimp
1 - Able to update digital playbook app setup using fixed data
    [Documentation]    Able to update digital playbook app setup using fixed data
    [Tags]     hqadm    9.2     NRSZUANQ-44186    NRSZUANQ-44193
    ${AppSetupDetails}=    create dictionary
    ...    PLAYBK_PROD_HIERARCHY_LEVEL=Brand
    ...    PLAYBK_MAX_CONTENT_SIZE=200 KB      #5 MB   1 MB    500 KB   200 KB
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup digital playbook details using fixed data
    Then expected return status code 200

2 - Able to update digital playbook app setup by using empty data
    [Documentation]    Able to update digital playbook app setup by using empty data
    [Tags]     hqadm   9.2    NRSZUANQ-44188
    ${AppSetupDetails}=    create dictionary
    ...    PLAYBK_PROD_HIERARCHY_LEVEL=${null}
    ...    PLAYBK_MAX_CONTENT_SIZE=${null}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup digital playbook details using fixed data
    Then expected return status code 200

3 - Unable to update digital playbook app setup by using invalid data
    [Documentation]    Unable to update digital playbook app setup by using invalid data
    [Tags]     hqadm   9.2    NRSZUANQ-44190
    ${AppSetupDetails}=    create dictionary
    ...    PLAYBK_PROD_HIERARCHY_LEVEL=abcde
    ...    PLAYBK_MAX_CONTENT_SIZE=tetetet
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as ${user_role}
    When user updates app setup digital playbook details using fixed data
    Then expected return status code 404