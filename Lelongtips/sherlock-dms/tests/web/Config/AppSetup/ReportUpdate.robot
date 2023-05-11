*** Settings ***
Resource        ${EXECDIR}${/}tests/web/common.robot
Library         ${EXECDIR}${/}resources/web/Config/AppSetup/ReportEditPage.py
Library         ${EXECDIR}${/}resources/components/Tab.py

*** Test Cases ***
1 - Able to update report using random data
    [Documentation]    Able to update report using random data
    [Tags]    hqadm100    9.1    1234
    When user navigates to menu Configuration | Application Setup
    And user navigates to Report tab
    Then user updates report using random data
    And Report updated successfully with message 'Record updated successfully'

2 - Able to update report using given data
    [Documentation]    Able to update report using given data
    [Tags]    hqadm100   9.1    123456
    ${ReportDetails}=    create dictionary
    ...    Region_Level_(Geographical)=Region
    ...    Brand_(Product_Hierarchy)=Variant
    ...    Product_Category_(Product_Hierarchy)=Category
    ...    Channel_(Customer_Hierarchy)=Channel
    ...     Outlet_Type_(Customer_Hierarchy)=Outlet Group
    ...     Segmentation_(Customer_Attribute)=Loyalty Level
    ...     Default_View=Page Width
    ...     Repeat_Header_in_Every Page=${True}
    ...     Enable_Parameter_Saving=${False}
    set test variable    &{ReportDetails}
    When user navigates to menu Configuration | Application Setup
    And user navigates to Report tab
    Then user updates report using given data
    And Report updated successfully with message 'Record updated successfully'

#Not applicable to hqadm
3 - Able to update report using given data
    [Documentation]    Able to update report using given data
    [Tags]    sysimp   9.1
    ${ReportDetails}=    create dictionary
    ...     Default_Select_All_Multi-Selection_Parameter=${True}
    ...     Display_Parameter_in_Report_Header=${False}
    set test variable    &{ReportDetails}
    When user navigates to menu Configuration | Application Setup
    And user navigates to Report tab
    Then user updates report using fixed data
    And Report updated successfully with message 'Record updated successfully'
