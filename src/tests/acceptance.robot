*** Settings ***
Resource  resource.robot
Suite Setup  Prepare Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
User Can Add Weblink To Collection
    Go To Weblinks Page
    Set Weblink Title  test_title
    Set Weblink Url  http://example.com/
    Submit Weblink
    Weblink Should Be Displayed On Reload  test_title

All Weblinks Are Fetched From Database Then Displayed
    Add Weblink To Database  weblink_name1  http://example1.com 
    Add Weblink To Database  weblink_name2  http://example2.com 
    Weblink Should Be Displayed On Reload  weblink_name1
    Weblink Should Be Displayed On Reload  weblink_name2

*** Keywords ***
Set Weblink Title
    [Arguments]  ${weblink_title}
    Input Text  name:title  ${weblink_title}

Set Weblink Url
    [Arguments]  ${weblink_url}
    Input Text  name:url  ${weblink_url}

Submit Weblink
    Click Button  Add

Weblink Should Be Displayed On Reload
    [Arguments]  ${weblink_title}
    Go To Weblinks Page
    Page Should Contain  ${weblink_title}
