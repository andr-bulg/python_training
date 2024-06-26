*** Settings ***
Library    rf.AddressBook
Library    Collections
Suite Setup    Init Fixtures
Suite Teardown    Destroy Fixtures


*** Test Cases ***
Add new group
    ${old_list} =    Get Group List
    ${group} =    New Group  name1  header1  footer1
    Create Group  ${group}
    ${new_list} =    Get Group List
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}


Delete group
    ${old_list} =    Get Group List
    ${len} =    Get Length  ${old_list}
    ${index} =    Evaluate    random.randrange(${len})    random
    ${group}    Get From List    ${old_list}  ${index}
    Delete Group  ${group}
    ${new_list} =    Get Group List
    Remove Values From List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}


Modify group
    ${old_list} =    Get Group List
    ${len} =    Get Length  ${old_list}
    ${index} =    Evaluate    random.randrange(${len})    random
    ${modified_group}    Get From List    ${old_list}  ${index}
    ${group} =    New Group  name10  header10  footer10
    Modify Group  ${modified_group}   ${group}
    ${new_list} =    Get Group List
    Remove Values From List  ${old_list}  ${modified_group}
    Append To List  ${old_list}  ${group}
    Group Lists Should Be Equal  ${new_list}  ${old_list}

