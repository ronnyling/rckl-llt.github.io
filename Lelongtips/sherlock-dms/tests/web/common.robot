*** Settings ***
Library         SeleniumLibrary    timeout=20    implicit_wait=1.5   run_on_failure=Capture Page Screenshot
Library         ${EXECDIR}${/}resources/web/Common/AlertCheck.py
Library         ${EXECDIR}${/}resources/web/Common/LoginPage.py
Library         ${EXECDIR}${/}resources/web/Common/MenuNav.py
Library         ${EXECDIR}${/}resources/web/Common/Logout.py
Library         ${EXECDIR}${/}resources/web/Common/POMLibrary.py
Library         ${EXECDIR}${/}resources/components/Pagination.py
Library         ${EXECDIR}${/}resources/components/PopUpMsg.py
Library         ${EXECDIR}${/}resources/components/Button.py
Library         ${EXECDIR}${/}resources/components/TextField.py
Library         ${EXECDIR}${/}resources/components/Tab.py
Library         ${EXECDIR}${/}resources/components/Toggle.py
Library         ${EXECDIR}${/}setup/hanaDB/HanaDB.py
Library         ${EXECDIR}${/}setup/csvreader/CsvLibrary.py
Library         ${EXECDIR}${/}resources/web/CustTrx/UICustTrxCommon.py
