import tkinter as tk
import customtkinter as ctk
import customtkinter

window = ctk.CTk()
window.title("Unit Converter")
window.geometry("500x300")
window.resizable(False, False)

def T_convert():
    input_unit = T_select_input.get()
    output_unit = T_select_output.get()
    value = entryInt.get()

    if input_unit == "Celsius [°C]" and output_unit == "Fahrenheit [°F]":
        result = value * 1.8 + 32
    elif input_unit == "Fahrenheit [°F]" and output_unit == "Celsius [°C]":
        result = (value - 32) / 1.8
    elif input_unit == "kelvin [K]" and output_unit == "Celsius [°C]":
        result = value - 273.15
    elif input_unit == "Celsius [°C]" and output_unit == "kelvin [K]":
        result = value + 273.15
    elif input_unit == "Fahrenheit [°F]" and output_unit == "kelvin [K]":
        result = (value + 459.67) * 5/9
    elif input_unit == "kelvin [K]" and output_unit == "Fahrenheit [°F]":
        result = value * 9/5 - 459.67
    else:
        result = value
    
    output_box_text.set(result)

ctk.set_appearance_mode("dark")
#this is so that the user knows what unit he is converting
Label = ctk.CTkLabel(window, text="Temperature", font=("Arial", 26), text_color="white", bg_color="black")
Label.pack(fill="both")

#this is where the user can see the result of the conversion
output_box_text = ctk.StringVar()
output_box = ctk.CTkEntry(window, width=130, font=("Arial", 14), textvariable=output_box_text)
output_box.configure(state="disabled")
output_box.place(x=360, y=150)

#this is where the user is supposed to write his unit he wants converted
entryInt = tk.IntVar()
input_box = ctk.CTkEntry(window, width=130, font=("Arial", 14),  textvariable = entryInt)
# set the input type to a number
input_box.configure(validate="key")
input_box.configure(validatecommand=(input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.place(x=175, y=150)

T_convert_button = ctk.CTkButton(window, text="Convert", font=("Arial", 16), command=T_convert)
T_convert_button.place(x=262, y=195)

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

T_select_input = customtkinter.CTkOptionMenu(window, values=["Celsius [°C]", 
                                                             "Fahrenheit [°F]", 
                                                             "kelvin [K]"], width=130)
T_select_input.place(x=175, y=105)
T_select_output = customtkinter.CTkOptionMenu(window, values=["Celsius [°C]", 
                                                              "Fahrenheit [°F]", 
                                                              "kelvin [K]"], width=130)
T_select_output.place(x=360, y=105)

L_select_input = customtkinter.CTkOptionMenu(window, values=["centimeter [cm]", 
                                                             "decimeter [dm]", 
                                                             "meter [m]", 
                                                             "kilometer [km]", 
                                                             "inch [in]", 
                                                             "foot [ft]", 
                                                             "yard [yd]", 
                                                             "mile [mi]"], width=130)
L_select_output = customtkinter.CTkOptionMenu(window, values=["centimeter [cm]", 
                                                              "decimeter", 
                                                              "meter [m]", 
                                                              "kilometer [km]", 
                                                              "inch [in]", 
                                                              "foot [ft]", 
                                                              "yard [yd]", 
                                                              "mile [mi]"], width=130)

A_select_input = customtkinter.CTkOptionMenu(window, values=["square centimeter [cm²]", 
                                                             "square decimetre [dm²]", 
                                                             "square meter [m²]", 
                                                             "square decametre [dam²]",
                                                             "square hectometre [hm²]", 
                                                             "square kilometer [km²]", 
                                                             "square inch [in²]", 
                                                             "square foot [ft²]", 
                                                             "square yard [yd²]", 
                                                             "square mile [mi²]",
                                                             "acre"], width=130)
A_select_output = customtkinter.CTkOptionMenu(window, values=["square centimeter [cm²]", 
                                                             "square decimetre [dm²]", 
                                                             "square meter [m²]", 
                                                             "square decametre [dam²]",
                                                             "square hectometre [hm²]", 
                                                             "square kilometer [km²]", 
                                                             "square inch [in²]", 
                                                             "square foot [ft²]", 
                                                             "square yard [yd²]", 
                                                             "square mile [mi²]",
                                                             "acre"], width=130)

#going to do this tmr V_select_input = customtkinter.CTkOptionMenu(window, values=["Celsius [°C]", "Fahrenheit [°F]", "kelvin [K]"], width=130)
#going to do this tmr V_select_output = customtkinter.CTkOptionMenu(window, values=["Celsius [°C]", "Fahrenheit [°F]", "kelvin [K]"], width=130)


L_button = ctk.CTkButton(sidebar, text="Length", font=("Arial", 16))
L_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

A_button = ctk.CTkButton(sidebar, text="Area", font=("Arial", 16))
A_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

V_button = ctk.CTkButton(sidebar, text="Volume", font=("Arial", 16))
V_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

sidebar.pack(side="left", fill="y")

window.mainloop()