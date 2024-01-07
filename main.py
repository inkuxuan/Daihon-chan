import tkinter as tk
from tkinter import messagebox, scrolledtext

import config_handler
import log_utils
import osc_handlers


class TextEditor:
    def __init__(self, root, message_handler):
        self.root = root
        self.message_handler = message_handler

        self.root.title("Daihon-Chan VRChatbox Editor")

        # Define the text field with scroll bar
        self.text_field = scrolledtext.ScrolledText(root, wrap=tk.WORD, undo=True, font=('Arial', 12))
        self.text_field.pack(expand=True, fill='both', padx=10, pady=10)
        self.text_field.focus_set()

        # Bindings for text resizing and hotkeys
        root.bind("<Control-MouseWheel>", self.change_text_size)
        root.bind("<Shift-Return>", self.send_previous_line)
        root.bind("<Control-s>", self.send_current_line)
        root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Set the default background for all lines
        self.default_bg = self.text_field.cget("background")
        # Update the current line background
        self.update_line_highlight()

    def update_line_highlight(self):
        # Remove highlight from all lines
        self.text_field.tag_remove("highlight", 1.0, "end")
        # Get current line
        current_line = self.text_field.index("insert").split(".")[0]
        # Highlight current line
        self.text_field.tag_add("highlight", f"{current_line}.0", f"{current_line}.end")
        self.text_field.tag_config("highlight", background="light green")
        # Call this method again whenever the cursor moves
        self.text_field.after(1, self.update_line_highlight)

    def change_text_size(self, event=None):
        # Get current font size and increase or decrease based on mouse wheel movement
        size = int(self.text_field.cget("font").split()[-1])
        new_size = size + (1 if event.delta > 0 else -1)
        self.text_field.configure(font=('Arial', new_size))

    def send_previous_line(self, event=None):
        self.send_current_line(event=event, previous_line=True)

    def send_current_line(self, event=None, previous_line=False):
        # Get current line text
        current_line_index = self.text_field.index("insert").split('.')[0]
        if previous_line:
            current_line_index = int(current_line_index) - 1
        line_text = self.text_field.get(f"{current_line_index}.0", f"{current_line_index}.end")
        self.message_handler.send_message(line_text)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit? \n"
                                          "Text will not be saved. \n"
                                          "Please copy and save on your own."):
            self.root.destroy()


def main():
    log_utils.setup_logger()
    config = config_handler.retrieve_config()
    osc = osc_handlers.VrcOscHandler(config)
    root = tk.Tk()
    app = TextEditor(root, osc)
    app.root.mainloop()


# Create root window and pass it to the application
if __name__ == "__main__":
    main()
