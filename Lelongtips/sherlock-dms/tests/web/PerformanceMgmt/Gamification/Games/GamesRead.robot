*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesListPage.py

*** Test Cases ***
1 - Able to filter created record in game setup
    [Documentation]    Able to filter created record in game setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28566
    When user navigates to menu Performance Management | Gamification | Games
    And user can create game setup using random data
    Then record created successfully with message 'Record added'
    And click cancel game setup button
    And user filters game setup using created data

2 - Able to inline search created record in game setup
    [Documentation]    Able to filter created record in game setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28566
    When user navigates to menu Performance Management | Gamification | Games
    And user can create game setup using random data
    Then record created successfully with message 'Record added'
    And click cancel game setup button
    Then user inline search created game setup

3 - Validate specific fields are disabled in edit view
    [Documentation]    Validate fields shown below are disabled in edit view
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28836
    [Template]    Validate specific fields are disabled in edit view
    Game Code, Frequency, Total Reward Points, Level, From (Points)

4 - From (Point) field is default to zero and disabled in ranking section
    [Documentation]    Validate UI display on ranking section
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28614
    When user navigates to menu Performance Management | Gamification | Games
    Then user verified from point is default to zero and disabled

5 - Validate columns shown in listing page and details page
    [Documentation]    Validate columns shown in listing page
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28544
    [Template]    Validate columns in listing screen for game setup
    Game Code, Game Description, Start Date, End Date, Status

6 - Validate UI display on game details
    [Documentation]    Validate UI display on game details page
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28544    NRSZUANQ-28581    NRSZUANQ-28614
    [Template]    Validate UI display on game details page
    Game Code, Game Description, Start Date, End Date, Frequency, Status, KPI, Available Reward, Total Reward Points:, Level, Rank Name, From (Point), To (Point)

7 - Verify default value and drop down values for frequency
    [Documentation]    Default value is Once and has other values: Monthly, Quarterly, Half Yearly and Yearly
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28577
    When user navigates to menu Performance Management | Gamification | Games
    Then user verified drop down values and default value once is selected for frequency

8 - Verify default value and option values for status
    [Documentation]    Default value is Active and has other option: Inactive
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28579
    When user navigates to menu Performance Management | Gamification | Games
    Then user verified option values and default value active is selected for status

9 - Verify level is default to one and read only in ranking section
    [Documentation]    Validate UI display on ranking section
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28614
    When user navigates to menu Performance Management | Gamification | Games
    Then user verified level is default to one