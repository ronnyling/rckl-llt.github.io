*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/TradeAsset/TradeAssetGet.py


*** Test Cases ***
1 - Able to retrieve asset model
    [Documentation]    Able to retrieve asset model from Back Office
    [Tags]    deliveryperson    9.2    NRSZUANQ-47705
    Given user retrieves token access as ${user_role}
    When user retrieves asset model
    Then expected return status code 200

2 - Able to retrieve asset model mapping
    [Documentation]    Able to retrieve asset model mapping from Back Office
    [Tags]    deliveryperson    9.2    NRSZUANQ-47705
    Given user retrieves token access as ${user_role}
    When user retrieves asset model mapping
    Then expected return status code 200

3 - Able to retrieve trade asset type
    [Documentation]    Able to retrieve trade asset type from Back Office
    [Tags]    deliveryperson    9.2    NRSZUANQ-47705
    Given user retrieves token access as ${user_role}
    When user retrieves asset type
    Then expected return status code 200

4 - Able to retrieve asset condition
    [Documentation]    Able to retrieve asset condition from Back Office
    [Tags]    deliveryperson    9.2    NRSZUANQ-47705
    Given user retrieves token access as ${user_role}
    When user retrieves asset condition
    Then expected return status code 200

5 - Able to retrieve asset manufacturer
    [Documentation]    Able to retrieve asset manufacturer from Back Office
    [Tags]    deliveryperson    9.2    NRSZUANQ-47705
    Given user retrieves token access as ${user_role}
    When user retrieves asset manufacturer
    Then expected return status code 200
