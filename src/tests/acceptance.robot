*** Settings ***
Resource  resource.robot
Suite Setup  Prepare Browser
Suite Teardown  Close Browser
Test Setup  Go To Home Page

*** Test Cases ***
User Can Add Courses
    Go To Courses Page
    Set Course Name  Testing with Robot Framework
    Submit Course
    Course Should Be Displayed On Reload  Testing with Robot Framework

All Courses Are Fetched From Database Then Displayed
    Add Course To Database  Testing 101
    Add Course To Database  Testing 102
    Course Should Be Displayed On Reload  Testing 101
    Course Should Be Displayed On Reload  Testing 102

User Can Add Weblink To Collection
    Go To Weblinks Page
    Set Weblink Title  test_title
    Set Weblink Url  http://example.com/
    Set Comment  Weblink Comment Acceptance
    Submit Weblink
    Weblink Should Be Displayed On Reload  test_title

All Weblinks Are Fetched From Database Then Displayed
    Add Weblink To Database  weblink_name1  http://example1.com  Weblink Comment Acceptance 1  Testing with Robot Framework
    Add Weblink To Database  weblink_name2  http://example2.com  Weblink Comment Acceptance 2  Testing with Robot Framework
    Weblink Should Be Displayed On Reload  weblink_name1
    Weblink Should Be Displayed On Reload  weblink_name2

User Can Delete Weblink From Database
    Add Weblink To Database  weblink_name1  http://example1.com  Weblink Comment Acceptance Delete  Testing with Robot Framework
    Weblink Should Be Displayed On Reload  weblink_name1
    Delete Weblink

User Can Add Book To Collection
    Go To Books Page
    Set Book Title  Robot Acceptance Test Book
    Set Book Author  Robot I. Acceptance
    Set Book Year  2021
    Set Comment  Book Comment Acceptance
    Submit Book
    Book Should Be Displayed On Reload  Robot Acceptance Test Book

All Books Are Fetched From Database Then Displayed
    Add Book To Database  First Book Added  Firstly Authored  2020  Book Comment 1  Testing with Robot Framework
    Add Book To Database  Second Book Added  Secondly Authored  2021  Book Comment 2  Testing with Robot Framework
    Book Should Be Displayed On Reload  First Book Added
    Book Should Be Displayed On Reload  Second Book Added

User Can Add Podcast To Collection
    Go To Podcasts Page
    Set Podcast Title  Podcast Acceptance Testing 
    Set Podcast Name  Acceptance Testing Podcast
    Set Podcast Description  Podcast About Acceptance Testing
    Set Comment  Podcast Comment Acceptance
    Submit Podcast
    Podcast Should Be Displayed On Reload  Podcast Acceptance Testing 

User Can Delete Book From Database
    Add Book To Database  First Book Added  Firstly Authored  2020  Book Comment Delete  Testing with Robot Framework
    Book Should Be Displayed On Reload  First Book Added
    Delete Book    

All Podcasts Are Fetched From Database Then Displayed
    Add Podcast To Database  First Podcast Added  Podcast Name 1  First Podcast Description  Podcast Comment 1  Testing with Robot Framework
    Add Podcast To Database  Second Podcast  Podcast Name 2  Second Podcast Description  Podcast Comment 2  Testing with Robot Framework
    Podcast Should Be Displayed On Reload  Podcast Acceptance Testing    
    Podcast Should Be Displayed On Reload  Podcast Acceptance Testing   

User Can Delete Podcast From Collection
    Add Podcast To Database  Podcast To Be Deleted In Acceptance Test  Podcast Name  Description of the Podcast  Podcast Comment Delete  Testing with Robot Framework
    Podcast Should Be Displayed On Reload  Podcast To Be Deleted In Acceptance Test
    Delete Podcast
    Podcast Should Not Be Displayed On Reload  Podcast To Be Deleted In Acceptance Test

User Can Delete Podcast From Database
    Add Course To Database  Testing Deleting
    Course Should Be Displayed On Reload  Testing Deleting
    Delete Course
    Course Should Not Be Displayed On Reload  Testing Deleting

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

Set Comment
    [Arguments]  ${comment}
    Input Text  id:comment  ${comment}

Set Course Name
    [Arguments]  ${name}
    Input Text  id:course_name  ${name}

Submit Book
    Submit New WinkVink

Submit Weblink
    Submit New WinkVink

Submit Podcast
    Submit New WinkVink

Submit Course
    Click Button  Add

Book Should Be Displayed On Reload
    [Arguments]  ${book_title}
    Go To Books Page
    Page Should Contain  ${book_title}

Book Should Not Be Displayed On Reload
    [Arguments]  ${book_title}
    Go To Books Page
    Page Should Not Contain  ${book_title}

Delete Book
    Click Element  xpath: ((//form))[last()]//input[@type='submit']       

Weblink Should Be Displayed On Reload
    [Arguments]  ${weblink_title}
    Go To Weblinks Page
    Page Should Contain  ${weblink_title}

Weblink Should Not Be Displayed On Reload
    [Arguments]  ${weblink_title}
    Go To Weblinks Page
    Page Should Not Contain  ${weblink_title}
    
Delete Weblink
    Click Element  xpath: ((//form))[last()]//input[@type='submit']

Podcast Should Be Displayed On Reload
    [Arguments]  ${podcast_title}
    Go To Podcasts Page
    Page Should Contain  ${podcast_title}

Podcast Should Not Be Displayed On Reload
    [Arguments]  ${podcast_title}
    Go To Podcasts Page
    Page Should Not Contain  ${podcast_title}

Delete Podcast
    Click Element  xpath: ((//form))[last()]//input[@type='submit']

Course Should Be Displayed On Reload
    [Arguments]  ${course_name}
    Go To Courses Page
    Page Should Contain  ${course_name}

Course Should Not Be Displayed On Reload
    [Arguments]  ${course_name}
    Go To Courses Page
    Page Should Not Contain  ${course_name}

Delete Course
    Click Element  xpath: ((//form))[last()]//input[@type='submit']