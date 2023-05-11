*** Settings ***
Resource          ${EXECDIR}${/}tests/restAPI/common.robot
Library           ${EXECDIR}${/}resources/restAPI/MasterDataMgmt/Distributor/DistributorPost.py

*** Test Cases ***

1 - Able To create distributor with given data
    [Documentation]    To create valid distributor with given data
    [Tags]     sysimp    hqadm    9.0   vmi01    BUG-NRSZUANQ-45290
    ${LOCALITY}=    create dictionary
    ...    ID=D3056170:2ECFB6F8-8BCC-45CE-AF0B-4C74EFFB658C
    ...    CITY_CD=WVMM
    ...    CITY_NAME=7GTBCYCGHTRFI6BOD204
    ${STATE}=    create dictionary
    ...    ID=D2DC0911:6AF51F88-9752-4CF1-9EB8-10693DCC7881
    ...    STATE_CD=MZNMZBQBCA
    ...    STATE_NAME=4R35HOS3BVATQ00V2GPG
    ...    COUNTRY=E6E3A813:4A6C3D1A-BC7D-4537-8F42-7E7B5780EC04
    ${COUNTRY}=    create dictionary
    ...    ID=E6E3A813:E0A7A66E-5E9A-4AFF-8FD3-A6C19B670A91
    ...    COUNTRY_CD=LHOHITBWNX
    ...    COUNTRY_NAME=XMY5MBVNUYRPT8DRBGV8
    ${PRICE_GRP}=    create dictionary
    ...    ID=CAC822D9:EC67DB3A-695C-4736-90CB-8579A551DAB6
    ...    PRICE_GRP_CD=ZAJMK0EG0QOFH8JNWVIN
    ...    PRICE_GRP_DESC=JHKXSRVWPMSKZIUKEVNALCLAHQTQNFNMNGLVVHCXANFBHFIQAQ
    ${OTH_PRICE_GRP}=    create dictionary
    ...    ID=CAC822D9:036F2DBC-40B6-46E7-9C51-870275B30FF2
    ...    PRICE_GRP_CD=PGE2E1
    ...    PRICE_GRP_DESC=Pg E2E
    ${TIME_ZONE}=    create dictionary
    ...    TIMEZONE=Asia/Calcutta
    ${REPLENISHMENT_METHOD}=  create dictionary
    ...   REPLENISHMENT_METHOD=CMI_DIST
    set test variable  &{LOCALITY}
    set test variable  &{STATE}
    set test variable  &{COUNTRY}
    set test variable  &{PRICE_GRP}
    set test variable  &{OTH_PRICE_GRP}
    set test variable  &{TIME_ZONE}
    set test variable  &{REPLENISHMENT_METHOD}
    Given user retrieves token access as hqadm
    When user creates distributor with given data
    Then expected return status code 201
