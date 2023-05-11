*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/DeliveryEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***

1 - Able to update delivery tab using random data
    [Documentation]    Able to update delivery using random data
    [Tags]    hqadm    9.2
    When user navigates to menu Configuration | Application Setup
    And user navigates to Delivery tab
    Then user updates delivery using random data
    And delivery updated successfully with message 'Record updated successfully'

2 - Able to update delivery tab using fixed data
    [Documentation]    Able to update delivery using random data
    [Tags]    hqadm    9.2      asdwqeasdas
    ${DeliveryDetails} =    create dictionary
    ...   PartialDelivery=true
    ...   PartialCollection=false
    When user navigates to menu Configuration | Application Setup
    And user navigates to Delivery tab
    Then user updates delivery using fixed data
    And delivery updated successfully with message 'Record updated successfully'