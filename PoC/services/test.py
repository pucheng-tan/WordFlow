from api_service import APIService
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from datetime import datetime, timezone

# JUST A TEMPORARY FILE USED FOR EXPERIMENTATION WITH API STUFF
api = APIService()
db = APIService.get_db()

SCHOOL_ID = "o2lTSAI6X4yGdIZ0huB9"
CLASSROOM_ID = "uWkea95OBZ1d94kaPThK"
USER_ID = "BMSoKUzVnRYn103t2Oi6Nacv9X03"

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
# - "get all users belonging to classroom X"
classroom = db.collection("Schools").document(SCHOOL_ID).collection("Classrooms").document(CLASSROOM_ID)
classroom = api.to_dict(classroom, True)

members = classroom["Members"]
member_references = []
for member in members:
    m = member.get()
    print(member.path)
    member_references.append(member)


# where: date between x and y // y = Nov 1
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
ch_r_dict = api.to_dict(challenge_results)
print(ch_r_dict)



# - "get all users matching search X, matching their email address, display name, or privilege level"
search_term = "puchen"
# need to check that index is not out of range?
temp = search_term[0].upper() + search_term[1:]
print(temp)
search_fields = ["DisplayName", "Email"]

# .where("last_name", ">=", last_name.upper())\ # Solution from Stack Overflow. Doesn't like the UT8 thing and returns weird results
#         .where("last_name", "<=", last_name.lower() + "\uf8ff")\
#         .stream()
results = []
for field in search_fields:
    matching_users = db.collection("Schools").document(SCHOOL_ID).collection("UserProfiles").where(field, ">=", temp).where(field, "<=", temp)
    results.append(api.to_dict(matching_users))

# need to remove duplicate values
print(results)

# - "get all assignments for user X, who is part of classroom Y, where the assignment has not been completed"
# - "get random challenge content of mode X"

# - "put new challenge result X for user Y of school Z"
# - "delete user X. Delete their data in such a way that it doesn't mess anything else up"
# - "authenticate user with <email, password, school>. Return their user data as well"
# check what happens when duplicate data is attempted to be enterred
# try to get leaderboard data- use an orderby and a limit of 20
# - should data be saved as a leaderboard (collection?) or should it be generated? Cached?
# - attempt to access data from a different school than the current user has
# 	- try to get some of that privacy stuff implemented at the school level