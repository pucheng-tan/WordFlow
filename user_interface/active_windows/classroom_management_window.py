import tkinter as tk
from user_interface.active_windows import active_window
from user_interface.components import list_view, header
from managements import classroom_management

class ClassroomManagementWindow(active_window.ActiveWindow):
    """Window for viewing list of classrooms
    Has buttons for performing different classroom actions.
    """
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.classroom_management = classroom_management.ClassroomManagement()
        self.heading_frame = header.Header(self.frame, "Classroom Management") 

        HEADINGS = ["Name", "Managed By", "Members"]
        FIELDS = ["name", "Managed By", "Members", "id"]
        self.history_list = list_view.ListView(self.frame, HEADINGS, FIELDS, self.load_classrooms)
        self.history_list.set_action_button("View/Edit", self.view_classroom, True, True)
        self.history_list.set_action_button("Add", self.add_classroom)

    def add_classroom(self):
        print("Add classroom has been called")

    def view_classroom(self):
        classroom = self.history_list.get_focus()
        print(classroom)


    def load_classrooms(self, limit, last_classroom=None):
        start_at = " " if not last_classroom else last_classroom["name"]
        classrooms = self.classroom_management.get_classrooms(limit, start_at)
        return self.format_data(classrooms)


    def format_data(self, data):
        # get who is managing the class, and how many members
        for id, item in data.items():
            managed_by = self.classroom_management.get_classroom_management(item)
            item["Managed By"] = self.person_list_to_string(managed_by)
            member_count = len(item["members"])
            item["Members"] = member_count
            # put the id in so that we can reference it easily later
            item["id"] = id

        return list(data.values())


    def person_list_to_string(self, person_list):
        """ Turn a list of user profiles into a comma separated string
        Args:
            person_list: [UserProfile]
        Returns: "email_1, email_2,..., email_n"
        """
        email_list = [person["email"] for person in person_list]
        return ", ".join(email_list)