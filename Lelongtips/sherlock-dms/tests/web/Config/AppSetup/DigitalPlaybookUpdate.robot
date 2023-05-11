*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/DigitalPlaybookEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
#not applicable to sysimp
1 - Able to update digital playbook using random data
    [Documentation]    Able to update digital playbook using random data
    [Tags]    hqadm    9.2   NRSZUANQ-44231    NRSZUANQ-44243
    Given user navigates to menu Configuration | Application Setup
    And user navigates to Digital Playbook tab
    When user updates digital playbook using random data
    Then digital playbook updated successfully with message 'Record updated successfully'

#not applicable to sysimp
2 - Able to update digital playbook using fixed data
    [Documentation]    Able to update digital playbook using fixed data
    [Tags]    hqadm    9.2     NRSZUANQ-44234
    ${PlaybookDetails}=    create dictionary
    ...    Product_Hierarchy_Level=Category
    ...    Max_Playbook_Content_Size=1 MB
    Given user navigates to menu Configuration | Application Setup
    And user navigates to Digital Playbook tab
    When user updates digital playbook using random data
    Then digital playbook updated successfully with message 'Record updated successfully'

3 - Able to remove Product Hierarchy Level for Playbook and save successfully using HQ access
    [Documentation]    Able to remove product hierarchy from digital playbook
    [Tags]    hqadm    9.2   NRSZUANQ-44233    NRSZUANQ-44236
    Given user navigates to menu Configuration | Application Setup
    And user navigates to Digital Playbook tab
    When user updates digital playbook using empty data
    Then digital playbook updated successfully with message 'Record updated successfully'

4 - Validate dropdown selection is retrieved from Product Hierarchy setup
    [Documentation]    Validate product hierarchy dropdown for product hierarchy retrieving correctly
    [Tags]    hqadm    9.2   NRSZUANQ-44239
    Given user navigates to menu Configuration | Application Setup
    And user navigates to Digital Playbook tab
    When user validates dropdown selection for product hierarchy
    Then dropdown of product hierarchy displaying correctly

5 - Validate Digital Playbook fields are disabled using sys imp access
    [Documentation]    Unable to edit field for digital playbook using system implementer
    [Tags]    sysimp    9.2   NRSZUANQ-44240    NRSZUANQ-44242
    Given user navigates to menu Configuration | Application Setup
    When user navigates to Digital Playbook tab
    Then digital playbook fields are disabled
