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



