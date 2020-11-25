from managements.application_management import ApplicationManagement
from services.school_service import SchoolService

class SchoolManagement(ApplicationManagement):

    _service = SchoolService()

    def create_school(self, school_name, owner_uid):
        """Creates the school. Needs an owner in order to be created.
        """
        # make school object
        school = {
            "name": school_name
        }
        # the owner attribute needs the school id to be set
        create_result = self._service.create_school(school)
        school["id"] = create_result["id"]
        # then update the school
        school = self.update_school_owner(school, owner_uid)

        self._context.set_user(0, owner_uid, school["id"])
        return create_result 

    def update_school_owner(self, school, owner_uid):
        school["owner"] = "Schools/" + school["id"] + "/UserProfiles/" + owner_uid
        result = self._service.update_school(school)
        return school

    def get_school_users(self, school_id, privilege):
        # TODO
        # Returns a list of all the user ids with that privilege level in the school
        if privilege == 2:
            standard_user_ids = [0, 1, 2, 3, 4, 5]

        return standard_user_ids

