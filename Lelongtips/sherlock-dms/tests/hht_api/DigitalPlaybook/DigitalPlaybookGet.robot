*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/DigitalPlaybook/DigitalPlaybookGet.py


*** Test Cases ***
1 - Able to retrieve playbook
    [Documentation]    Able to retrieve playbook from Back Office
    [Tags]    salesperson    DigitalPlaybook    9.2    NRSZUANQ-43982
    Given user retrieves token access as ${user_role}
    When user retrieves playbook
    Then expected return status code 200

2 - Able to retrieve playbook content
    [Documentation]    Able to retrieve playbook content from Back Office
    [Tags]    salesperson    DigitalPlaybook    9.2    NRSZUANQ-43982
    Given user retrieves token access as ${user_role}
    When user retrieves playbook content
    Then expected return status code 200

3 - Able to retrieve playbook assignment
    [Documentation]    Able to retrieve playbook assignment from Back Office
    [Tags]    salesperson    DigitalPlaybook    9.2    NRSZUANQ-43982
    Given user retrieves token access as ${user_role}
    When user retrieves playbook assignment
    Then expected return status code 200

4 - Able to retrieve playbook content history
    [Documentation]    Able to retrieve playbook content history from Back Office
    [Tags]    salesperson    DigitalPlaybook    9.2    NRSZUANQ-43983
    Given user retrieves token access as ${user_role}
    When user retrieves playbook content history
    Then expected return status code 200
