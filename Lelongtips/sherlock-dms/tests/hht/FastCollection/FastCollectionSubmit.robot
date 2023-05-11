*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/FastCollection/FastCollectionView.py
Library         ${EXECDIR}${/}resources/hht/FastCollection/FastCollectionCreate.py
Library         ${EXECDIR}${/}resources/hht/FastCollection/FastCollectionSubmit.py

*** Test Cases ***
1 - Able to submit fast collection transaction
    [Documentation]    To test that user is able to submit fast collection transaction
    [Tags]    deliveryperson     9.2    NRSZUANQ-45486
    Given user navigates to fast collection page for customer no:1
    When user creates fast collection
    And user ends visit
    Then user releases picklist from device

2 - Able to submit fast collection transaction with attribute FAST_COLLECT
    [Documentation]    To test that user is able to submit fast collection transaction attribute FAST_COLLECT
    [Tags]    deliveryperson     9.2    NRSZUANQ-45486
    Given user navigates to fast collection page for customer no:1
    When user creates fast collection
    And fast collection saved
    And pull emulator db into local
    And validates fast collect
    And user ends visit
    Then user releases picklist from device
    And validates fast collect submitted
