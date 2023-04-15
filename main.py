import tkinter as tk
import customtkinter as ctk

window = ctk.CTk()
window.title("Unit Converter")
window.geometry("500x300")
ctk.set_appearance_mode("dark")
#this is so that the user knows what unit he is converting
T = ctk.CTkLabel(window, text="Temperature", font=("Arial", 24), text_color="white", bg_color="black")
T.pack(fill="both")

#this is where the user can see the result of the conversion
output_box = tk.Text(window, width="12", height="1", font=("Arial", 14))
output_box.configure(state="disabled")
output_box.pack(side="right", padx="20", pady="20")

#this is where the user is supposed to write his unit he wants converted
input_box = tk.Entry(window, width=12, font=("Arial", 14))
# set the input type to a number
input_box.config(validate="key")
input_box.config(validatecommand=(input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.pack(side="right", padx="20", pady="20")

#this button frame is where all the buttons are which are used for manoeuvring through the app
sidebar = tk.Frame(window, background="black")
sidebar.rowconfigure(0, weight=1)
sidebar.rowconfigure(1, weight=1)
sidebar.rowconfigure(2, weight=1)
sidebar.rowconfigure(3, weight=1)
sidebar.columnconfigure(0, weight=1)

#these buttons changing to the unit which you want to convert(Temperature, Length, Area, Volume)
T_button = ctk.CTkButton(sidebar, text="Temperature", font=("Arial", 16))
T_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")


L_button = ctk.CTkButton(sidebar, text="Length", font=("Arial", 16))
L_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

A_button = ctk.CTkButton(sidebar, text="Area", font=("Arial", 16))
A_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

V_button = ctk.CTkButton(sidebar, text="Volume", font=("Arial", 16))
V_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

sidebar.pack(side="left", fill="y")

window.mainloop()   