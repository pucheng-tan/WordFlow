from managements.application_management import ApplicationManagement
from services import classroom_service

class ClassroomManagement(ApplicationManagement):

    _service = classroom_service.ClassroomService()

    def get_classrooms(self, limit=10, start_at_name=" "):
        """Returns a list of classrooms belonging to the school
        Built for pagination. Use start_at_name and sort on the classroom name

        Args:
            limit: max number of results to return
            start_at_name: the classroom name to start with (ie: get results after this name)
        """
        school_id = self._context.get_school_id()
        return ClassroomManagement._service.get_classrooms(school_id, limit, start_at_name)
        
    def get_classroom_management(self, classroom):
        return ClassroomManagement._service.get_user_profiles(classroom["managed_by"])

    def get_classroom_members(self, classroom):
        return ClassroomManagement._service.get_user_profiles(classroom["members"])

    def add_classroom(self, classroom):
        pass

    def assign_classroom_teacher(self, classroom_id, teacher_uid):
        pass

    def add_students_to_classroom(self, classroom_id, student_uids):
        pass

    def delete_classroom(self, classroom_id):
        pass