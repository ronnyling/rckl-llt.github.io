*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardSetup/ScoreCardSetupPost.py
Library           ${EXECDIR}${/}resources/restAPI/PerformanceMgmt/VisionStore/ScoreCardSetup/ScoreCardSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPost.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerGet.py
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Customer/CustomerPut.py

*** Test Cases ***
1 - Able to edit vision store field in customer module using hqadm and hquser
    [Documentation]    Verify enable scoring value is true and unable to edit field by using hqadm, hquser
    ...    This is not applicable to distadm
    [Tags]    hqadm    hquser    9.1.1    NRSZUANQ-39194
    Given user retrieves token access as hqadm
    When user creates vs score card using random data
    Then expected return status code 201
    When user creates kpi assignment using random data
    Then expected return status code 201
    ${VSScoreCardDetails}=    create dictionary
    ...    ENABLE_SCORE=${false}
    set test variable    ${VSScoreCardDetails}
    When user updates kpi assignment using fixed data
    Then expected return status code 400
    ${VSScoreCardDetails}=    create dictionary
    ...    ENABLE_SCORE=${empty}
    set test variable    ${VSScoreCardDetails}
    When user updates kpi assignment using fixed data
    Then expected return status code 400

2 - Verify enable scoring value is true and unable to edit it in vision store card module
    [Documentation]    Verify enable scoring value is true and unable to edit field by using hqadm, hquser
    ...    This is not applicable to distadm
    [Tags]    hqadm    hquser    9.1.1    NRSZUANQ-39194
    Given user retrieves token access as hqadm
    When user creates vs score card using random data
    Then expected return status code 201
    When user creates kpi assignment using random data
    Then expected return status code 201
    ${VSScoreCardDetails}=    create dictionary
    ...    ENABLE_SCORE=${false}
    set test variable    ${VSScoreCardDetails}
    When user updates kpi assignment using fixed data
    Then expected return status code 400
    ${VSScoreCardDetails}=    create dictionary
    ...    ENABLE_SCORE=${empty}
    set test variable    ${VSScoreCardDetails}
    When user updates kpi assignment using fixed data
    Then expected return status code 400
