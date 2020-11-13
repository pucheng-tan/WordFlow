from enum import Enum
from firebase_object import FirebaseObject

class PrivilegeLevel(Enum):
    
    super_admin = 0
    admin = 1
    standard = 1
    

class User(FirebaseObject):

    @property
    def _type_defs(self):
        return {
            "id": "string",
            "email": "string",
            "display_name": "string",
            "privilege_level": "int",
            "phone_number": "string",
        }

    def __init__(self, email=None, display_name=None, privilege_level=PrivilegeLevel.standard, id=None, phone_number=None):
        self.id = id
        self.email = email
        self.display_name = display_name
        self.privilege_level = privilege_level
        self.id = id
        self.phone_number = phone_number

        # self.validate()



