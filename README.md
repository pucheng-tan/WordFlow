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


## How to run our PoC!

Note: Prefered python version is python 3.6!

### For Mac:

1. clone our git repo and run make
2. run make in the root
3. enter into the created virual environment, type 'soure env/bin/activate'
4. type 'pytest PoC/services' to run tests
5. when finished running tests, type 'deactivate' to leave the virtual environment
6. type 'rm -rf env' to remove the environment

#### (Assuming the windows user does have access to make)

1. clone git repo
2. create the virual environment in the root folder of the repo 'python3 -m venv env'
3. enter into the env, type '. env\Scripts\activate'
4. install dependencies using 'pip3 install -r requirements.txt'
5. run 'pytest PoC\services'
6. when finished running tests, type 'deactivate 'rm -f env'

Known issues on windows:

1. You are not alloud to run scripts. First enter windows power shell in administrator, then enter the command 'set-executionpolicy remotesigned'



