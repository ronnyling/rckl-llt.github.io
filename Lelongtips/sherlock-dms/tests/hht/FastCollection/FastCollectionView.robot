*** Settings ***
Resource        ${EXECDIR}/tests/hht/common.robot
Resource        ${EXECDIR}${/}tests/hht/common.robot
Library         ${EXECDIR}${/}resources/hht/FastCollection/FastCollectionView.py

*** Test Cases ***
1 - Able to navigate to fast collection page
    [Documentation]    To test that user is able to view fast collection page
    [Tags]    deliveryperson     9.2    NRSZUANQ-45482
    When user navigates to fast collection page for customer no:2
    Then validate element in fast collection page

2 - Able to get correct collectable amount
    [Documentation]    To test that user is able to view correct collectable amount
    [Tags]    deliveryperson     9.2    NRSZUANQ-45483
    When user navigates to fast collection page for customer no:2
    Then validate collectable amount
