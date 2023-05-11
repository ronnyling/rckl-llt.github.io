*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookAssignmentPage.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookPost.py
Library         ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookGeneralInfo/DigitalPlaybookDelete.py

*** Test Cases ***
1 - Able to add assignment to random Playbook
    [Documentation]    Able to add assignment to random playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758    NRSZUANQ-44759    NRSZUANQ-44764
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

2 - Able to add assignment to route Playbook
    [Documentation]    Able to add assignment to route playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44759    NRSZUANQ-44764
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

3 - Able to add assignment to customer Playbook
    [Documentation]    Able to add assignment to customer playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

4 - Able to update assignment on random Playbook
    [Documentation]    Able to update assignment on random playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758    NRSZUANQ-44759    NRSZUANQ-44764
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user deletes assignment from playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

5 - Able to exclude distributor from Playbook
    [Documentation]    Able to add exclusion to route playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44759    NRSZUANQ-44764
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user exclude Distributor:DistEgg from ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

6 - Able to exclude route from Playbook
    [Documentation]    Able to add exclusion to route playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44759    NRSZUANQ-44764
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user exclude Route:DistBran,RouteBran from ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

7 - Able to add exclusion to customer Playbook
    [Documentation]    Able to add exclusion to customer playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user exclude Customer:DistBran,CustomerBran from ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

8 - Able to remove distributor exclusion from Playbook
    [Documentation]    Able to remove exclusion from customer playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user exclude Distributor:DistBran from ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user remove Distributor exclusion from playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

9 - Able to remove customer exclusion from Playbook
    [Documentation]    Able to remove exclusion from customer playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user exclude Customer:DistBran,CustomerBran from ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user remove Customer exclusion from playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

10 - Able to remove exclusion from route Playbook
    [Documentation]    Able to remove exclusion from route playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44759    NRSZUANQ-44764
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    set test variable   &{playbook_general_details}
    Given user retrieves token access as ${user_role}
    When user creates playbook with fixed data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user exclude Route:DistBran,RouteBran from ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user remove Route exclusion from playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

11 - Able to delete assignment from Playbook
    [Documentation]    Able to delete assignment from both customer and route playbook
    [Tags]   hqadm    9.2    NRSZUANQ-44757    NRSZUANQ-44758    NRSZUANQ-44759    NRSZUANQ-44764
    Given user retrieves token access as ${user_role}
    When user creates playbook with random data
    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    And user add Level:Country assignment to ${playbk_ass_to} playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user selects playbook to edit
    And user deletes assignment from playbook
    Then playbook updated successfully with message 'Record added successfully'
    When user deletes playbook with created data
    Then expected return status code 200

12 - Able to validate assignment refreshed on route Playbook
    [Documentation]    Able to validate assignment refreshed on route Playbook
    [Tags]   hqadm    9.2    NRSZUANQ-46838
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=R
    set test variable   &{playbook_general_details}
#    Given user retrieves token access as ${user_role}
#    When user creates playbook with fixed data
#    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    Then user validates route playbook assignment
#    When user deletes playbook with created data
#    Then expected return status code 200

13 - Able to validate assignment refreshed on customer Playbook
    [Documentation]    Able to validate assignment refreshed on route Playbook
    [Tags]   hqadm    9.2    NRSZUANQ-46838
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    set test variable   &{playbook_general_details}
#    Given user retrieves token access as ${user_role}
#    When user creates playbook with fixed data
#    Then expected return status code 201
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    Then user validates customer playbook assignment
#    When user deletes playbook with created data
#    Then expected return status code 200

14 - Able to validate assignment refreshed on customer Playbook
    [Documentation]    Able to validate assignment refreshed on route Playbook
    [Tags]   hqadm    9.2    NRSZUANQ-46838
    ${playbook_general_details}=    create dictionary
    ...     PLAYBK_ASSIGN_TO=C
    set test variable   &{playbook_general_details}
    Given user navigates to menu Master Data Management | Digital Playbook
    When user selects playbook to edit
    Then user validates customer playbook assignment