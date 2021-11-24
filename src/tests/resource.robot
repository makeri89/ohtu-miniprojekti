*** Settings ***
Library  SeleniumLibrary

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

Open Browser Before Configuration
    Open Browser  browser=${BROWSER}

Prepare Browser
    Open Browser Before Configuration
    Configure Browser
