*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/hht_api/Gamification/GamificationGet.py
Library           ${EXECDIR}${/}resources/hht_api/Distributor/DistributorGet.py

Test Setup        user gets distributor by using code 'DistPotato01'

*** Test Cases ***
1 - Able to retrieve Gamification Setup Header
    [Documentation]    Able to retrieve Gamification Setup Header
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Setup Header using Salesperson
    Then expected return status code 403

2 - Able to retrieve Gamification Ranking Setup
    [Documentation]    Able to retrieve Gamification Ranking Setup
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Ranking using Salesperson
    Then expected return status code 403

3 - Able to retrieve Gamification Team and Salesperson Setup
    [Documentation]    Able to retrieve Gamification Team and Salesperson Setup
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Team and Salesperson Setup using Salesperson
    Then expected return status code 403

4 - Able to retrieve Gamification Badge Setup Header
    [Documentation]    Able to retrieve Gamification Badge Setup Header
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Badge Setup using Salesperson
    Then expected return status code 403

5 - Able to retrieve Gamification Badge Attachment Setup
    [Documentation]    Able to retrieve Gamification Badge Attachment Setup
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Badge Attachment Setup
    Then expected return status code 403

6 - Able to retrieve Gamification Leaderboard
    [Documentation]    Able to retrieve Gamification Leaderboard
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Leaderboard
    Then expected return status code 403

7 - Able to retrieve Gamification Route Rank
    [Documentation]    Able to retrieve Gamification Route Rank
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Route Rank
    Then expected return status code 403

8 - Able to retrieve Gamification Route Badge
    [Documentation]    Able to retrieve Gamification Route Badge
    [Tags]    salesperson    Gamification    9.1
    Given user retrieves token access as salesperson
    When user retrieves Gamification Route Badge
    Then expected return status code 403