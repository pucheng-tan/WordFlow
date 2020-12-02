from services.api_service import API

class ClassroomService:
    _api = None

    def __init__(self):
        if not ClassroomService._api:
            ClassroomService._api = API.get_api()

    def get_classrooms(self, school_id, limit, start_at):
        """ Get paginating list of classrooms belonging to school
        """
        sort = {"name": True}
        where_clauses = [["name", ">", start_at]]

        path = "Schools/" + school_id + "/Classrooms/"
        results = ClassroomService._api.get(path=path, limit=limit, order_by=[sort], where_clauses=where_clauses)
        return results

    def update_classroom(self, school_id, classroom):
        """Create a new classroom or update an existing one
        """
        path = "Schools/" + school_id + "/Classrooms"
        response = ClassroomService._api.post(path=path, data=classroom)
        return response

    def check_class_name_exists(self, school_id, class_name):
        """Before creating a classroom, check that it's a unique name
        Will return true if the name already exists in the school
        """
        path = "Schools/" + school_id + "/Classrooms/"
        where_clauses = [["name", "==", class_name]]
        response = ClassroomService._api.get(path=path, where_clauses=where_clauses)
        class_exists = True if response and "name" in resonse else False
        return class_exists

