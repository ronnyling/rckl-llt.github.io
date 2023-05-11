*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Promotion/PromotionGet.py
Library           ${EXECDIR}${/}resources/hht_api/Supervisor/SupervisorGet.py
Library           ${EXECDIR}${/}resources/hht_api/Sampling/SamplingGet.py


*** Test Cases ***
1 - Able to retrieve sampling general info
    [Documentation]    Able to retrieve sampling general info
    [Tags]    salesperson    9.3    NRSZUANQ-52975
    Given user retrieves token access as ${user_role}
    When user retrieves sampling general info
    Then expected return status code 200

2 - Unable to retrieve sampling general info
    [Documentation]    Able to retrieve sampling general info
    [Tags]    distadm    9.3    NRSZUANQ-53292
    Given user retrieves token access as ${user_role}
    When user retrieves sampling general info
    Then expected return status code 403

3 - Able to retrieve sampling assignment
    [Documentation]    Able to retrieve sampling assignment
    [Tags]    salesperson    9.3    NRSZUANQ-52977
    Given user retrieves token access as ${user_role}
    When user retrieves sampling assignment
    Then expected return status code 200

4 - Unable to retrieve sampling general info
    [Documentation]    Able to retrieve sampling general info
    [Tags]    distadm    9.3    NRSZUANQ-53333
    Given user retrieves token access as ${user_role}
    When user retrieves sampling assignment
    Then expected return status code 403

5 - Able to retrieve sampling product assignment
    [Documentation]    Able to retrieve sampling product assignment
    [Tags]    salesperson    9.3    NRSZUANQ-52935
    Given user retrieves token access as ${user_role}
    When user retrieves sampling assignment
    Then expected return status code 200
    When user retrieves sampling product assignment
    Then expected return status code 200

6 - Unable to retrieve sampling general info
    [Documentation]    Unable to retrieve sampling product assignment
    [Tags]    distadm    9.3    NRSZUANQ-53335
    Given user retrieves token access as ${user_role}
    When user retrieves sampling assignment
    Then expected return status code 403
    When user retrieves sampling product assignment
    Then expected return status code 403

7 - Able to retrieve sampling order header
    [Documentation]    Able to retrieve sampling order header
    [Tags]    salesperson    9.3    NRSZUANQ-53415
    Given user retrieves token access as ${user_role}
    When user retrieves sampling order header
    Then expected return status code 200

8 - Able to retrieve sampling order detail
    [Documentation]    Able to retrieve sampling order detail
    [Tags]    salesperson    9.3    NRSZUANQ-53415
    Given user retrieves token access as ${user_role}
    When user retrieves sampling order detail
    Then expected return status code 200

9 - Able to retrieve sampling order and invoice product history
    [Documentation]    Able to retrieve sampling order and invoice product history
    [Tags]    salesperson    9.3    NRSZUANQ-52786
    Given user retrieves token access as ${user_role}
    When user retrieves sampling order and invoice product history
    Then expected return status code 200

10 - Able to retrieve sampling return invoice list
    [Documentation]    Able to retrieve sampling return invoice list
    [Tags]    salesperson    9.3    NRSZUANQ-53215
    Given user retrieves token access as ${user_role}
    When user retrieves sampling return invoice list
    Then expected return status code 200