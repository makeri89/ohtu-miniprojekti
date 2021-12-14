*** Settings ***
Library  SeleniumLibrary
Library  ../AppLibrary.py

*** Variables ***
${SERVER}  localhost:5000
${BROWSER}  headlesschrome
${DELAY}  0.0 seconds
${BOOKS URL}  http://${SERVER}/books
${HOME URL}  http://${SERVER}
${WEBLINKS URL}  http://${SERVER}/weblinks
${PODCASTS URL}  http://${SERVER}/podcasts
${COURSES_URL}  http://${SERVER}/courses

*** Keywords ***
Configure Browser
    Set Selenium Speed  ${DELAY}

Go To Books Page
    Go To  ${BOOKS URL}

Go To Home Page
    Go To  ${HOME URL}

Go To Weblinks Page
    Go To  ${WEBLINKS URL}

Go To Podcasts Page
    Go To  ${PODCASTS URL}

Go To Courses Page
    Go To  ${COURSES_URL}

Home Page Should Be Open
    Title Should Be  Front page - WinkVink
    Page Should Contain  WinkVink

Open Browser Before Configuration
    Open Browser  browser=${BROWSER}

Prepare Browser
    Open Browser Before Configuration
    Configure Browser

Submit New WinkVink
    Click Button  Add
