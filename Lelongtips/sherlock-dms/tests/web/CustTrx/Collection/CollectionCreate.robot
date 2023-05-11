*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/CustTrx/Collection/CollectionListPage.py
Library         ${EXECDIR}${/}resources/web/CustTrx/Collection/CollectionAddPage.py


*** Test Cases ***
1 - Able to create Collection with random data
    [Documentation]    To create Collection with random data
    [Tags]     distadm    9.2
    Given user navigates to menu Customer Transaction | Collection
    When user applies collection header
    And user creates collection with random data
    Then collection created successfully with message 'Create Collection(s) Process Initiated'

2 - Able to create Collection with fixed data
    [Documentation]    To create Collection with fixed data
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    route=route choon
    ...    customer=Customer B02
    ...    amount=${3}
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user applies collection header
    And user creates collection with fixed data
    Then collection created successfully with message 'Create Collection(s) Process Initiated'

3 - Able to upload valid file for e-wallet receipt
    [Documentation]    Able to upload valid file for e-wallet receipt
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    route=route choon
    ...    customer=Customer B02
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user applies collection header
    And user uploads valid file for e-wallet receipt
    Then collection created successfully with message 'File added'

4 - Unable to upload invalid file type for e-wallet receipt
    [Documentation]    Unable to upload invalid file type for e-wallet receipt
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    route=route choon
    ...    customer=Customer B02
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user applies collection header
    And user uploads invalid file for e-wallet receipt
    Then validate pop up message shows 'File extension does not match predefined format'
    And close payment pop up

5 - Unable to upload file with invalid size for e-wallet receipt
    [Documentation]    Unable to upload file with invalid size for e-wallet receipt
    [Tags]     distadm    9.2
    ${ColDetails}=    create dictionary
    ...    route=route choon
    ...    customer=Customer B02
    set test variable     &{ColDetails}
    Given user navigates to menu Customer Transaction | Collection
    When user applies collection header
    And user uploads invalid file with invalid size for e-wallet receipt
    Then validate pop up message shows 'File size exceeds predefined maximum size'
    And close payment pop up