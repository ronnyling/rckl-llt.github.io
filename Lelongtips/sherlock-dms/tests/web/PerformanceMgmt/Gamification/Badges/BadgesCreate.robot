*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesAddPage.py
Library         ${EXECDIR}${/}resources/web/PerformanceMgmt/Gamification/Badges/BadgesListPage.py

#not applicable to distadm, but applicable for hqadm, sysimp
*** Test Cases ***
1 - Validate user scope for badge setup
    [Documentation]    To ensure only sysimp and hqadm has the full access, distadm has view access only
    [Tags]    hqadm    sysimp    distadm    9.1    NRSZUANQ-27109
    [Template]    Validate user scope for badge setup
    ${user_role}

2 - Able to create badge setup using random data
    [Documentation]    Able to create badge setup using random data
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27112
    When user navigates to menu Performance Management | Gamification | Badges
    Then user can create badge setup using random data
    And badge setup created successfully with message 'Record created successfully'
    When user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'

3 - Able to create badge setup using fixed data
    [Documentation]    Able to create badge setup using fixed data
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27112
    When user navigates to menu Performance Management | Gamification | Badges
    ${BadgeSetupDetails}=    create dictionary
    ...    Badge_Code=TestingBadgeCode
    ...    Badge_Description=TestingBadgeDescription
    set test variable    &{BadgeSetupDetails}
    Then user verified badge setup is created
    When user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'

4 - Validate columns in listing screen for badge setup
    [Documentation]    Validate columns in listing screen for badge setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27112
    [Template]    Validate columns in listing screen for badge setup
    badge_code
    badge_description
    badge_image

5 - Validate mandatory field in badge setup
    [Documentation]    Validate mandatory field in badge setup
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27114
    [Template]    Validate mandatory field in badge setup
    Badge Code
    Badge Description
    Badge Image

6 - Unable to create duplicate badge code
    [Documentation]    Unable to create duplicate badge code
    [Tags]    hqadm    sysimp    9.1    NRSZUANQ-27122
    When user navigates to menu Performance Management | Gamification | Badges
    ${BadgeSetupDetails}=    create dictionary
    ...    Badge_Code=TestingCode
    ...    Badge_Description=TestingDesc
    set test variable    &{BadgeSetupDetails}
    Then user can create badge setup using fixed data
    And badge setup created successfully with message 'Record created successfully'
    When user can create badge setup using fixed data
    Then expect pop up message: Duplicate Badge Code
    And user navigates back to listing page
    When user selects badge setup to delete
    Then badge setup deleted successfully with message 'Record deleted'


