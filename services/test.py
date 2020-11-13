from api_service import API
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import auth
from datetime import datetime, timezone
from user import User, PrivilegeLevel

# JUST A TEMPORARY FILE USED FOR EXPERIMENTATION WITH API STUFF
# DON'T MIND ME
api = API()
db = API._get_db()

SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
TEST_SCHOOL_ID = SCHOOL_ID
CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"
TARA_USER_ID = "kUJrBZtlYJeU8ZLAFFcm4dAJVBt2"
email = "pucheng@hotmail.yea"

# The where() method takes three parameters: a field to filter on, a comparison operator, and a value. Firestore supports the following comparison operators:

# < less than
# <= less than or equal to
# == equal to
# > greater than
# >= greater than or equal to
# != not equal to
# array-contains
# array-contains-any
# in
# not-in

# test_complicated_query()


# - "get all challenge results from users of classroom X at school X where date is between Y and Z, the challenge mode is Q, and the challenge was an assignment"
def getting_users():
    # - "get all users belonging to classroom X"
    classroom = db.collection("Schools").document(SCHOOL_ID).collection("Classrooms").document(CLASSROOM_ID)
    classroom = api._to_dict(classroom, True)

    members = classroom["Members"]
    member_references = []
    for member in members:
        m = member.get()
        print(member.path)
        member_references.append(member)


# where: date between x and y // y = Nov 1
# def timestamp_stuff():
    # datetime(year, month, day, hour=0, minute=0, second=0, microsecond=0, tzinfo=None, *, fold=0)
    tz = timezone.utc
    start_date = datetime(2020, 1, 1, tzinfo=tz) # DatetimeWithNanoseconds(2020, 1, 1, 1, 4)
    end_date = datetime(2020, 11, 1, tzinfo=tz)
    # where: challenge mode = 0
    # where: assignmentID exists
    # challenge_results = db.collection_group("History")
    # challenge_results = db.collection_group("History").where("UserProfile", "in", member_references)
    challenge_results = db.collection_group("History").where("UserProfile", "in", member_references).order_by("AssignmentID")
    # challenge_results = db.collection_group("History").where("UserProfile", "in", member_ids).where("Mode", "==", 1)
    challenge_results = db.collection_group("History").where("UserProfile", "in", member_references).where("DateCompleted", ">", start_date).where("DateCompleted", "<", end_date)
    ch_r_dict = api._to_dict(challenge_results, False)
    #print(ch_r_dict)



def serching_users():
    # - "get all users matching search X, matching their email address, display name, or privilege level"
    search_term = "puchen"
    # need to check that index is not out of range?
    temp = search_term[0].upper() + search_term[1:]
    #print(temp)
    search_fields = ["DisplayName", "Email"]

    # .where("last_name", ">=", last_name.upper())\ # Solution from Stack Overflow. Doesn't like the UT8 thing and returns weird results
    #         .where("last_name", "<=", last_name.lower() + "\uf8ff")\
    #         .stream()
    results = []
    for field in search_fields:
        matching_users = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").where(field, ">=", temp).where(field, "<=", temp)
        results.append(api.to_dict(matching_users))

# need to remove duplicate values
#print(results)

# - "get all assignments for user X, who is part of classroom Y, where the assignment has not been completed"
# - "get random challenge content of mode X"

# - "put new challenge result X for user Y of school Z"
#set

def _test_setting_data():
    data = {"Mode":4}

    results = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document(USER_ID).collection("History").document()
    resultsss = results.set(data)

    print(results.id)
    print(resultsss)


def update_user_info():
# - "update user X. update their data in such a way that it doesn't mess anything else up"
    data = {"Email":email}

    # Addeed an email for Pucheng
    # merge= True to avoid deleting important info...
    results = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document(USER_ID).set(data, merge=True)
    print(results)
    # resultsss = results.set(data)
    



# Adding to a non existing History Collention    
def adding_to_no_existing_history_func():
    # result: Creates the whole collection for you and then adds the data as intended.
    data = {"Mode":4}

    results = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document(TARA_USER_ID).collection("History").document()
    resultsss = results.set(data)

    print(results.id)
    print(resultsss)

# Interesting Note = deleting a document does not delete its subcollection
def deleting_stuff():
# - "delete user X. Delete their data in such a way that it doesn't mess anything else up"

    results = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document("HAi").delete()
    # results when deleting gives you seconds and nanos
    # delete doesn't really tell you if succesfull
    # All his stuff is still acccecable but will not show up in query results
    print(results)


def deleting_steves_stuff():
# Deleting steves entire life history :)

    # we are trying to delete is entire collections and everythingin it
    collections = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document("steve").collections()
    
    # Looping throgh collections references
    for i in collections:
        # i is a collection reference object
        docs = i.stream()
        for doc in docs:
            doc.reference.delete()
        
    
    # print(collections)


# Making steve again after he got rolled by the world
def createing_steve():
# Yea we are creating a new User
    data = {"id": 44}
    # Dont forget merge=True
    results = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document("steve").set(data, merge=True)

    # New steve did not get old steves stuff
    print(results)


def create_school():
    # TODO new school needs to have a name and an owner. The other collections will be automatically created as needed so don't bother making them
    results = db.collection("Schools").document()

# - create an account, and make sure it also creates a UserProfile
# first create the user as a user proper, so we can get the User UID
def auth_new_user():
    user = {
        "email": "testq@test.ca", 
        "emailVerified": True, # default is false
        "phoneNumber": "123-345-5678",
        "password": "123Pass!", # must be at least 6 characters long for Firestore, we may want to be more strict
        "Schools": SCHOOL_ID, 
        "displayName": "New User"
        }

    u = auth.create_user(display_name=user["displayName"], email=user["email"], password=user["password"])
    print(u.uid)
    

    # second make the user as the UserProfile within the school
    # user_profile = {
    #     ""
    # }


# - authenticate to an account, and get the UserProfile back
def auth_login():
    pass

# - getting user data but not logging in
def auth_get_user():

    # user = auth.get_user_by_email("test1@test.ca")
    # user = auth.get_user_by_phone_number("4")
    user = auth.get_user(USER_ID) #<firebase_admin._user_mgt.UserRecord object at 0x000001A0867694E0> https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/auth/UserRecord
    print(user.uid)
    # user = auth.get_user("12") # "firebase_admin._auth_utils.UserNotFoundError: No user record found for the provided user ID: 12."

    # bulk
    result = auth.get_users([
        auth.UidIdentifier(USER_ID),
        auth.EmailIdentifier("taramepp@gmail.com"),
        auth.UidIdentifier(TARA_USER_ID),
        auth.UidIdentifier("George")
    ])

    for user in result.users:
        print("found: " + user.uid)

    for uid in result.not_found:
        print("not found: " + str(uid)) # <firebase_admin._user_identifier.UidIdentifier object at 0x000001B81C40B710>


# - delete both the account and the userprofile
# - maybe make another school and create the same user in both schools


# auth_new_user()

# ({"Schools": TEST_SCHOOL_ID, "UserProfiles": TEST_USER_ID, "History": API.WHERE_CLAUSE}, [["Mode", "==", "0"]], "2020101513071234"),
#     ({"History": API.SEARCH_ALL}, [["UserProfile", "==", "BMSoKUzVnRYn103t2Oi6Nacv9X03"], ["AssignmentID", "exists"]], "2020101513091234"),
#     ({"Schools": TEST_SCHOOL_ID, "Classrooms": API.WHERE_CLAUSE}, [["Members", "array_contains", TEST_USER_ID]], "uWkea95OBZ1d94kaPThK"),
#     ({"Schools": TEST_SCHOOL_ID, "Classrooms": TEST_CLASSROOM_ID}, [], TEST_CLASSROOM_ID)

def test_first_func():
    # path = {"History": API.SEARCH_ALL}
    where = [["UserProfile", "==", "BMSoKUzVnRYn103t2Oi6Nacv9X03"]]
    order_by = {"AssignmentID": True}

    result = api.get_all("History", where, order_by)
    print("CALLING THE GET")
    # # print(api._to_dict(result, True))
    statement = api.get_last_statement()
    print(statement)
    print(result)

    # print("DOING IT MANUALLY")
    # result = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").document(USER_ID).collection("History").where("Mode", "==", 0)
    # # result = api._to_dict(result, False)
    # print(result)

    # result = {'2020101513071234': {'DateCompleted': datetime(2020, 11, 1, 6, 0, tzinfo=timezone.utc), 'UserProfile': "<google.cloud.firestore_v1.document.DocumentReference object at 0x0000020F17913898>", 'Mode': 0, 'CharsTyped': 612, 'CharsCorrect': 600, 'Duration': 120}}
    # results = list(result)
    # print(results)

def test_filter():
    comparisons = ["<", ">", "<=", ">="]

    clauses = [["1", "<", 30], ["2", "==", 500]]

    # I want to get the fields where the second clause is in comparisons

    x = map(lambda q: q[0], filter(lambda b: b[1] in comparisons, clauses))

    print(len(x))

def test_params3():
    path = {"Schools": SCHOOL_ID, "Classrooms": CLASSROOM_ID}

    result = api.get(path)
    print(result)

def test_params2():
    path = {"Schools": SCHOOL_ID}
    collection_name = "Classrooms"
    user_path = "Schools/" + SCHOOL_ID + "/UserProfiles/" + USER_ID
    # Valid choices are: <, <=, ==, >, >=, array_contains, array_contains_any, in.
    where = [["Members", "array_contains_any", [user_path]]]

    string_in_data = "Schools/o2lTSAI6X4yGdIZ0huB9/UserProfiles/BMSoKUzVnRYn103t2Oi6Nacv9X03"
    if "cheese/" == "c" + "heese" + "/":
        print("THEY MATCH")
    else:
        print("PATH:")
        print(repr(user_path))
        print(len(user_path))
        print("DATA:")
        print(repr(string_in_data))
        print(len(string_in_data))
    try:
        result = api.get(path, collection_name=collection_name, where_clauses=where)
        print(result)
        print(api.get_last_statement())
    except:
        print(api.get_last_statement())

    

def test_params1():
    collection_name = "History"
    where_clauses = [["UserProfile", "string_starts", "Schools/" + TEST_SCHOOL_ID]]
    order_by = [{"AssignmentID": True} ] 

    # try:
    result = api.get_all(collection_name, where_clauses, order_by)
    print(result)
    # except Exception as e:
    #     print(api.get_last_statement())
    #     print(e)
    
def test_dicts():
    temp = [{"UserProfile": True}, {"Another": False}]
    # temp2 = temp.get("UserProfile")
    # print(temp2)
    for order in temp:
        key = list(order.keys())[0]
        value = order[key]
        print(key)
        print(value)
        # print(list(order.items())[0])
        # print(list(order.keys())[0])
        # print(list(order.values())[0])


def test_post():
    path = "/Albatross/AlbatrossID/Bat/BatID/Capybara"
    # path = {"Albatross": "AlbatrossID", "Bat": "BatID", "Capybara": None}
    data = {
            "id": "CapybaraID", 
            "Boolean": True, 
            "Date": datetime.now(), 
            "Number": 3.14159, 
            "Array": [5, False, "cheese"], 
            "None": None, 
            "object": {
                "Dog": 6, 
                "Emu": {
                    "Fox": [1, 2, 3]
                }
            }
        }

    result = api.post(path, data, False)
    print(result)

def test_path():
    path_string = "Schools/o2lTSAI6X4yGdIZ0huB9/Classrooms/classID/Albratross"
    split_path = path_string.split("/")

    num_collections = len(split_path) // 2
    path = []

    print(split_path)
    print(num_collections)
    for i in range(0, num_collections):
        collection_index = i * 2
        document_index = collection_index + 1
        collection = split_path[collection_index]
        document = split_path[document_index]
        path.append({collection: document})
        print("COLLECTION:")
        print(collection)
        print(document)

    print(path)
    if len(split_path) % 2 == 1:
        print(split_path[-1])


def test_is_document():
    query = db.collection("Schools").document("id").collection("Classrooms")
    doc_type = str(type(query))
    
    if "DocumentReference" in doc_type:
        print("It is a document!")
    else:
        print(doc_type)


def test_string_path():
    TEST_DATE = datetime(2020, 10, 30, tzinfo=timezone.utc)
    path = "Schools/" + TEST_SCHOOL_ID + "/UserProfiles/" + USER_ID + "/History"
    where_clauses = [["DateCompleted", ">", TEST_DATE], ["Mode", "==", 0], ["Duration", "in", [120]]]
    limit = None
    order_by = []

    result = api.get(path, where_clauses, limit, order_by)
    print(result)

def test_user():
    id = "123"
    email = "email"
    display_name = "tara"
    privilege_level = PrivilegeLevel.super_admin
    phone_number = "123-3456"

    user = User(email, display_name, privilege_level, id, phone_number)

    user_dict = {
        "id": "123",
        "email": "email",
        "display_name": "tara",
        "privilege_level": PrivilegeLevel.super_admin,
        "phone_number": "123-3456"
    }

    # for key, value in user_dict.items():
    #     print(key)
    #     print(value)

    # print(user_dict.items())

    user = User().from_dict(user_dict)
    print(user.id)
    print(user.email)

def test_date():
    path = "Albatross/AlbatrossID/Bat/BatID/Capybara/CapybaraID"
    get_result = api.get(path)

    # date = get_result["Date"]

    # for attribute in get_result:
    #     value = get_result[attribute]
    #     # print(attribute)
    #     # print(value)
    #     # print(str(type(value)))
    #     if "DatetimeWithNanoseconds" in str(type(value)):
    #         # print("IT'S A DATE")
    #         date_timestamp = value.timestamp()
    #         new_date = datetime.fromtimestamp(date_timestamp)
    #         get_result[attribute] = new_date
    #     else:
    #         attribute_type = (str(type(value)))
    #         if "{" in attribute_type or isinstance(value, list):
    #             print("Right here")
    #             print(attribute)
    #             print(value)
    #     # if isinstance(attribute, list):
    #     #     print(attribute + " is an object")
    #     #     print(value)

    print(get_result)

    # date_timestamp = date.timestamp()

    # new_date = datetime.fromtimestamp(date_timestamp)
    # print(date)
test_date()


# - "authenticate user with <email, password, school>. Return their user data as well"
# check what happens when duplicate data is attempted to be enterred
# try to get leaderboard data- use an orderby and a limit of 20
# - should data be saved as a leaderboard (collection?) or should it be generated? Cached?
# - attempt to access data from a different school than the current user has
# 	- try to get some of that privacy stuff implemented at the school level