import dictionaries
import customtkinter as ctk
import customtkinter
from PIL import Image

window = ctk.CTk()
window.title("Unit Converter")
window.iconbitmap("app_icon.ico")
window.geometry("540x300")
window.resizable(False, False)
ctk.set_appearance_mode("dark")

#define constants for the buttons
BUTTON_FG_COLOR = ("black", "#1F6AA5")
BUTTON_HOVER_COLOR = ("darkgrey", "#144870")
BUTTON_FONT = customtkinter.CTkFont(family = "Arial", size = 11, weight = "bold")
BUTTON_WIDTH = 1

def convert(s:str):
    value = entry_double.get()
    input_unit = select_input.get()
    output_unit = select_output.get()
    if s != "t":
        try:
            conversion_factor = getattr(dictionaries, s + "_conversion_factors")[input_unit][output_unit]
            result = conversion_factor * value
        except KeyError:
            result = "0"
    else:
        if input_unit == output_unit:
            result = value
        else:
            result = dictionaries.t_conversion_factors[input_unit][output_unit](value)
    output_box_text.set(result)

def box_reset():
    output_box_text.set("")
    entry_double.set(0)

def show_widgets(s: str, conversion_factors:dict, title:str, values:str):
    box_reset()
    convert_button.configure(command = lambda: convert(s))
    select_output.configure(values = conversion_factors)
    select_output.set(value = values[0])
    select_input.configure(values = conversion_factors)
    select_input.set(value = values[0])
    Label.configure(text = title)
    input_box.configure(validate = "key")
    input_box.configure(validatecommand = (
        input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))

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
#disabling the entry so that the user cant input anything in it
output_box.configure(state = "disabled")
output_box.place(x = 360, y = 150)

#this is where the user is supposed to write his unit he wants converted
entry_double = ctk.DoubleVar()
input_box = ctk.CTkEntry(window, 
                         width = 130, 
                         font = ("Arial", 14),  
                         textvariable = entry_double)
#set the input type to number only
input_box.configure(validate = "key")
input_box.configure(validatecommand = (input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.place(x = 175, y = 150)

# this is the sidebar where the user can choose the conversion type
sidebar = ctk.CTkFrame(window, fg_color = ("lightgrey","black"), corner_radius = 0)
for x in range(7):
    sidebar.rowconfigure(x, weight = 1)

categories = [
    ("Temperature", lambda: show_widgets("t", dictionaries.t_conversion_factors, "Temperature", dictionaries.t_values)),
    ("Length", lambda: show_widgets("l", dictionaries.l_conversion_factors, "Length", dictionaries.l_values)),
    ("Area", lambda: show_widgets("a", dictionaries.a_conversion_factors, "Area", dictionaries.a_values)),
    ("Volume", lambda: show_widgets("v", dictionaries.v_conversion_factors, "Volume", dictionaries.v_values)),
    ("Mass", lambda: show_widgets("m", dictionaries.m_conversion_factors, "Mass", dictionaries.m_values)),
    ("Time", lambda: show_widgets("ti", dictionaries.ti_conversion_factors, "Time", dictionaries.ti_values)),
    ("Pressure", lambda: show_widgets("p", dictionaries.p_conversion_factors, "Pressure", dictionaries.p_values))
]

for row, (label, command) in enumerate(categories):
    button = ctk.CTkButton(sidebar,
                           text = label,
                           font = customtkinter.CTkFont(family="Arial", size=16, weight="bold"),
                           command = command,
                           fg_color = BUTTON_FG_COLOR,
                           hover_color = BUTTON_HOVER_COLOR)
    button.grid(row = row, column = 0, padx = 10, pady = 10, sticky = "ew")

sidebar.pack(side = "left", fill = "y")

#label telling the user what type of conversion he is doing
Label = ctk.CTkLabel(window, 
                       text = "Temperature", 
                       font = customtkinter.CTkFont(family = "Arial", size = 26, weight = "bold"), 
                       text_color = ("black", "white"), 
                       bg_color = ("lightgrey", "black"))
Label.pack(fill = "both", ipady = 3)

#copy to clipboard button
copy_button = customtkinter.CTkButton(window, 
                                      text = "copy", 
                                      font = BUTTON_FONT, 
                                      width = BUTTON_WIDTH, 
                                      command = copy_to_clipboard, 
                                      fg_color = BUTTON_FG_COLOR, 
                                      hover_color = BUTTON_HOVER_COLOR)
copy_button.place(x = 495, y = 150)

#theme button
theme = ctk.StringVar(value = ctk.get_appearance_mode())
theme_button = ctk.CTkButton(window, 
                             textvariable = theme, 
                             command = change_theme, 
                             width = BUTTON_WIDTH, 
                             font = BUTTON_FONT, 
                             fg_color = BUTTON_FG_COLOR, 
                             hover_color = BUTTON_HOVER_COLOR)
theme_button.place(x = 495, y = 195)

#input dropdown menu
select_input = customtkinter.CTkOptionMenu(window,
                                            values = ["Celsius [°C]", 
                                                    "Fahrenheit [°F]", 
                                                    "kelvin [K]"],
                                            width = 130,
                                            text_color = "white",
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
                                            text_color = "white",
                                            fg_color = ("black", "#1F6AA5"),
                                            button_color = ("black","#144870"),
                                            button_hover_color = ("darkgrey", "#144870"))
select_output.place(x = 360, y = 105)

#convert button
convert_button_image = customtkinter.CTkImage(Image.open("convert.png"), size = (20, 20))
convert_button = ctk.CTkButton(window, 
                                text = "",
                                image = convert_button_image,
                                command = lambda: convert("t"),
                                width = 21,
                                height = 21,
                                fg_color = BUTTON_FG_COLOR,
                                hover_color = BUTTON_HOVER_COLOR)
convert_button.place(x = 315, y = 150)

window.mainloop()