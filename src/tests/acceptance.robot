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

User Can Add Book To Collection
    Go To Books Page
    Set Book Title  Robot Acceptance Test Book
    Set Book Author  Robot I. Acceptance
    Set Book Year  2021
    Submit Book
    Book Should Be Displayed On Reload  Robot Acceptance Test Book

All Books Are Fetched From Database Then Displayed
    Add Book To Database  First Book Added  Firstly Authored  2020
    Add Book To Database  Second Book Added  Secondly Authored  2021
    Book Should Be Displayed On Reload  First Book Added
    Book Should Be Displayed On Reload  Second Book Added

User Can Add Podcast To Collection
    Go To Podcasts Page
    Set Podcast Title  Podcast Acceptance Testing 
    Set Podcast Name  Acceptance Testing Podcast
    Set Podcast Description  Podcast About Acceptance Testing
    Submit Podcast
    Podcast Should Be Displayed On Reload  Podcast Acceptance Testing 

All Podcasts Are Fetched From Database Then Displayed
    Add Podcast To Database  First Podcast Added  Podcast Name 1  First Podcast Description
    Add Podcast To Database  Second Podcast  Podcast Name 2  Second Podcast Description
    Podcast Should Be Displayed On Reload  Podcast Acceptance Testing    
    Podcast Should Be Displayed On Reload  Podcast Acceptance Testing   

*** Keywords ***
Set Book Author
    [Arguments]  ${book_author}
    Input Text  id:author  ${book_author}

Set Book Title
    [Arguments]  ${book_title}
    Input Text  id:title  ${book_title}

Set Book Year
    [Arguments]  ${book_year}
    Input Text  id:year  ${book_year}

Set Weblink Title
    [Arguments]  ${weblink_title}
    Input Text  name:title  ${weblink_title}

Set Weblink Url
    [Arguments]  ${weblink_url}
    Input Text  name:url  ${weblink_url}

Set Podcast Title
    [Arguments]  ${podcast_title}
    Input Text  id:title  ${podcast_title}

Set Podcast Name
    [Arguments]  ${podcast_name}
    Input Text  id:name  ${podcast_name}

Set Podcast Description
    [Arguments]  ${podcast_description}
    Input Text  id:description  ${podcast_description}

Submit Book
    Submit New WinkVink

Submit Weblink
    Submit New WinkVink

Submit Podcast
    Submit New WinkVink

Book Should Be Displayed On Reload
    [Arguments]  ${book_title}
    Go To Books Page
    Page Should Contain  ${book_title}

Weblink Should Be Displayed On Reload
    [Arguments]  ${weblink_title}
    Go To Weblinks Page
    Page Should Contain  ${weblink_title}

Podcast Should Be Displayed On Reload
    [Arguments]  ${podcast_title}
    Go To Podcasts Page
    Page Should Contain  ${podcast_title}
