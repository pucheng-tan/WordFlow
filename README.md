    
# Group 2

Tuesday Tutorial

Abdul Salawu  
Cameron Mcleod  
Pucheng Tan  
Sarah Chen  
Tara Epp  
Yuta Ogawa


## How to run our PoC!

Note: Preferred Python version is python 3.6!

Also: our test PoC is located at PoC/services/test_api_service.py

### For Mac:

1. Clone the git repo
2. Run make in the root directory
3. Enter into the created virual environment by typing 'source env/bin/activate'
4. Run automated tests (see below)
5. When finished running tests, type 'deactivate' to leave the virtual environment
6. Type 'make clean' or use 'rm -rf env' to remove the environment

## For Windows:

NOTE: It is recommended to use PowerShell for running commands in Windows

1. Clone the git repo
2. Create the virual environment in the root folder of the repo with 'python3 -m venv env' (if this doesn't work, try python -m venv env)
3. Enter into the created virtual environment by typing '. env\Scripts\activate', (if this doesn't work, try just env\Scripts\activate)
4. Install dependencies using 'pip3 install -r requirements.txt'
5. Run automated tests (see below)
6. When finished running tests, type 'deactivate' and then 'rm env'

Known issues on Windows:

1. You do not have permission to run scripts. First open Windows PowerShell as administrator, then enter the command 'Set-ExecutionPolicy RemoteSigned'

## To run automated tests:
1. Run 'pytest' in the group2 directory
2. View test results in the .report.json file created in the group2 root directory
    - if tests are satisfactory to do a merge request, the "success" attribute will be true
    - if the success attribute is false, the possible problems are:
        - pytest was not run at the group2 root directory (all tests in the repository must be ran)
        - one or more tests could have failed, xfailed, xpassed, or given a warning (all tests must pass with no skips and no warnings)
    - tests that pass log only their nodeid, outcome, and metadata for brevity
    - all other tests will log additional debugging information
    - any warnings will be logged

