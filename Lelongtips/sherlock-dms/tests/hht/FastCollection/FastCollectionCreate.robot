*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/FastCollection/FastCollectionView.py
Library         ${EXECDIR}${/}resources/hht/FastCollection/FastCollectionCreate.py

*** Test Cases ***
1 - Able to create fast collection
    [Documentation]    To test that user is able to create fast collection
    [Tags]    deliveryperson     9.2    NRSZUANQ-45483
    Given user navigates to fast collection page for customer no:1
    When user creates fast collection
    Then fast collection saved

2 - Able to update fast collection
    [Documentation]    To test that user is able to update fast collection
    [Tags]    deliveryperson     9.2    NRSZUANQ-45483
    Given user navigates to fast collection page for customer no:1
    When user updates fast collection
    Then fast collection saved

3 - Able to update fast collection completion status
    [Documentation]    To test that user is able to update fast collection completion status
    [Tags]    deliveryperson     9.2    NRSZUANQ-45483
    Given user navigates to fast collection page for customer no:1
    When user updates fast collection
    Then validates fast collection completion status

4 - Able to create fast collection with FAST_COLLECT
    [Documentation]    To test that user is able to create fast collection with new attribute 'FAST_COLLECT'
    [Tags]    deliveryperson     9.2    NRSZUANQ-45483
    Given user navigates to fast collection page for customer no:1
    When user creates fast collection
    Then fast collection saved
    When pull emulator db into local
    Then validates fast collect