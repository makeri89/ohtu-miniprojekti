*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  chrome
${DELAY}  0.5 seconds
${HOME URL}  http://${SERVER}

*** Keywords ***
Configure Browser
    Set Selenium Speed  ${DELAY}

Go To Home Page
    Go To  ${HOME URL}

Home Page Should Be Open
    Title Should Be  WinkVink
    Page Should Contain  Hello, fellow Winkers!

Open Browser Before Configuration
    Open Browser  browser=${BROWSER}

Prepare Browser
    Open Browser Before Configuration
    Configure Browser
