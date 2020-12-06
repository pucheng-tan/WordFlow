import tkinter as tk
from user_interface.active_windows import active_window
from user_interface.components import list_view, header, item_view
from user_interface.components.form_view import FormView, EntryBox, MultiSelect
from managements import classroom_management, user_management

class ClassroomManagementWindow(active_window.ActiveWindow):
    """Window for viewing list of classrooms
    Has buttons for performing different classroom actions.
    """

    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.classroom_management = classroom_management.ClassroomManagement()
        self.user_management = user_management.UserManagement()
        self.heading_frame = header.Header(self.frame, "Classroom Management") 

        self.HEADINGS = ["Name", "Managed By", "Members"]
        self.FIELDS = ["name", "Managed By", "Members", "id"]
        self.history_list = list_view.ListView(self.frame, self.HEADINGS, self.FIELDS, self.load_classrooms)

        self.history_list.set_action_button("Delete", self.delete_classroom, True, True)
        self.history_list.set_action_button("Reports", self.view_classroom_report, True, True)
        self.history_list.set_action_button("Assign Challenges", self.assign_typing_challenge, True, True)        
        self.history_list.set_action_button("View/Edit", self.view_classroom, True, True)

        self.history_list.set_action_button("Add", self.add_classroom)


    def view_classroom_report(self):
        classroom = self.history_list.get_focus()
        print(classroom)


    def delete_classroom(self):
        classroom = self.history_list.get_focus()
        print(classroom)
        # TODO: pop up a window confirming delete


    def assign_typing_challenge(self):
        classroom = self.history_list.get_focus()
        print(classroom)


    def add_classroom(self):
        self.add_edit_classroom(None)

    def add_edit_classroom(self, classroom):
        """Creates a classroom window and a classroom form within it.
        For new, classroom should be None
        """
        classroom_window = item_view.ItemView(self.gui)
        title_text = "New Classroom" if not classroom else "Classroom Management: " + classroom["name"]
        classroom_window.set_data(classroom, title_text)

        classroom_form = FormView(classroom_window.frame, self.classroom_management.update_classroom)

        # create a name field
        name_field = EntryBox(
            field_name="name",
            default_data="" if not classroom else classroom["name"],
            label_text="Name")

        # create a search box for the managers of the classroom
        search_admins = EntryBox(
            field_name=None, 
            label_text="Search Admins")
        search_admin_users=lambda text: self.user_management.search_users(text, ["email"], 1)
        search_admins.set_on_change_function(search_admin_users)

        # create a multiselect for managers
        select_admins = MultiSelect(
            field_name="managed_by",
            label_text="Managed By",
            default_data=[] if not classroom else classroom["managed_by"]
        )

        # create a search box for the members of the classroom
        search_standards = EntryBox(
            field_name=None, 
            label_text="Search Students")
        search_standard_users=lambda text: self.user_management.search_users(text, ["email"], 2)
        search_standards.set_on_change_function(search_standard_users)

        # create a multiselect for managers
        select_standards = MultiSelect(
            field_name="members",
            label_text="Members",
            default_data=[] if not classroom else classroom["members"]
        )

        form_inputs = [name_field, search_admins, select_admins, search_standards, select_standards]
        classroom_form.add_form_inputs(form_inputs)

        self.gui.change_window(classroom_window)

    def view_classroom(self):
        classroom = self.history_list.get_focus()
        if classroom:
            self.add_edit_classroom(classroom)


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