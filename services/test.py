from user_management import PRIVILEGE, UserManagement
from school_management import SchoolManagement

UM = UserManagement()
SM = SchoolManagement()

def create_school():
    email = "blahblah@test.ca"
    display_name = "Steve Smith"
    password = "Pass123!"
    school_name = "I am a school"

    user = UM.create_auth_user(email, password, display_name)

    school = SM.create_school(school_name, user["id"])

    # this is wrong- context needs to be set, but from within UserManagement:
    UM._context.set_user(PRIVILEGE["super_admin"], user["id"], school["id"])

    school_user = UM.create_user_profile(email, user["id"], PRIVILEGE["super_admin"], display_name)


create_school()

