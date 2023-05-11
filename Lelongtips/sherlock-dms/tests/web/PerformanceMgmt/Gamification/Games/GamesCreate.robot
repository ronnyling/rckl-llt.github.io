*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Games/GamesListPage.py

*** Test Cases ***
1 - Validate user scope for game setup
    [Documentation]    Validate hqadm and sysimp has full access whereby distadm has view access
    [Tags]    hqadm    sysimp    distadm    9.1    NRSZUANQ-28547
    [Template]    Validate user scope for game setup
    hqadm
    sysimp
    distadm

2 - Validate mandatory field for game setup
    [Documentation]    Validate Game Code, Game Description, Start Date, End Date, KPI, Available Rewards are mandatory fields in game setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28569    NRSZUANQ-28588
    [Template]    Validate mandatory field in game setup
    Game Code
    Game Description
    Start Date
    End Date
    KPI
    Available Rewards

3 - Validate start date and end date for game setup
    [Documentation]    Start date must be future date, and end date must be equal to or greater than start date
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28573
    When user navigates to menu Performance Management | Gamification | Games
    ${GameSetupDetails}=    create dictionary
    ...    GameCode=testStartEndDate
    ...    GameDesc=testStartEndDate
    ...    StartDate=next day
    ...    EndDate=next day
    set test variable    ${GameSetupDetails}
    And user can create game setup using fixed data
    Then record created successfully with message 'Record added'
    When user deletes created game setup
    Then record created successfully with message 'Record deleted'

4 - Able to create game setup using random data
    [Documentation]    Able to create game setup using random data
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28545
    When user navigates to menu Performance Management | Gamification | Games
    And user can create game setup using random data
    Then record created successfully with message 'Record added'

5 - Unable to create game setup with used game code
    [Documentation]    Game code is unique
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28572
    When user navigates to menu Performance Management | Gamification | Games
    ${GameSetupDetails}=    create dictionary
    ...    GameCode=testDuplicationCase
    ...    GameDesc=testDuplicationCase
    ...    StartDate=next day
    ...    EndDate=next day
    set test variable    ${GameSetupDetails}
    And user can create game setup using fixed data
    Then record created successfully with message 'Record added'
    And click cancel game setup button
    When user can create game setup using fixed data
    Then message prompted successfully 'Duplicate Game Code'
    When user deletes created game setup
    Then record created successfully with message 'Record deleted'

6 - Able to select created reward in reward setup in reward assignment section
    [Documentation]    Able to select created reward in reward setup in reward assignment section
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28583
    Given user creates reward setup
    When user navigates to menu Performance Management | Gamification | Games
    Then user able to assign created reward in reward setup successfully

7 - Verify reward points shown in reward assignment section
    [Documentation]    To ensure reward points shown same as created in reward setup
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28589
    When user navigates to menu Performance Management | Gamification | Games
    Then user verified reward points shown

8 - Verify total reward points shown in ranking section
    [Documentation]    To ensure total reward points shown in ranking section are correct
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28609
    When user navigates to menu Performance Management | Gamification | Games
    Then user verified total reward points shown

9 - Able to add record in ranking section
    [Documentation]    Read only from (point) will automatically update after record added in ranking section
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28609
    When user navigates to menu Performance Management | Gamification | Games
    And user can create game setup using random data
    Then record created successfully with message 'Record added'
    And user able to add record in ranking section successfully
    When user deletes created game setup
    Then record created successfully with message 'Record deleted'

10 - Unable to add invalid points in ranking section
    [Documentation]    To (Point) cannot be greater than Total Reward Points will prompt when invalid points entered
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-28609
    When user navigates to menu Performance Management | Gamification | Games
    And user can create game setup using random data
    Then record created successfully with message 'Record added'
    And verified user unable to add invalid points in ranking section
    When user deletes created game setup
    Then record created successfully with message 'Record deleted'

11 - Able to edit added points in ranking section
    [Documentation]    Update button will reflect once clicked on the hyperlink for Rank Name
    ...    This is not applicable to distadm
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-286091    TODO
    When user navigates to menu Performance Management | Gamification | Games
    And user can create game setup using random data
    Then record created successfully with message 'Record added'
    When user edit added points in ranking section
    Then ranking record updated successfully
    And user deletes created game setup
    Then record created successfully with message 'Record deleted'