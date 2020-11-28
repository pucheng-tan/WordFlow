from services.api_service import API

class SchoolService:
    """ Perform school-specific tasks
    """

    _api = None

    def __init__(self):
        if not SchoolService._api:
            SchoolService._api = API.get_api()

    def create_school(self, school):
        """ Creates the school through the API.
        """
        path = "Schools/"
        result = SchoolService._api.post(path, school)
        return result["document"]

    def update_school(self, school):
        if "id" not in school:
            raise Exception("School must have id attribute in order to be updated")
        path = "Schools/" + school["id"]
        result = SchoolService._api.post(path, school)
        return result["document"]

    def get_user_documents_by_privilege(self, school_id, desired_privilege,
                                       limit=10, start_at=" "):
        """Gets a list of user privileges from the database with the desired privilege.

        Args:
            school_id: The id of the school.
            desired_privilege: The privilege of the users to get from the school.
            limit: The pagination limit.
            start_at:

        Returns: A list of dictionaries with the key id associated with a
        dictionary containing the user's profile information.
        """
        sort = {"email": True}

        where_clauses = [["email", ">", start_at],
                         ["privilege_level", "==", desired_privilege]]

        path = "Schools/" + school_id + "/UserProfiles"
        user_documents = SchoolService._api.get(path=path, limit=limit, order_by=[sort],
                                      where_clauses=where_clauses)

        return user_documents



# school_service = SchoolService()
# print(school_service.get_user_profiles_by_privilege("3p1U6xAvKic1RvXMl5nJ", 0))
