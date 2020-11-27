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

    def check_school_exists(self, school_name):
        """ Checks if the school already exists.
        Args:
            school_name: The name of the school.
        Returns:
             True if the school does exist. False if it does not.
        """
        path = "Schools/" + school_name
        result = SchoolService._api.get(path)

        if result:
            return True
        else:
            return False
