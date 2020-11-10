import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyDg_L6PD2cbSSFUTEpET56VOVKJaGWm5Nc",
    'authDomain': "cmpt370-group2.firebaseapp.com",
    'databaseURL': "https://cmpt370-group2.firebaseio.com",
    'projectId': "cmpt370-group2",
    'storageBucket': "cmpt370-group2.appspot.com",
    'messagingSenderId': "985070142874",
    'appId': "1:985070142874:web:8d5d49ddeaea00890be623",
    'measurementId': "G-YDBCLJ6R7X"
}

firebase = pyrebase.initialize_app(firebaseConfig)

auth = firebase.auth()

#Signup
print("Let's sign up an account!")
email=input("Enter your email: ")
password=input("Enter your password: ")
confirmpass=input("Confirm password: ")
if password==confirmpass:
    try:
        auth.create_user_with_email_and_password(email,password)
        print("Successfully signed up!")
    except:
        print("Password needs to be longer than 6 characters")
else:
    print("passwords do not match")

#Login
print("Let's log in to our account!")
email=input("Enter your email: ")
password=input("Enter your password: ")
try:
    auth.sign_in_with_email_and_password(email, password)
    print("Successfully signed in!")
except:
    print("Invalid user or password. Try again.")