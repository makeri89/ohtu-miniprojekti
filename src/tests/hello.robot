*** Settings ***
Resource  resource.robot
Suite Setup  Prepare Browser
Suite Teardown  Close Browser

*** Test Cases ***
Flask Framework Should Be Operational
    Go To Home Page
    Home Page Should Be Open

*** Keywords ***
    