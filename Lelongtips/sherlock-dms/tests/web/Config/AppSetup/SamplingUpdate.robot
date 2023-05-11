*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/SamplingEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py


*** Test Cases ***
1 - Able to update sampling using random data
    [Documentation]    Able to update sampling using random data
    [Tags]    hqadm    9.3    NRSZUANQ-52779
    When user navigates to menu Configuration | Application Setup
    And user navigates to Promotion tab
    Then user updates sampling using random data
    And sampling updated successfully with message 'Record updated successfully'

2 - Able to update sampling using fixed data
    [Documentation]    Able to update sampling using fixed data
    [Tags]    hqadm    9.3    NRSZUANQ-52779
    When user navigates to menu Configuration | Application Setup
    And user navigates to Promotion tab
    ${sampling_details}=    create dictionary
    ...    Combine_Sample_&_Selling_Products_in_Transaction=${True}
    ...    Allow_Sampling_for_New_/_Unapproved_Customers=${True}
    set test variable    &{sampling_details}
    Then user updates sampling using fixed data
    And sampling updated successfully with message 'Record updated successfully'
