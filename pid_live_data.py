import tkinter as tk
from matplotlib import pyplot as plt
import obd


def live_data_screen():
    root = tk.Tk()
    connection = obd.OBD()
    root.configure(bg="#333333")
    # Set the window title
    root.title("Live Data")
    # Set the window size
    root.geometry("1080x600")
    root.eval('tk::PlaceWindow . center')
    main_title = tk.Label(root,
                          text="Live Data",
                          fg="white",
                          bg="#333333",
                          font=("Ariel", 38, "bold"))
    main_title.pack(pady=(30, 10))
