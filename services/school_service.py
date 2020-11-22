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