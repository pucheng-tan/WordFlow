import tkinter as tk
from tkinter import ttk
from user_interface.components.styles import Styles

class ListView():

    # the number of items to show on a page
    PAGE_LIMIT = 10

    def __init__(self, parent_frame, column_headings, column_data_fields, load_data_function):
        """Creates a table with headings that paginates (has next/prev buttons)

        Args:
            parent_frame: the frame in which to place the table
            column_headings: ordered list of headings to be displayed
            column_data_fields: list of data attributes that match up to those headings
                Additional data fields (such as id) can be added here and not shown
            load_data_function: The function used to call the data
                It's expected to take a limit (int) parameter, and an item parameter,
                that it will use to find the next item on the page (see my_history_window)
                It should take care of formatting the data (ie: dates, any mapping),
                and should return a list of data items
        """
        # initialize variables to parameters
        self.column_headings = column_headings
        self.column_data_fields = column_data_fields
        self.load_data_function = load_data_function
        self.parent_frame = parent_frame

        # start setting up page data
        self.generate_buttons() # load_new_data needs the buttons made first
        self.current_page_data = self.load_new_data()
        self.pages = [self.current_page_data]
        self.current_page = 0 # first page

        # make the gui things      
        
        self.generate_table()
        self.update_table_data()

    def set_action_button(self, button_text, action_function, disabled=False, item_scope=False):
        """Add a button to the frame of buttons.
        Args:
            button_text: the text to display on the button (NO DUPLICATES)
            action_function: function to call when it's clicked
            disabled: whether it should be disabled by default
            item_scope: whether the button performs an action on an individual
                list item, or whether it's scoped to the whole page
        """
        if item_scope:
            self.item_buttons.append(button_text)
            # make the item buttons frame if non existant
            if not hasattr(self, "item_buttons_frame"):
                self.item_buttons_frame = tk.Frame(self.parent_frame)
                self.item_buttons_frame.pack(side=tk.RIGHT, fill=tk.Y)
            frame = self.item_buttons_frame
        else:
            frame = self.buttons_frame

        new_button = tk.Button(frame,
                                text=button_text,
                                fg=Styles.BUTTON_FG,
                                bg=Styles.BUTTON_BG,
                                font=Styles.BUTTON_FONT)
        if disabled:
            new_button["state"] = tk.DISABLED
        new_button["command"] = action_function
        

        new_button.pack(side=tk.RIGHT, padx=Styles.PADX, pady=Styles.PADY)
        self.buttons[button_text] = new_button

        

    def get_focus(self):
        """Returns the item which is currently selected.
        Will return it in exactly the same format it was received in by load_data_function
        """
        iid = self.data_table.focus()
        focus_item = self.current_page_data[int(iid)]
        return focus_item

    def select_list_item(self, event):
        """Enables any item_scope buttons.
        No need to disable them, because you can't completely deselect.
        """
        for item in self.item_buttons:
            self.buttons[item]["state"] = tk.NORMAL

    def generate_buttons(self):
        """ Create the next and previous buttons
        """
        self.buttons = {}
        self.item_buttons = []
        self.buttons_frame = tk.Frame(self.parent_frame)
        self.buttons_frame.pack(side=tk.TOP, fill=tk.X)

        self.set_action_button("Next", self.view_next_page)
        self.set_action_button("Previous", self.view_previous_page, True)

    def generate_table(self):
        """Create the table part of it
        """
        # parent frame for table
        self.table_frame = tk.Frame(self.parent_frame)
        self.table_frame.pack(side=tk.TOP, fill=tk.X, expand=True, padx=Styles.PADX)

        # scroll bar in the table
        self.scroll_bar = tk.Scrollbar(self.table_frame)
        self.scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

        # table itself, and more scrollbar stuff
        self.data_table = ttk.Treeview(self.table_frame, 
                                       yscrollcommand=self.scroll_bar.set, 
                                       selectmode="browse", 
                                       style="Custom.Treeview",
                                       show=["headings"])
        self.scroll_bar.config(command=self.data_table.yview)
        self.data_table.pack(fill=tk.X)

        # make the header row
        self.data_table["columns"] = self.column_headings
        for heading in self.column_headings:
            self.data_table.heading(heading, text=heading, anchor=tk.CENTER)

        # and then style the table
        table_style = ttk.Style()
        table_style.configure("Treeview.Heading", font=Styles.HEADER_FONT)
        table_style.configure("Treeview", font=Styles.DEFAULT_FONT, rowheight=40)
        self.data_table.tag_configure("odd", background=Styles.ALT_ROW_COLOUR)

        self.data_table.bind('<<TreeviewSelect>>', self.select_list_item)


    def update_table_data(self):
        """Changes the data in the table
        """
        # nuke all the current data
        self.data_table.delete(*self.data_table.get_children())

        # then put in data for all of the current page
        self.current_page_data = self.pages[self.current_page]
        
        for i in range(0, len(self.current_page_data)):
            data = self.current_page_data[i]
            values = ([data[field] for field in self.column_data_fields])

            tag = "even" if i % 2 == 0 else "odd"
            self.data_table.insert(parent="", index="end", iid=i, values=values, tags=(tag))


    def view_previous_page(self):
        """Called by clicking the previous button, it'll go to the previous page
        Will enable the "next" button, and disable itself if at first page
        """
        # updates the data to the previous page data, don't pull again
        self.current_page = self.current_page - 1
        # disable the button if applicable, enable next button
        if self.current_page == 0:
            self.buttons["Previous"]["state"] = tk.DISABLED
        self.buttons["Next"]["state"] = tk.NORMAL
        self.update_table_data()

    def view_next_page(self):
        """Called by clicking the next button,
        it'll make the calls to update the data, 
        possibly enable the previous button, and then
        call to update the table data
        """
        # update page number
        self.current_page = self.current_page + 1

        # if we don't have the page data, get it
        if self.current_page > len(self.pages) - 1:
            
            # do the stuff to get the data
            last_item = None
            if self.current_page_data:
                last_item = self.current_page_data[-1]

            new_data = self.load_new_data(last_item)
            self.pages.append(new_data)
        
        # enable the previous button if applicable
        if self.current_page == 1:
            self.buttons["Previous"]["state"] = tk.NORMAL
        self.update_table_data()
        
    def load_new_data(self, last_item=None):
        """Calls the passed in load data function to get more data.
        Checks it for errors, and that it exists.
        
        Args:
            last_item: the last item on the current page to be compared for the next page
        """
        # get the data
        data_items = self.load_data_function(ListView.PAGE_LIMIT, last_item)
        # and then check that it's all good
        if "error" not in data_items:
            self.check_if_out_of_data(data_items)
            return data_items
        else:
            self.display_error(data_items["error"])
            return []

    def check_if_out_of_data(self, results):
        """Checks if we're out of data and if the next button should be disabled.
        If the most recent page is the final page, but it's exactly the page limit,
        it won't be caught until the next button is clicked again
        """
        if len(results) < self.PAGE_LIMIT:
            # disable the next button
            self.buttons["Next"]["state"] = tk.DISABLED

    def display_error(self, error_message):
        # TODO: this should be actually displayed on the page
        print(error_message)