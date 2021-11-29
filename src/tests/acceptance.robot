*** Settings ***
Resource  resource.robot
Suite Setup  Prepare Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
User Can Add Weblink To Collection
    Set Weblink Title  test_title
    Set Weblink Url  http://example.com/
    Submit Weblink
    Weblink Should Be Submitted  test_title

*** Keywords ***
Home Page Should Be Open
    Title Should Be  WinkVink
    Page Should Contain  #something

Set Weblink Title
    [Arguments]  ${weblink_title}
    Input Title  id:#something  ${weblink_title}

Set Weblink Url
    [Arguments]  ${weblink_url}
    Input Url  id:#something  ${weblink_url}

Submit Weblink
    Click Button  #something

Weblink Should Be Submitted
    [Arguments]  ${weblink_title}
    Go To Home Page
    Page Should Contain  ${weblink_title}
