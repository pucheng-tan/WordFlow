import tkinter as tk
from user_interface.components.styles import Styles

class FormView():

    def __init__(self, parent_frame, on_submit_function, submit_label="Submit"):
        # make a frame for the form
        self.form_frame = tk.Frame(parent_frame)
        self.form_frame.pack(side=tk.TOP, fill=tk.X)
        self.on_submit_function = on_submit_function
        

        # and then add a submit button
        submit = tk.Button(self.form_frame,
                            text=submit_label,
                            fg=Styles.BUTTON_FG,
                            bg=Styles.BUTTON_BG,
                            font=Styles.BUTTON_FONT)
        submit.pack(side=tk.BOTTOM, padx=Styles.PADX, pady=Styles.PADY)
        submit["command"] = self.submit

        # get ready to add data
        self.inputs = []

    def add_form_inputs(self, form_inputs):
        self.inputs += form_inputs

        for item in form_inputs:
            form_input = item.render(self.form_frame)
            form_input.pack(side=tk.TOP, padx=Styles.PADX, pady=Styles.PADY)

    def submit(self):
        data = {}
        for field_input in self.inputs:
            field_name = field_input.field_name
            if field_name:
                data[field_name] = field_input.get()

        print(data)

        response = self.on_submit_function(data)
        if "error" in response:
            self.display_error(error)
        else:
            message = " created" if "id" not in response else " updated"
            self.display_success(message)

    def display_success(self, message):
        print(message)

    def display_error(self, error):
        print(error)



class FormInput():
    """A base class for all form input elements
    """

    def __init__(self, field_name, label_text="", required=False, default_data=None):  
        """
        Args:
            field_name: the name of the field as corresponds to the data
                use None if input doesn't directly correspond to data.
            label_text: set to a string to auto create a label
            required: set to true if should be required
            default_data: what to initialize the input's data as
        """          
        self.field_name = field_name
        self.label_text = label_text
        self.required = required
        self.data = tk.StringVar(value=default_data)
        

    def render(self, parent):
        """Inserts the element into a frame,
        creates a label if applicable, and returns the frame.
        Subclasses should insert any other things in this method.
        """
        self.item_frame = tk.Frame(parent)
        if self.label_text:
            label = tk.Label(self.item_frame, text=self.label_text)
            label.pack(side=tk.TOP, fill=tk.X)
        return self.item_frame

    def get(self):
        return self.data.get()

class EntryBox(FormInput):
    """An expansion of the tk Entry. Will auto-create a label if label text given.
    User set_on_change_function to set a function to be called whenever
    the text is changed.
    """
    def __init__(self, field_name, label_text, required=False, default_data=None):
        super().__init__(field_name, label_text, required, default_data)

    def set_on_change_function(self, function):
        self.on_change_function = function
        self.data.trace_add("write", self.callback)

    def callback(self, name, index, mode):
        response = self.on_change_function(self.data.get())
        print(response)
        return True

    def render(self, parent):
        item_frame = super().render(parent)
        self.control = tk.Entry(item_frame, textvariable=self.data)
        self.control.pack(side=tk.LEFT, fill=tk.X)
        return item_frame

class MultiSelect(FormInput):

    def __init__(self, field_name, label_text, required=False, default_data=None):
        super().__init__(field_name, label_text, required, default_data)
        self.data = [] if not default_data else default_data

    def set_values(self, values):
        """WARNING. DO NOT CALL BEFORE RENDERING
        """
        self.control.delete(0, tk.END)
        self.control.insert(tk.END, values)

    def render(self, parent):
        item_frame = super().render(parent)
        self.control = tk.Listbox(item_frame, selectmode="multiple")
        self.control.pack(side=tk.LEFT, fill=tk.X)
        self.set_values(self.data)
        return item_frame

    def get(self):
        return self.control.get(tk.ACTIVE)