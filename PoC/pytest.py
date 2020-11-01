import requests
from firebase import firebase
import firebase_admin
# from firebase_admin import auth
# from firebase_admin import credentials

url = "http://api.seazon.org/2-0-1-1-1-0/0-0-1/2-9-45-85-3-4/api.txt"

ecode = requests.get(url)

# print(ecode.text)

# import firebase_admin
# from firebase_admin import credentials

# cred = credentials.Certificate("path/to/serviceAccountKey.json")
# firebase_admin.initialize_app(cred)

# We dont need authentication right now because the data base is in test mode for 30 days.
#authentication = firebase.FirebaseAuthentication('vWQEWcMriE0abC3WbkMrMODz4hAg2cUZ2M7Pdq54', 'cameronmcleod71@gmail.com')
firebase = firebase.FirebaseApplication(
    'https://cmpt370-group2.firebaseio.com')
result = firebase.get('/users', None)

#This will print whatever is in the data base at /users (currently empty)
#should be none
print("this is what it returns when nothing is in the database")
print(result)

to_be_deleted = {'User_Name': 'Cameron Mcleod', 'Email': 'blah blah'}
#This will add the data 'to be delted' to our database in a directory called /test
print_database = firebase.post('/test', to_be_deleted)
print("the data we just added has been hashed")
print(print_database)

#after I run this PoC I can go to the database page on the firebase website and actually see the data being added
#youlle also notice that you cant just print the data because it is autimatically hashed

result = firebase.get('/test', None)
print(
    "Since I have ran the PoC multiple times, when I try to get the /test dir, I see lots of data"
)
print(" this is starting to get hard to read")
print(result)

#use firebase put command to change data in firebase
firebase.put('/test/-MIHzxRT4UJL4YFBt1lf', 'Email',
             'cameronmcleod71@gmail.com')

# firebase.delete('/test', name)
