    
# Group 2

Tuesday Tutorial

Abdul Salawu  
Cameron Mcleod  
Pucheng Tan  
Sarah Chen  
Tara Epp  


# How to run our Project:

Note: Preferred Python version is python 3.6

Here is a link to the download (scroll to the bottom of the page, to the Files section): https://www.python.org/downloads/release/python-360/

## Mac:

1. Clone the git repo
2. Run make in the root directory
3. Enter into the created virual environment by typing 'source env/bin/activate'
4. Run our program using python3 main.py, or run our gui by using run_gui.py
5. Run automated tests (see below)
6. When finished running tests, type 'deactivate' to leave the virtual environment
7. Type 'make clean' or use 'rm -rf env' to remove the environment

## Windows:

NOTE: It is recommended to use PowerShell for running commands in Windows

1. Clone the git repo
2. Run the PowerShell script 'windows-create-environment.ps1' to create and activate the virtual environment, and install dependencies.
3. When finished running tests, type 'deactivate' and then 'rm env'

### Known issues on Windows:

1. You do not have permission to run scripts. First open Windows PowerShell as administrator, then enter the command 'Set-ExecutionPolicy RemoteSigned'
- NOTE: if issues continue after trying the above fix, try the line 'Set-ExecutionPolicy Bypass'
2. The PowerShell script assumes that the "python" command rather than "python3" is used, which may cause issues on devices with multiple versions of python installed. Open the script in a text editor and change 'python' and 'pip' commands to 'python3' and 'pip3'.

## To run automated tests:
1. Run 'pytest' in the group2 directory
   - to run tests only in a specific file, run 'pytest ./path/to/test_file.py'
2. View test results in the .report.json file created in the group2 root directory
   - detailed test results are also displayed in the console
   - if tests are satisfactory to do a merge request, the "success" attribute will be true
   - if the success attribute is false, the possible problems are:
     - pytest was not run at the group2 root directory (all tests in the repository must be ran)
     - one or more tests could have failed, xfailed, xpassed, or given a warning (all tests must pass with no skips and no warnings)
   - tests that pass log only their nodeid, outcome, and metadata for brevity
   - all other tests will log additional debugging information
   - any warnings will be logged


## External Libraries
External libraries are listed in the requirements.txt file and will be installed by following the Mac or Windows instructions.
The following external libraries are used:
* requests 2.25.0 (https://pypi.org/project/requests/)
* firebase-admin 4.4.0 (https://pypi.org/project/firebase-admin/)
* pyttsx3 2.90 (https://pypi.org/project/pyttsx3/)
* yapf 0.30.0 (https://pypi.org/project/yapf/)
* pytest 6.1.2 (https://pypi.org/project/pytest/) 
* pytest-json-report 1.2.4 (https://pypi.org/project/pytest-json-report/)
* mock-firestore 0.7.3 (https://pypi.org/project/mock-firestore/) **Note that this library is not used in the master branch, only on branch #83 which is not fully implemented.

