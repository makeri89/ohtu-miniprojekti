*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${BOOKS URL}  http://${SERVER}/books
${HOME URL}  http://${SERVER}
${WEBLINKS URL}  http://${SERVER}/weblinks

*** Keywords ***
Configure Browser
    Set Selenium Speed  ${DELAY}

Go To Books Page
    Go To  ${BOOKS URL}

Go To Home Page
    Go To  ${HOME URL}

Go To Weblinks Page
    Go To  ${WEBLINKS URL}

Home Page Should Be Open
    Title Should Be  WinkVink
    Page Should Contain  Hello, fellow Winkers!

Open Browser Before Configuration
    Open Browser  browser=${BROWSER}

Prepare Browser
    Open Browser Before Configuration
    Configure Browser

Submit New WinkVink
    Click Button  Add
