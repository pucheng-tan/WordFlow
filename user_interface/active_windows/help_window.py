import tkinter as tk
from user_interface.active_windows import active_window


class HelpWindow(active_window.ActiveWindow):
    def __init__(self, gui):
        active_window.ActiveWindow.__init__(self, gui)

        self.display_help_information()

        if self.privilege < 2:
            self.add_admin_help_information()
        if self.privilege == 0:
            self.add_super_admin_help_information()

        self.help_text.configure(state="disabled")

    def display_help_information(self):
        heading_label = tk.Label(self.frame, text="Welcome to Word Flow!")
        heading_label["font"] = ("Helvetica", 20, "bold")
        heading_label.pack()

        help_scroll_bar = tk.Scrollbar(self.frame)
        self.help_text = tk.Text(self.frame)
        help_scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
        self.help_text.pack(side=tk.LEFT, fill=tk.BOTH)
        help_scroll_bar.config(command=self.help_text.yview)
        self.help_text.config(yscrollcommand=help_scroll_bar.set)
        help_information = """
        Word Flow is a typing tool that helps users improve their typing speed.
        The target users are any computer users that wish to improve their
        speed. We want to make tests that fit different types of users,
        including programmers, professional typists, TBD. The user is given text
        to type, and metrics are recorded and displayed at the end of the test.
        We hope to develop different types of metrics that can help users track
        their improvement!
        
        Types of typing challenges:
        Standard Mode
        Consists of English words, spaces, and punctuation.
        Programming Mode
        The user types code including special characters.
        Dictation Mode
        Audio is played back over the device's speakers. There is no
        punctuation.
        
        Taking a typing challenge:
        1. Click New Challenge in the main menu.
        2. Select a mode and a time.
        3. Click Start.
        
        Changing your profile information:
        1. Click My Profile in the main menu.
        2. Select a feature to change from the drop down menu and click the
        button.
        3. Enter in the new information.
        4. Click My Profile again to see the change.
        """
        self.help_text.insert(tk.END, help_information)
        self.help_text.configure(font=("Helvetica", 15))

        email_label = tk.Label(
            self.frame,
            text="If you have any issues, email us at group2@gmail.com!")
        email_label["font"] = ("Helvetica", 15)
        email_label.pack(anchor=tk.S)

    # def show(self):
    #     self.frame.pack(fill=tk.BOTH)

    def add_admin_help_information(self):
        """Adds help information for admin users to text box or the help window.
        """
        help_information = """
        Creating a Classroom
        1. Click Classroom Management in the main menu. 
        2. Click the Add button.
        3. Fill the information required for creating a new Classroom.
        4. Click the Submit button.
        """
        self.help_text.insert(tk.END, help_information)

    def add_super_admin_help_information(self):
        """Adds help information for super admin users to text box for the help
        window.
        """
        help_information = """
        Types of Users:
        There are three of types of users.
        Standard Users
        Standard users are equivalent to students. They can take challenges.
        Admin Users
        Admin users are equivalent to teachers. They can do everything standard
        users can do and manage classrooms.
        Super-Admin Users
        Super-admin users are equivalent to principals or IT staff. They can do
        everything that admin users can do and manage users in the school.
        
        Adding New Users to the School:
        1. Click User Management in the main menu.
        2. Click New User.
        3. Enter their email address.
        4. Pick a privilege level.
        5. Click enter. A verification email will be sent to them.
        6. Once they have verified their email, they can sign up and then log
        in.
        
        Changing Privilege Level of Users:
        1. Click User Management in the main menu.
        2. Select a user in the table.
        3. Pick a privilege level in the drop down menu.
        4. Click the button "Change Privilege".
        Note: The privilege level of super-admin users cannot be changed.
        """

        self.help_text.insert(tk.END, help_information)
