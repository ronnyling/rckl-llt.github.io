@ECHO OFF
REM BFCPEOPTIONSTART
REM Advanced BAT to EXE Converter www.BatToExeConverter.com
REM BFCPEEXE=C:\Users\j.tang.ling.ling\Documents\np-testbot\install.exe
REM BFCPEICON=C:\Program Files (x86)\Advanced BAT to EXE Converter v4.11\ab2econv411\icons\icon13.ico
REM BFCPEICONINDEX=-1
REM BFCPEEMBEDDISPLAY=0
REM BFCPEEMBEDDELETE=1
REM BFCPEADMINEXE=0
REM BFCPEINVISEXE=0
REM BFCPEVERINCLUDE=0
REM BFCPEVERVERSION=1.0.0.0
REM BFCPEVERPRODUCT=NP DMS AutoBot
REM BFCPEVERDESC=By j.tang.ling.ling@accenture.com
REM BFCPEVERCOMPANY=Accenture Newspage Sdn Bhd
REM BFCPEVERCOPYRIGHT=Copyrighted by Accenture Newspage
REM BFCPEOPTIONEND
@ECHO ON
@echo off
pip install cryptography --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade setuptools --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade ez_setup --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade robotframework-seleniumlibrary --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade robotframework-faker --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install -U robotframework-pabot --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade pyautogui --trusted-host pypi.org --trusted-host files.pythonhosted.org
REM look for instruction at https://pyautogui.readthedocs.io/en/latest/index.html
pip install numpy==1.22.3 --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade robotframework --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade requests --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade pandas --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade xlrd --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade faker-e164 --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade robotframework-angularjs --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install .\robotframework-jsonlibrary\ --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install --upgrade pylint --trusted-host pypi.org --trusted-host files.pythonhosted.org
REM pip install "hdbcli-2.3.134.zip"
pip install hdbcli --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install nested-lookup --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install beautifulsoup4 --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install robotframework-pageobjectlibrary --trusted-host pypi.org --trusted-host files.pythonhosted.org
pip install ruamel.yaml --trusted-host pypi.org --trusted-host files.pythonhosted.org

REM cmd /C pip install -U wxPython
REM cmd /C pip install robotframework-ride
REM Look for example at https://github.com/franz-see/Robotframework-Database-Library/
REM http://test-automation-timestamps.blogspot.com/2017/02/selecting-context-menu-item-with-robot.html
REM cmd /C pip install --upgrade robotframework-autoitlibrary
REM follow instruction here http://www.codingwhy.com/view/895.html
REM cmd /C pip install --upgrade PyMsSQL
REM look for instruction at https://franz-see.github.io/Robotframework-Database-Library/api/1.0.1/DatabaseLibrary.html
REM call python -m pip install --upgrade robotframework-extendedselenium2library
REM call python -m pip install --upgrade robotframework-databaselibrary