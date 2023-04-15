import tkinter as tk
import customtkinter as ctk
import customtkinter

window = ctk.CTk()
window.title("Unit Converter")
window.geometry("500x300")
window.resizable(False, False)

ctk.set_appearance_mode("dark")
#this is so that the user knows what unit he is converting
T = ctk.CTkLabel(window, text="Temperature", font=("Arial", 26), text_color="white", bg_color="black")
T.pack(fill="both")

#this is where the user can see the result of the conversion
output_box = ctk.CTkEntry(window, width=130, font=("Arial", 14))
output_box.configure(state="disabled")
output_box.place(x=360, y=150)

#this is where the user is supposed to write his unit he wants converted
input_box = ctk.CTkEntry(window, width=130, font=("Arial", 14))
# set the input type to a number
input_box.configure(validate="key")
input_box.configure(validatecommand=(input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.place(x=175, y=150)

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

T_select_input = customtkinter.CTkOptionMenu(master=window, values=["Celsius [°C]", "Fahrenheit [°F]", "kelvin [K]"], width=130)
T_select_input.place(x=175, y=105)
T_select_output = customtkinter.CTkOptionMenu(master=window, values=["Celsius [°C]", "Fahrenheit [°F]", "kelvin [K]"], width=130)
T_select_output.place(x=360, y=105)

L_button = ctk.CTkButton(sidebar, text="Length", font=("Arial", 16))
L_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

A_button = ctk.CTkButton(sidebar, text="Area", font=("Arial", 16))
A_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

V_button = ctk.CTkButton(sidebar, text="Volume", font=("Arial", 16))
V_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

sidebar.pack(side="left", fill="y")

window.mainloop()   