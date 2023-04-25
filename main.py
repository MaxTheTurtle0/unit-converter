import dictionaries
import tkinter as tk
import customtkinter as ctk
import customtkinter
from PIL import Image

my_image = customtkinter.CTkImage(light_image = Image.open("convert.png"),
                                  dark_image = Image.open("convert.png"),
                                  size = (20, 20))
window = ctk.CTk()
window.title("Unit Converter")
window.iconbitmap("app_icon.ico")
window.geometry("540x300")
window.resizable(False, False)
ctk.set_appearance_mode("dark")

def convert(s:str):
    value = entry_double.get()
    input_unit = select_input.get()
    output_unit = select_output.get()
    if s == "t":
        if input_unit == output_unit:
            result = value
        else:
            result = dictionaries.t_conversion_factors[input_unit][output_unit](value)
    elif s == "l":
        result = dictionaries.l_conversion_factors[input_unit][output_unit] * value
    elif s == "a":
        result = dictionaries.a_conversion_factors[input_unit][output_unit] * value
    elif s == "v":
        result = dictionaries.v_conversion_factors[input_unit][output_unit] * value
    elif s == "m":
        result = dictionaries.m_conversion_factors[input_unit][output_unit] * value
    else:
        result = "0"
    output_box_text.set(result)

def box_reset():
    output_box_text.set("")
    entry_double.set(0)

#these functions are used to show the correct widgets for each conversion type
def show_length_widgets():
    box_reset()
    convert_button.configure(command = lambda: convert("l"))
    select_output.configure(values = dictionaries.l_values)
    select_output.set(value = dictionaries.l_values[0])
    select_input.configure(values = dictionaries.l_values)
    select_input.set(value = dictionaries.l_values[0])
    Label.configure(text = "Length")
    input_box.configure(validate="key")
    input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))

def show_temperature_widgets():
    box_reset()
    convert_button.configure(command = lambda: convert("t"))
    select_output.configure(values = dictionaries.t_values)
    select_output.set(value = dictionaries.t_values[0])
    select_input.configure(values = dictionaries.t_values)
    select_input.set(value = dictionaries.t_values[0])
    Label.configure(text = "Temperature")
    input_box.configure(validate="key")
    input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))

def show_area_widgets():
    box_reset()
    convert_button.configure(command = lambda: convert("a"))
    select_output.configure(values = dictionaries.a_values)
    select_output.set(value = dictionaries.a_values[0])
    select_input.configure(values = dictionaries.a_values)
    select_input.set(value = dictionaries.a_values[0])
    Label.configure(text = "Area")
    input_box.configure(validate="key")
    input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))

def show_volume_widgets():
    box_reset()
    convert_button.configure(command = lambda: convert("v"))
    select_output.configure(values = dictionaries.v_values)
    select_output.set(value = dictionaries.v_values[0])
    select_input.configure(values = dictionaries.v_values)
    select_input.set(value = dictionaries.v_values[0])
    Label.configure(text = "Volume")
    input_box.configure(validate="key")
    input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))

def show_mass_widgets():
    box_reset()
    convert_button.configure(command = lambda: convert("m"))
    select_output.configure(values = dictionaries.m_values)
    select_output.set(value = dictionaries.m_values[0])
    select_input.configure(values = dictionaries.m_values)
    select_input.set(value = dictionaries.m_values[0])
    Label.configure(text = "Mass")
    input_box.configure(validate="key")
    input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))

#this is the function for the button that will copy the result to the clipboard
def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(output_box_text.get())

#this is the function for the button that will change the theme of the app
def change_theme():
    current_theme = ctk.get_appearance_mode()
    if current_theme == "Dark":
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")
    theme.set(ctk.get_appearance_mode())

#this is where the user can see the result of the conversion
output_box_text = ctk.StringVar()
output_box = ctk.CTkEntry(window, 
                          width = 130, 
                          font = ("Arial", 14),
                         textvariable = output_box_text)
#disabling the Entry so that the user cant input anything in it
output_box.configure(state ="disabled")
output_box.place(x = 360, y = 150)

#this is where the user is supposed to write his unit he wants converted
entry_double = tk.DoubleVar()
input_box = ctk.CTkEntry(window, 
                         width = 130, 
                         font = ("Arial", 14),  
                         textvariable = entry_double)
#set the input type to number only
input_box.configure(validate="key")
input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.place(x=175, y=150)


# this is the sidebar where the user can choose the conversion type
sidebar = ctk.CTkFrame(window, fg_color = ("lightgrey","black"), corner_radius=0)
sidebar.rowconfigure(0, weight = 1)
sidebar.rowconfigure(1, weight = 1)
sidebar.rowconfigure(2, weight = 1)
sidebar.rowconfigure(3, weight = 1)
sidebar.rowconfigure(4, weight = 1)
sidebar.columnconfigure(0, weight = 1)
sidebar.pack(side="left", fill = "y")

Label = ctk.CTkLabel(window, 
                       text = "Temperature", 
                       font = customtkinter.CTkFont(family = "Arial", size = 26, weight = "bold"), 
                       text_color = ("black", "white"), 
                       bg_color = ("lightgrey", "black"))
Label.pack(fill = "both")

#Temperature
#This is where all the widgets regarding the Temperature section are

t_button = ctk.CTkButton(sidebar, 
                         text = "Temperature", 
                         font = customtkinter.CTkFont(family = "Arial", size = 16, weight="bold"), 
                         command = show_temperature_widgets, 
                         text_color="white", 
                         fg_color = ("black", "#1F6AA5"), 
                         hover_color=("darkgrey", "#144870"))
t_button.grid(row = 0, column = 0, padx = 10, pady = 10, sticky = "ew")


#Length
#This is where all the widgets regarding the Length section are

l_button = ctk.CTkButton(sidebar, 
                         text = 
                         "Length", 
                         font = customtkinter.CTkFont(family = "Arial", size = 16, weight="bold"), 
                         command = show_length_widgets, 
                         text_color="white", 
                         fg_color = ("black", "#1F6AA5"), 
                         hover_color=("darkgrey", "#144870"))
l_button.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "ew")

#Area
#This is where all the widgets regarding the Area section are

a_button = ctk.CTkButton(sidebar, 
                         text = "Area", 
                         font = customtkinter.CTkFont(family = "Arial", size = 16, weight="bold"), 
                         command = show_area_widgets, 
                         text_color="white", 
                         fg_color = ("black", "#1F6AA5"), 
                         hover_color=("darkgrey", "#144870"))
a_button.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "ew")


#Volume
#This is where all the widgets regarding the Volume section are

v_button = ctk.CTkButton(sidebar, 
                         text = "Volume", 
                         font = customtkinter.CTkFont(family = "Arial", size = 16, weight="bold"), 
                         command = show_volume_widgets, 
                         text_color="white", 
                         fg_color = ("black", "#1F6AA5"), 
                         hover_color=("darkgrey", "#144870"))
v_button.grid(row = 3, column = 0, padx = 10, pady = 10, sticky = "ew")

#Mass
#This is where all the widgets regarding the Mass section are

m_button = ctk.CTkButton(sidebar,
                        text = "Mass",
                        font = customtkinter.CTkFont(family = "Arial", size = 16, weight="bold"),
                        command = show_mass_widgets,
                        text_color="white",
                        fg_color = ("black", "#1F6AA5"),
                        hover_color=("darkgrey", "#144870"))
m_button.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "ew")

#copy to clipboard button
copy_button = customtkinter.CTkButton(window, 
                                      text = "copy", 
                                      font = customtkinter.CTkFont(family = "Arial", size = 11, weight="bold"), 
                                      width = 1, 
                                      command = copy_to_clipboard, 
                                      text_color="white",  
                                      fg_color = ("black", "#1F6AA5"), 
                                      hover_color=("darkgrey", "#144870"))
copy_button.place(x = 495, y = 150)

#theme button
theme = tk.StringVar(value = ctk.get_appearance_mode())
theme_button = ctk.CTkButton(window, 
                             textvariable = theme, 
                             command = change_theme, 
                             width = 1, 
                             font = customtkinter.CTkFont(family = "Arial", size = 11, weight="bold"), 
                             text_color="white", 
                             fg_color = ("black", "#1F6AA5"), 
                             hover_color=("darkgrey", "#144870"))
theme_button.place(x = 495, y = 195)

#input dropdown menu
select_input = customtkinter.CTkOptionMenu(window,
                                            values = ["Celsius [°C]", 
                                                    "Fahrenheit [°F]", 
                                                    "kelvin [K]"],
                                            width = 130,
                                            text_color="white",
                                            fg_color = ("black", "#1F6AA5"),
                                            button_color = ("black","#144870"),
                                            button_hover_color = ("darkgrey", "#144870"))
select_input.place(x = 175, y = 105)

#output dropdown menu
select_output = customtkinter.CTkOptionMenu(window,
                                            values = ["Celsius [°C]", 
                                                    "Fahrenheit [°F]", 
                                                    "kelvin [K]"],
                                            width = 130,
                                            text_color="white",
                                            fg_color = ("black", "#1F6AA5"),
                                            button_color = ("black","#144870"),
                                            button_hover_color = ("darkgrey", "#144870"))
select_output.place(x = 360, y = 105)

convert_button = ctk.CTkButton(window, text = "",
                                image = my_image,
                                font = customtkinter.CTkFont(family = "Arial", size = 16, weight="bold"),
                                command = lambda: convert("t"),
                                text_color="white",
                                width=21,
                                height=21,
                                fg_color = ("black", "#1F6AA5"),
                                hover_color=("darkgrey", "#144870"))
convert_button.place(x = 315, y = 150)

window.mainloop()