*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/Collection/CollectionListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/Collection/CollectionAddPage.py


*** Test Cases ***
1 - Able to process Collection
    [Documentation]    To process Collection
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000867
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to check
    And user process selected collection
    Then collection created successfully with message 'Process Collection(s) Process Initiated'

2 - Able to reject Collection
    [Documentation]    To reject Collection
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    collectionNo=CO0000000853
    ...    rejectReason=Invalid Collection
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user selects collection to check
    And user reject selected collection
    Then collection created successfully with message 'Success: Reject Reason Saved successfully.'
