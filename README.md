# To compile with makefile 
{instructions from Cameron go here}

# To run automated tests:
1. run pytest in the group2 directory
2. View test results in the .report.json file created in the group2 root directory
    - if tests are satisfactory to do a merge request, the "success" attribute will be true
    - if the success attribute is false, the possible problems are:
        - pytest was not run at the group2 root directory (all tests in the repository must be ran)
        - one or more tests could have failed, xfailed, xpassed, or given a warning (all tests must pass with no skips and no warnings)
    - tests that pass log only their nodeid, outcome, and metadata for brevity
    - all other tests will log additional debugging information
    - any warnings will be logged
    
# Group 2

Tuesday Tutorial

Abdul Salawu  
Cameron Mcleod  
Pucheng Tan  
Sarah Chen  
Tara Epp  
Yuta Ogawa
