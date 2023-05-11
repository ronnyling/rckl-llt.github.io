*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/FeatureSetup/FeatureSetupGet.py


*** Test Cases ***
1 - Able to retrieve feature setup
    [Documentation]    Able to retrieve feature setup from Back Office
    [Tags]    salesperson    FeatureSetup    9.2    NRSZUANQ-44113
    Given user retrieves token access as ${user_role}
    When user retrieves feature setup
    Then expected return status code 200