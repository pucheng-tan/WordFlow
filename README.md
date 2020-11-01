# Group 2

Tuesday Tutorial

Abdul Salawu  
Cameron Mcleod  
Pucheng Tan  
Sarah Chen  
Tara Epp  
Yuta Ogawa


## How to run our PoC!

### For Mac:

1. clone our git repo and run make
2. run make in the root
3. enter into the created virual environment, type 'soure env/bin/activate'
4. type 'pytest PoC/services' to run tests
5. when finished running tests, type 'deactivate' to leave the virtual environment
6. type 'rm -rf env' to remove the environment

### For Windows:

#### (Assuming the windows user does have access to make)

1. close git repo
2. create the virual environment 'py -m venv env'
3. enter into the env, type 'source env\Scripts\activate'
4. install dependencies using 'env\bin\pip3 install -r requirements.txt'
5. run 'pytest PoC\services'
6. when finished running tests, type 'deactivate 'rm -f env'


