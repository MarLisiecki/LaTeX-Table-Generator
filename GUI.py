__name__ = "LaTeX table generator from CSV"
__author__ = "Marcin Lisiecki"
__license__ = "Open-source"
__version__ = "1.0"
__status__ = "production"

import tkinter as tk
import tkinter.filedialog
from LaTeX_table_automation import combine_functions

# Variables

path_to_file = ""
geometry_size = "800x600"


# Window configuration 

window = tk.Tk()
window.title("LaTeX table generator")
window.configure(background="#c2c2c2")
window.geometry(geometry_size)
window.resizable(0, 0)

enter_of_path = tk.Entry(window, font=40, width=60)
enter_of_path.pack(side=tk.LEFT)
enter_of_path.pack(side=tk.TOP)
enter_of_path.pack(padx=10, pady=10)
second_button.pack(side=tk.RIGHT)
second_button.pack(side=tk.BOTTOM)
text_box = tk.Text(window)
text_box.pack(side=tk.BOTTOM)
text_box.pack(expand=True)
first_button.pack(side=tk.RIGHT)
first_button.pack(side=tk.TOP)

# Button with handlers

first_button = tk.Button(
    window,
    text="Path to file",
    font=40,
    command=lambda: [path_to_file == browsefunc()],
)


second_button = tk.Button(
    window,
    text="Generate",
    font=40,
    command=lambda: [path_to_file == print_syntax_of_table()],
)

# Functions for GUI which call LaTeX_table_automation

def browsefunc():
    filename = tkinter.filedialog.askopenfilename(
        filetypes=(("CSV files", "*.csv"), ("All files", "*.*"))
    )
    enter_of_path.insert(tk.END, filename)
    path = enter_of_path.get()
    path = path.replace("/", "\\")
    global path_to_file
    path_to_file = path


def print_syntax_of_table():
    syntax = combine_functions(path_to_file)
    text_box.insert(tk.END, syntax)
    print(syntax)


window.mainloop()
