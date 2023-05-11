*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionAddPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/PromotionMgmt/Promotion/PromotionListPage.py


*** Test Cases ***
1 - Able to copy promotion from distributor successfully
    [Documentation]    Able to copy distributor promotion using distributor access
    [Tags]    distadm    9.2    NRSZUANQ-52143
    ${CopyDetails}=    create dictionary
    ...    promo_code=DIST_PROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user enters the copy promotion details
    Then promotion copied successfully with message 'Promotion Copied successfully'

2 - Able to copy promotion from hqadm successfully
    [Documentation]    Able to copy hq promotion using hqadm access
    [Tags]    hqadm    9.2     NRSZUANQ-52144
    ${CopyDetails}=    create dictionary
    ...    promo_code=HQPROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user enters the copy promotion details
    Then promotion copied successfully with message 'Promotion Copied successfully'

3 - Unable to copy hq created promotion using distributor access
    [Documentation]    Unable to copy hq promo using distributor access
    [Tags]    distadm    9.2    NRSZUANQ-52145
    ${CopyDetails}=    create dictionary
    ...    promo_code=HQPROMO2
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    Then user validates copy button is disabled

4 - Validate mandatory fields in copy promotion
    [Documentation]    Validate the mandatory fields in copy promotion pop up
    [Tags]    hqadm    9.2     NRSZUANQ-52147
    ${CopyDetails}=    create dictionary
    ...    promo_code=HQPROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user clicks on Save button
    Then user validates copy promotion mandatory fields

5 - Validate copy button is disabled when no promotion is selected
    [Documentation]    Able to copy button is disabled without promotion selection
    [Tags]    hqadm    9.2    NRSZUANQ-52176
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects no promotion to copy
    Then user validates copy button is disabled

6 - Validate copy button is disabled when multiple promotion is selected
    [Documentation]    Able to copy button is disabled with multiple promotion selection
    [Tags]    hqadm    9.2    NRSZUANQ-52175
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects multiple promotion to copy
    Then user validates copy button is disabled

7 - Able to cancel copy promotion without any selection
    [Documentation]    Able to cancel copy promotion without any selection
    [Tags]    hqadm    9.2    NRSZUANQ-52154
    ${CopyDetails}=    create dictionary
    ...    promo_code=HQPROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user clicks on Cancel button
    Then user is able to view listing page

8 - Unable to copy Space Buy promotion without Entitlement Date
    [Documentation]    Unable to copy space buy without entitlement date
    [Tags]    hqadm    9.2    NRSZUANQ-52152
    ${CopyDetails}=    create dictionary
    ...    promo_code=SPACE100
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user enters the copy promotion details
    Then validate unable to save space buy promotion

9 - Unable to copy claimable promotion without Claim Submission Date
    [Documentation]    Unable to copy space buy without entitlement date
    [Tags]    hqadm    9.2    NRSZUANQ-52153
    ${CopyDetails}=    create dictionary
    ...    promo_code=CLAIMHQ
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user enters the copy promotion details
    Then validate unable to save space buy promotion

10 - Unable to copy promotion with invalid code and description
    [Documentation]    Unable to copy promotion using invalid code and description length and pattern
    [Tags]    distadm    9.2    NRSZUANQ-52157
    ${CopyDetails}=    create dictionary
    ...    promo_code=DIST_PROMO
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    ${PromoDetails}=    create dictionary
    ...    code=PROMO
    ...    desc=PR
    And user enters the copy promotion details
    Then validate message on invalid length
    ${PromoDetails}=    create dictionary
    ...    code=!@!@!@
    ...    desc=PROMO
    And user enters the copy promotion details
    Then validate message on invalid pattern

11 - Able to copy promotion for promotion with POSM Assignment
    [Documentation]    Able to copy promotion for POSM Assignment scheme
    [Tags]    hqadm    9.2    NRSZUANQ-52162
    ${CopyDetails}=    create dictionary
    ...    promo_code=POSMOR
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user enters the copy promotion details
    Then promotion copied successfully with message 'Promotion Copied successfully'

12 - Able to copy promotion for promotion with Max Count
    [Documentation]    Able to copy promotion for Max Count scheme
    [Tags]    hqadm    9.2    NRSZUANQ-52163
    ${CopyDetails}=    create dictionary
    ...    promo_code=MAXPRM
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user enters the copy promotion details
    Then promotion copied successfully with message 'Promotion Copied successfully'

13 - Able to copy promotion for promotion with Combi
    [Documentation]    Able to copy promotion for Combi scheme
    [Tags]    hqadm    9.2    NRSZUANQ-52168
    ${CopyDetails}=    create dictionary
    ...    promo_code=PROMOCOMBI
    Given user navigates to menu Master Data Management | Promotion Management | Promotion
    When user selects single promotion to copy
    And user clicks on Copy button
    And user enters the copy promotion details
    Then promotion copied successfully with message 'Promotion Copied successfully'


