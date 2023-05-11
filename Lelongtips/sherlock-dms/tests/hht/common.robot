*** Settings ***
Library         AppiumLibrary    run_on_failure=AppiumLibrary.CapturePageScreenshot
Library         ${EXECDIR}${/}setup/hanaDB/HanaDB.py
Library         ${EXECDIR}${/}setup/csvreader/CsvLibrary.py
Library         ${EXECDIR}${/}setup/sqllite/SQLLite.py
Library         ${EXECDIR}${/}setup/hht/HHTApplicationSetup.py
Library         ${EXECDIR}${/}setup/hht/HHTLoginPage.py
Library         ${EXECDIR}${/}setup/hht/HHTPOMLibrary.py
Library         ${EXECDIR}${/}setup/hht/HHTMenuNav.py
Library         ${EXECDIR}${/}setup/hht/HHTTaskBarNav.py
Library         Process
Library         String
Library         DateTime
Library         FakerLibrary
Library         Collections
Library         OperatingSystem