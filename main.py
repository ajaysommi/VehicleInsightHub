import pandas as py
import tkinter as tk
from pid_live_data import *


def main():
    # Use a breakpoint in the code line below to debug your script.
    root = tk.Tk()
    root.configure(bg="#333333")
    # Set the window title
    root.title("Vehicle Insight Hub")
    # Set the window size
    root.geometry("890x350")
    root.eval('tk::PlaceWindow . center')
    main_title = tk.Label(root,
                          text="Welcome to Your Vehicle Insight Hub!",
                          fg="white",
                          bg="#333333",
                          font=("Ariel", 38, "bold"))
    main_title.pack(pady=(30, 10))

    sub_title = tk.Label(root,
                         text="Vehicle Insight Hub provides real-time monitoring, "
                              "diagnostic trouble code analysis, \n"
                              "and in-depth performance insights "
                              "to help you maintain your vehicle's health \nand optimize its performance.",
                         fg="white",
                         bg="#333333",
                         font=("Ariel", 15)
                         )
    sub_title.pack(pady=(0, 0))

    diag_button = tk.Button(root, text="Trouble Codes and Diagnostics", highlightbackground="#FFA500",
                            font=("Ariel", 15, "bold"))
    diag_button.config(height=5, width=30)
    diag_button.pack(side="right", padx=5, pady=5, expand=True)

    live_data_button = tk.Button(root, text="View Live Data", highlightbackground="#00FF00",
                                 font=("Ariel", 15, "bold"), command=live_data_screen)
    live_data_button.config(height=5, width=30)
    live_data_button.pack(side="left", padx=5, pady=5, expand=True)

    # Run the application
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
