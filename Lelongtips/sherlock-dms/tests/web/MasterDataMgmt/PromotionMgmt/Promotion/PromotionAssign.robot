*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAsgnPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Promo/PromoDelete.py

Test Setup      run keywords
...    user open browser and logins using user role ${user_role}
...    AND    user creates fixed promotion as prerequisite
...    AND    user retrieves token access as ${user_role}
...    AND    user creates promotion with fixed data
...    AND    expected return status code 201
Test Teardown      run keywords
...    user retrieves token access as ${user_role}
...    AND    user updates promotion start date as tomorrow
...    AND    user deletes promotion
...    AND    expected return status code 200
...    AND    user logouts and closes browser

*** Test Cases ***
1 - Able to add POSM assignment and save successfully
    [Documentation]    Able to add posm assignment successfully
    [Tags]    hqadm    9.1.1    NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=${50}
    When user selects promotion to edit
    And user go to Assignment tab and assign fixed details
    Then assignment updated successfully with message 'Record updated'

2 - Able to expand and collapse POSM assignment section and cancel assignment pop up
    [Documentation]    Able to expand/collapse posm assignment and close pop up
    [Tags]    hqadm    9.1.1    NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user goes to assignment tab
    Then validate tab can be expand collapse successfully
    When user adds posm assignment
    Then user cancels posm assignment

3 - Able to search POSM assignment using inline search
    [Documentation]    Able to search posm assignment using inline search
    [Tags]    hqadm    9.1.1   NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    posm=POSMPRD1
    When user selects promotion to edit
    And user goes to assignment tab
    And user searches for fixed posm
    Then able to search posm successfully

4 - Unable to save without minimum quantity when quantity default to 0
    [Documentation]    Unable to save posm assignment with empty quantity
    [Tags]    hqadm    9.1.1    NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user goes to assignment tab
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=${0}
    And user adds posm assignment using fixed data
    Then assignment unable to update successfully with message 'Invalid quantity'

5 - Unable to add invalid (letters/negative/symbol) minimum quantity
    [Documentation]    Unable to type in invalid quantity for posm assignment
    [Tags]    hqadm    9.1.1    NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user goes to assignment tab
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=abc
    And user adds posm assignment using invalid data
    Then assignment unable to update successfully with message 'Invalid quantity'

6 - Validate dropdown selection disabled and fixed to assigned Attribute/POSM when there is assigned data
    [Documentation]    validate dropdown selection disabled on 2nd assign
    [Tags]    hqadm    9.1.1   NRSZUANQ-41632
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=${50}
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user go to Assignment tab and assign fixed details
    Then assignment updated successfully with message 'Record updated'
    When user adds posm assignment
    Then attribute level being disabled

7 - Validate added record not showing in add selection anymore
    [Documentation]    validate added record will not show in add list anymore
    [Tags]    hqadm    9.1.1    NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=${50}
    When user selects promotion to edit
    And user go to Assignment tab and assign fixed details
    Then assignment updated successfully with message 'Record updated'
    When user adds posm assignment
    Then user unable to search for assigned posm

8 - Validate add/delete button being disabled once promotion been approved
    [Documentation]    validate add/delete button not showing when promotion being approved
    [Tags]    hqadm    9.1.1    NRSZUANQ-41632
    [Teardown]    user logouts and closes browser
    ${DistAssignDetails}=    create dictionary
    ...    option=State
    ...    State=LCState
    ${OthAssignDetails}=   create dictionary
    ...    attribute=POSM
    ...    minQty=${50}
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user go to Assignment tab and assign fixed details
    Then assignment updated successfully with message 'Record updated'
    When user approve current promotion
    And user goes to assignment tab
    Then buttons should be disabled

9 - Unable to edit POSM assignment section using dist access
    [Documentation]    Unable to edit POSM assignment section when using distributor access
    [Tags]    distadm    9.1.1    NRSZUANQ-41632
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects promotion to edit
    And user goes to assignment tab
    Then buttons should be disabled
