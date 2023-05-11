*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardSetup/ScoreCardSetupPost.py

*** Test Cases ***
1 - Able to create vision store with KPI Description
    [Documentation]    Able to create vision store with KPI Description
    ...    This is not applicable to distadm
    [Tags]    hqadm    hquser561    9.1.1    NRSZUANQ-39192    NRSZUANQ-39201
    Given user retrieves token access as hqadm
    When user creates vs score card using random data
    Then expected return status code 201
    When user creates kpi assignment using random data
    Then expected return status code 201

2 - Able to create vision store with Achievement By when measurement method is Price Audit or Promotion Compliance
    [Documentation]    Able to create vision store with Achievement By with option: “Percentage” and "Hit Count”
    ...    This is not applicable to distadm
    [Tags]    hqadm89    hquser    9.1.1    NRSZUANQ-39195    NRSZUANQ-39201     bugticket:NRSZUANQ-52344
    Given user retrieves token access as hqadm
    When user creates vs score card using random data
    Then expected return status code 201
    ${VSScoreCardDetails}=    create dictionary
    ...    MEASUREMENT=MA
    ...    MERC_AUDIT_TYPE=POA
    ...    ACHIEVEMENT_BY=H
    set test variable    ${VSScoreCardDetails}
    When user creates kpi assignment using fixed data
    Then expected return status code 500
    ${VSScoreCardDetails}=    create dictionary
    ...    MEASUREMENT=MA
    ...    MERC_AUDIT_TYPE=PO
    ...    ACHIEVEMENT_BY=H
    set test variable    ${VSScoreCardDetails}
    When user creates kpi assignment using fixed data
    Then expected return status code 201
    ${VSScoreCardDetails}=    create dictionary
    ...    MEASUREMENT=MA
    ...    MERC_AUDIT_TYPE=PI
    ...    ACHIEVEMENT_BY=H
    set test variable    ${VSScoreCardDetails}
    When user creates kpi assignment using fixed data
    Then expected return status code 201
    ${VSScoreCardDetails}=    create dictionary
    ...    MEASUREMENT=MA
    ...    MERC_AUDIT_TYPE=PI
    ...    ACHIEVEMENT_BY=P
    set test variable    ${VSScoreCardDetails}
    When user creates kpi assignment using fixed data
    Then expected return status code 201

3 - Verify Achievement By field is mandatory when measurement method is Price Audit or Promotion Compliance
    [Documentation]    Verify field is mandatory when measurement method is Price Audit or Promotion Compliance
    ...    This is not applicable to distadm
    [Tags]    hqadm     hquser    9.1.1    NRSZUANQ-39197
    Given user retrieves token access as hqadm
    When user creates vs score card using random data
    Then expected return status code 201
    ${VSScoreCardDetails}=    create dictionary
    ...    MEASUREMENT=MA
    ...    MERC_AUDIT_TYPE=PO
    ...    ACHIEVEMENT_BY=${empty}
    set test variable    ${VSScoreCardDetails}
    When user creates kpi assignment using fixed data
    Then expected return status code 400
    ${VSScoreCardDetails}=    create dictionary
    ...    MEASUREMENT=MA
    ...    MERC_AUDIT_TYPE=PI
    ...    ACHIEVEMENT_BY=${empty}
    set test variable    ${VSScoreCardDetails}
    When user creates kpi assignment using fixed data
    Then expected return status code 400