*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Resource        ${EXECDIR}${/}tests/restAPI/common.robot
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypePost.py
Library         ${EXECDIR}${/}resources/restAPI/Config/ReferenceData/PlaybookType/PlaybookTypeDelete.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookListPage.py
Library         ${EXECDIR}${/}resources/web/MasterDataMgmt/DigitalPlaybook/DigitalPlaybookAddPage.py
Library         ${EXECDIR}${/}resources/restAPI/SysConfig/TenantMaintainance/FeatureSetup/FeatureSetupPut.py


*** Test Cases ***

1 - Able to Create Digital Playbook with given data
    [Documentation]    Able to create digital plauybook
    [Tags]    hqadm
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    Given user navigates to menu Master Data Management | Digital Playbook
    When user adds digital playbook general information with random data
    And user adds digital playbook content with random data
    Then Digital Playbook created successfully with message 'Record created successfully'

2 - Able to Delete Created Digital Playbook with given data
    [Documentation]    Able to create digital plauybook
    [Tags]    hqadm
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    Given user navigates to menu Master Data Management | Digital Playbook
    When user adds digital playbook general information with random data
    And user adds digital playbook content with random data
    Then Digital Playbook created successfully with message 'Record created successfully'
    When user back to digital playbook listing page
    And user selects digital playbook to delete
    Then Digital Playbook created successfully with message '1 record(s) deleted'

3 - Validate Assign to drop down will have 2 value (Customer and Route)
    [Documentation]     Assign to drop down will have 2 selection which is (Customer and Route)
    [Tags]    hqadm
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    Given user navigates to menu Master Data Management | Digital Playbook
    When user navigates to digital playbook add page
    Then user validate Assign To drop down have following value:Customer,Route

4 - Validate Assign to drop down will have 2 value (Customer and Route)
    [Documentation]     Assign to drop down will have 2 selection which is (Customer and Route)
    [Tags]    hqadm
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    Given user navigates to menu Master Data Management | Digital Playbook
    When user navigates to digital playbook add page
    Then user validate Priority drop down have following value:High,Medium,Low

5- Able to display created playbook type in add digital playbook, playbook type drop down
    [Documentation]    validate ef data playbook type will appear in the drop down selection
    [Tags]    hqadm
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    Given user navigates to menu Master Data Management | Digital Playbook
    When user navigates to digital playbook add page
    Then user validate Playbook Type drop down have following value:choonhierrrequired

6- Able to disabled playbook code, playbook type, Assign to field if the date is passed
    [Documentation]    validate ref data playbook type will appear in the drop down selection
    [Tags]    hqadm
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    Given user navigates to menu Master Data Management | Digital Playbook
    When user adds digital playbook general information with random data
    And user adds digital playbook content with random data
    Then Digital Playbook created successfully with message 'Record created successfully'
    And validated playbook code, playbook type, Assign to is in disabled

7 - Able to upload Digital Playbook content with valid content size
    [Documentation]    Able to upload digital plauybook content with valid content size set in application setup
    [Tags]    hqadm    9.2    NRSZUANQ-46899
    Given user navigates to menu Master Data Management | Digital Playbook
    When user adds digital playbook general information with random data
    And user adds digital playbook content with fixed data
    Then Digital Playbook created successfully with message 'Record created successfully'

8 - Unable to upload Digital Playbook content with invalid content size
    [Documentation]    Unable to upload digital playbook content with invalid content size set in application setup
    [Tags]    hqadm    9.2    NRSZUANQ-46899
    Given user navigates to menu Master Data Management | Digital Playbook
    When user upload digital playbook content with invalid file size
    Then validate pop up message shows 'Invalid file size'
    And close pop up error

9 - Able to Create Digital Playbook with file length
    [Documentation]    Able to create digital playbook with file length
    [Tags]    hqadm    9.2    NRSZUANQ-46114
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    ${ContentDetails} =    create dictionary
    ...   ContentType=video
    Given user navigates to menu Master Data Management | Digital Playbook
    When user adds digital playbook general information with random data
    And user adds digital playbook content with fixed data
    Then Digital Playbook created successfully with message 'Record created successfully'

10 - Able to Create Digital Playbook with file type code
    [Documentation]    Able to create digital playbook with file type code: I-Image, V-Video, P-PowerPoint, A-PDF
    [Tags]    hqadm    9.2    NRSZUANQ-47519
    ${DigiPlyBkDetails} =    create dictionary
    ...   Thumbnail=Upload
    ${ContentDetails} =    create dictionary
    ...   ContentType=image
    Given user navigates to menu Master Data Management | Digital Playbook
    When user adds digital playbook general information with random data
    And user adds digital playbook content with fixed data
    Then Digital Playbook created successfully with message 'Record created successfully'
    And validate file type code