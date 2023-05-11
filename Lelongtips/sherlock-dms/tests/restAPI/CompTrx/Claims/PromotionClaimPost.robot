*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/Claim/PromotionClaimPost.py
Library           ${EXECDIR}${/}resources/restAPI/SysConfig/Maintenance/WorkFlow/WorkFlowPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/ClaimMgmtGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/ClaimMgmtPut.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupGet.py
Library           ${EXECDIR}${/}resources/restAPI/Config/AppSetup/AppSetupPut.py
Library           ${EXECDIR}${/}resources/restAPI/CompTrx/Claim/ClaimPromoDocFilter.py

Test Setup        user updates claim_approval workflow to Auto:off, Hierarchy:General Non Prime Hierarchy , Level:Dove soap

*** Test Cases ***
1 - Able to create Promotion claims in Open status
    [Documentation]    To create Promotion claims in Open status
    [Tags]      distadm    9.1.1     NRSZUANQ-41946
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=D
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    When user cancelled created claims
    Then expected return status code 200

2 - Able to create Promotion claims in Confirmed status
    [Documentation]    To create Promotion claims in Confirmed status and reject it.
    [Tags]     distadm    9.1.1     NRSZUANQ-41947
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user reject created claims
    Then expected return status code 200

3- Able to dispute approved claim
    [Documentation]    To dispute approved promotion claims.
    [Tags]     distadm    9.1.1      NRSZUANQ-41700
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approve created claims
    Then expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_ENBL_CLAIM_ACK=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as distadm
    When user dispute created claim
    Then expected return status code 200

4- Unable to dispute approved claim when Acknowleged claim = True
    [Documentation]    To dispute approved promotion claims when acknowledged claim set to true.
    [Tags]     distadm    9.1.1       NRSZUANQ-41702
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approve created claims
    Then expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_ENBL_CLAIM_ACK=${True}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as distadm
    When user dispute created claim
    Then expected return status code 400

5- Able to dispute acknowledge claim
    [Documentation]    To dispute acknowledge promotion claims.
    [Tags]     distadm    9.1.1      NRSZUANQ-41694
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approve created claims
    Then expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_ENBL_CLAIM_ACK=${True}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    When user acknowledge approved claim
    And expected return status code 200
    Given user retrieves token access as distadm
    When user dispute created claim
    Then expected return status code 200

6- Able to dispute acknowledge claim when Acknowleged claim = False
    [Documentation]    To dispute acknowledge promotion claims when acknowledged claim set to false.
    [Tags]     distadm    9.1.1       NRSZUANQ-41701
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approve created claims
    Then expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_ENBL_CLAIM_ACK=${True}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    When user acknowledge approved claim
    Then expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_ENBL_CLAIM_ACK=${False}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as distadm
    When user dispute created claim
    Then expected return status code 200

7 - Unable to dispute Promotion claims in Open status
    [Documentation]    To create Promotion claims in Confirmed status and reject it.
    [Tags]     distadm    9.1.1       NRSZUANQ-41703
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=D
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    When user dispute created claim
    Then expected return status code 400
    When user cancelled created claims
    Then expected return status code 200

8 - Unable to create claim in confirmed status if Block Claim = Yes
    [Documentation]    To validate unable to create claim in confirmed status if any approved claim already exits.
    [Tags]     distadm    9.1.1       NRSZUANQ-41833
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    ...    CM_ENBL_CLAIM_ACK=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    Given user retrieves token access as hqadm
    When user approve created claims
    Then expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${True}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as distadm
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 400
    When user dispute created claim
    Then expected return status code 200

9 - Able to create claim in confirmed status if Block Claim = NO
    [Documentation]    To validate unable to create claim in confirmed status if any acknowledge claim already exits.
    [Tags]     distadm    9.1.1       NRSZUANQ-41850
    Given user retrieves token access as hqadm
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    ...    CM_ENBL_CLAIM_ACK=${False}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    When user retrieves token access as ${user_role}
    Then user gets the promotion details
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 201
    When user retrieves token access as hqadm
    Then user approve created claims
    When user retrieves token access as distadm
    And user dispute created claim
    Then expected return status code 200

10 - Unable to create claim in confirmed status if Block Claim = Yes
    [Documentation]    To validate unable to create claim in confirmed status if any acknowledge claim already exits.
    [Tags]     distadm    9.1.1       NRSZUANQ-41841
    Given user retrieves token access as hqadm
     ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    ...    CM_ENBL_CLAIM_ACK=${False}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=U
    set test variable   &{ClaimDetails}
    Given user retrieves token access as ${user_role}
    When user gets the promotion details
    Then expected return status code 200
    Then user creates promotion claims
    And expected return status code 201
    When user retrieves token access as hqadm
    Then user approve created claims
    And expected return status code 200
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${True}
    ...    CM_ENBL_CLAIM_ACK=${True}
    set test variable   &{AppSetupDetails}
    When user retrieves details of application_setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    When user acknowledge approved claim
    Then expected return status code 200
    Given user retrieves token access as distadm
    When user gets the promotion details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...  ClaimStatus=U
    set test variable   &{ClaimDetails}
    When user creates promotion claims
    Then expected return status code 400
    When user dispute created claim
    Then expected return status code 200

11 - Able to create Space Buy Promotion claims
    [Documentation]    To create Space Buy Promotion claims
    [Tags]    distadm    9.2
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    When user gets the spacebuy details
    Then expected return status code 200
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=D
    set test variable   &{ClaimDetails}
    When user creates spacebuy claims
    Then expected return status code 201
    When user cancelled created claims
    Then expected return status code 200

12 - Able to create Non-Customer-Related Promotion claims
    [Documentation]    To create Non-Customer-Related Promotion claims
    [Tags]    distadm
    ${AppSetupDetails}=    create dictionary
    ...    CM_RESTRICT_CLAIM_CFM_BEF_CLOSURE=${False}
    set test variable   &{AppSetupDetails}
    Given user retrieves token access as hqadm
    When user retrieves details of application setup
    Then expected return status code 200
    When user updates app setup details using fixed data
    Then expected return status code 200
    Given user retrieves token access as ${user_role}
    ${ClaimDetails}=  create dictionary
    ...    ClaimStatus=D
    ...    Amount=1
    ...    Claim_Type_Non_Cust=ClaimTypeB04
    set test variable   &{ClaimDetails}
    When user creates non-customer related claims
    Then expected return status code 201
    When user cancelled created claims
    Then expected return status code 200