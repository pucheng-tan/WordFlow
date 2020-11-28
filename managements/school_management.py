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

    # TODO: user_management_window most likely will need this
    def get_school_user_profiles(self, privilege):
        """Gets all the user data of users in the school with the chosen
        privilege level.

        Args:
            school_id: The id of the school to get the users.
            privilege: The privilege level of the users to get.

        Returns:
             Returns a list of dictionaries containing user profiles that have
             the information of:

             id
             privilege level
             email
             display_name
        """

        school_id = SchoolManagement._context.get_school_id()
        user_documents = self._service.get_user_documents_by_privilege(school_id, privilege)

        user_profiles = []
        for user_id in user_documents:
            user_profiles.append(user_documents[user_id])

        return user_profiles

