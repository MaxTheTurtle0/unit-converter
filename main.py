import tkinter as tk
import customtkinter as ctk
import customtkinter

window = ctk.CTk()
window.title("Unit Converter")
window.geometry("540x300")
window.resizable(False, False)
ctk.set_appearance_mode("dark")

def T_convert():
    input_unit = T_select_input.get()
    output_unit = T_select_output.get()
    value = entryInt.get()

    T_conversion_factors = {
        "Celsius [°C]": {"Fahrenheit [°F]": lambda x: x * 1.8 + 32, "kelvin [K]": lambda x: x + 273.15},
        "Fahrenheit [°F]": {"Celsius [°C]": lambda x: (x - 32) / 1.8, "kelvin [K]": lambda x: (x + 459.67) * 5/9},
        "kelvin [K]": {"Celsius [°C]": lambda x: x - 273.15, "Fahrenheit [°F]": lambda x: x * 9/5 - 459.67},
    }

    if input_unit == output_unit:
        result = value
    else:
        result = T_conversion_factors[input_unit][output_unit](value)

    output_box_text.set(result)

def L_convert():
    input_unit = L_select_input.get()
    output_unit = L_select_output.get()
    value = entryInt.get()

    L_conversion_factors = {
        ("centimeter [cm]", "decimeter [dm]"): 0.1,
        ("centimeter [cm]", "meter [m]"): 0.01,
        ("centimeter [cm]", "kilometer [km]"): 0.00001,
        ("centimeter [cm]", "inch [in]"): 0.393701,
        ("centimeter [cm]", "foot [ft]"): 0.0328084,
        ("centimeter [cm]", "yard [yd]"): 0.0109361,
        ("centimeter [cm]", "mile [mi]"): 0.00000621371,
        ("decimeter [dm]", "meter [m]"): 0.1,
        ("decimeter [dm]", "kilometer [km]"): 0.0001,
        ("decimeter [dm]", "inch [in]"): 3.93701,
        ("decimeter [dm]", "foot [ft]"): 0.328084,
        ("decimeter [dm]", "yard [yd]"): 0.109361,
        ("decimeter [dm]", "mile [mi]"): 0.0000621371,
        ("meter [m]", "kilometer [km]"): 0.001,
        ("meter [m]", "inch [in]"): 39.3701,
        ("meter [m]", "foot [ft]"): 3.28084,
        ("meter [m]", "yard [yd]"): 1.09361,
        ("meter [m]", "mile [mi]"): 0.000621371,
        ("kilometer [km]", "inch [in]"): 39370.1,
        ("kilometer [km]", "foot [ft]"): 3280.84,
        ("kilometer [km]", "yard [yd]"): 1093.61,
        ("kilometer [km]", "mile [mi]"): 0.621371,
        ("inch [in]", "foot [ft]"): 0.0833333,
        ("inch [in]", "yard [yd]"): 0.0277778,
        ("inch [in]", "mile [mi]"): 0.0000157828,
        ("foot [ft]", "yard [yd]"): 0.333333,
        ("foot [ft]", "mile [mi]"): 0.000189394,
        ("yard [yd]", "mile [mi]"): 0.000568182
    }

    factor = L_conversion_factors.get((input_unit, output_unit), 1)
    result = value * factor

    output_box_text.set(result)

def A_convert():
    input_unit = A_select_input.get()
    output_unit = A_select_output.get()
    value = entryInt.get()

    A_conversion_factors = {("square centimeter [cm²]", "square centimeter [cm²]"): 1,
                        ("square centimeter [cm²]", "square decimetre [dm²]"): 0.01,
                        ("square centimeter [cm²]", "square meter [m²]"): 0.0001,
                        ("square centimeter [cm²]", "square decametre [dam²]"): 0.000001,
                        ("square centimeter [cm²]", "square hectometre [hm²]"): 0.00000001,
                        ("square centimeter [cm²]", "square kilometer [km²]"): 0.0000000001,
                        ("square centimeter [cm²]", "square inch [in²]"): 0.155,
                        ("square centimeter [cm²]", "square foot [ft²]"): 0.001076,
                        ("square centimeter [cm²]", "square yard [yd²]"): 0.0001196,
                        ("square centimeter [cm²]", "square mile [mi²]"): 0.00000003861,
                        ("square centimeter [cm²]", "acre"): 0.00002471,
                        
                        ("square decimetre [dm²]", "square centimeter [cm²]"): 100,
                        ("square decimetre [dm²]", "square decimetre [dm²]"): 1,
                        ("square decimetre [dm²]", "square meter [m²]"): 0.01,
                        ("square decimetre [dm²]", "square decametre [dam²]"): 0.0001,
                        ("square decimetre [dm²]", "square hectometre [hm²]"): 0.000001,
                        ("square decimetre [dm²]", "square kilometer [km²]"): 0.00000001,
                        ("square decimetre [dm²]", "square inch [in²]"): 15.5,
                        ("square decimetre [dm²]", "square foot [ft²]"): 0.1076,
                        ("square decimetre [dm²]", "square yard [yd²]"): 0.01196,
                        ("square decimetre [dm²]", "square mile [mi²]"): 0.000003861,
                        ("square decimetre [dm²]", "acre"): 0.002471,
                        
                        ("square meter [m²]", "square centimeter [cm²]"): 10000,
                        ("square meter [m²]", "square decimetre [dm²]"): 100,
                        ("square meter [m²]", "square meter [m²]"): 1,
                        ("square meter [m²]", "square decametre [dam²]"): 0.01,
                        ("square meter [m²]", "square hectometre [hm²]"): 0.0001,
                        ("square meter [m²]", "square kilometer [km²]"): 0.000001,
                        ("square meter [m²]", "square inch [in²]"): 1550,
                        ("square meter [m²]", "square foot [ft²]"): 10.764,
                        ("square meter [m²]", "square yard [yd²]"): 1.196,
                        ("square meter [m²]", "square mile [mi²]"): 0.0000003861,
                        ("square meter [m²]", "acre"): 0.000247,

                        ("square decametre [dam²]", "square centimeter [cm²]"): 1000000,
                        ("square decametre [dam²]", "square decimetre [dm²]"): 10000,
                        ("square decametre [dam²]", "square meter [m²]"): 100,
                        ("square decametre [dam²]", "square decametre [dam²]"): 1,
                        ("square decametre [dam²]", "square hectometre [hm²]"): 0.01,
                        ("square decametre [dam²]", "square kilometer [km²]"): 0.0001,
                        ("square decametre [dam²]", "square inch [in²]"): 15500,
                        ("square decametre [dam²]", "square foot [ft²]"): 107.639,
                        ("square decametre [dam²]", "square yard [yd²]"): 11.9599,
                        ("square decametre [dam²]", "square mile [mi²]"): 0.003861,
                        ("square decametre [dam²]", "acre"): 2.471043946731,

                        ("square hectometre [hm²]", "square centimeter [cm²]"): 10000000000,
                        ("square hectometre [hm²]", "square decimetre [dm²]"): 100000000,
                        ("square hectometre [hm²]", "square meter [m²]"): 10000,
                        ("square hectometre [hm²]", "square decametre [dam²]"): 100,
                        ("square hectometre [hm²]", "square kilometer [km²]"): 0.01,
                        ("square hectometre [hm²]", "square inch [in²]"): 1550003100,
                        ("square hectometre [hm²]", "square foot [ft²]"): 10763910.42,
                        ("square hectometre [hm²]", "square yard [yd²]"): 1195990.05,
                        ("square hectometre [hm²]", "square mile [mi²]"): 0.003861,
                        ("square hectometre [hm²]", "acre"): 247.105381,
                        ("square hectometre [hm²]", "square hectometre [hm²]"): 1,

                        ("square kilometer [km²]", "square meter [m²]"): 1_000_000,
                        ("square kilometer [km²]", "square centimeter [cm²]"): 1_000_000_000_000,
                        ("square kilometer [km²]", "square kilometer [km²]"): 1,
                        ("square kilometer [km²]", "square decametre [dam²]"): 10000,
                        ("square kilometer [km²]", "square hectometre [hm²]"): 100,
                        ("square kilometer [km²]", "square mile [mi²]"): 0.386102,
                        ("square kilometer [km²]", "square yard [yd²]"): 1_195_990.05,
                        ("square kilometer [km²]", "square foot [ft²]"): 10_763_910.42,
                        ("square kilometer [km²]", "square inch [in²]"): 1_550_003_100.01,
                        ("square kilometer [km²]", "hectare [ha]"): 100,
                        ("square kilometer [km²]", "acre"): 247.105381,

                        ("square inch [in²]", "square centimeter [cm²]"): 6.4516,
                        ("square inch [in²]", "square decimetre [dm²]"): 0.064516,
                        ("square inch [in²]", "square meter [m²]"): 0.00064516,
                        ("square inch [in²]", "square decametre [dam²]"): 0.0000064516,
                        ("square inch [in²]", "square hectometre [hm²]"): 0.000000064516,
                        ("square inch [in²]", "square kilometer [km²]"): 0.00000000064516,
                        ("square inch [in²]", "square foot [ft²]"): 0.00694444,
                        ("square inch [in²]", "square yard [yd²]"): 0.000771605,
                        ("square inch [in²]", "square mile [mi²]"): 0.000000000249097,
                        ("square inch [in²]", "acre"): 0.00000015942,
                        ("square inch [in²]", "square inch [in²]"): 1,

                        ("square foot [ft²]", "square centimeter [cm²]"): 929.03,
                        ("square foot [ft²]", "square decimetre [dm²]"): 9.2903,
                        ("square foot [ft²]", "square meter [m²]"): 0.092903,
                        ("square foot [ft²]", "square decametre [dam²]"): 0.00092903,
                        ("square foot [ft²]", "square hectometre [hm²]"): 0.0000092903,
                        ("square foot [ft²]", "square kilometer [km²]"): 0.000000092903,
                        ("square foot [ft²]", "square inch [in²]"): 144,
                        ("square foot [ft²]", "square yard [yd²]"): 0.11111,
                        ("square foot [ft²]", "square mile [mi²]"): 0.00000003587,
                        ("square foot [ft²]", "acre"): 0.000022957,
                        ("square foot [ft²]", "square foot [ft²]"): 1,

                        ("square yard [yd²]", "square centimeter [cm²]"): 8361.27,
                        ("square yard [yd²]", "square decimetre [dm²]"): 836.127,
                        ("square yard [yd²]", "square meter [m²]"): 0.836127,
                        ("square yard [yd²]", "square decametre [dam²]"): 0.00836127,
                        ("square yard [yd²]", "square hectometre [hm²]"): 0.00000836127,
                        ("square yard [yd²]", "square kilometer [km²]"): 0.000000836127,
                        ("square yard [yd²]", "square inch [in²]"): 1296,
                        ("square yard [yd²]", "square foot [ft²]"): 9,
                        ("square yard [yd²]", "square mile [mi²]"): 0.00000032283,
                        ("square yard [yd²]", "acre"): 0.000206612,
                        ("square yard [yd²]", "square yard [yd²]"): 1,

                        ("square mile [mi²]", "square centimeter [cm²]"): 25899881103.36,
                        ("square mile [mi²]", "square decimetre [dm²]"): 258998811.0336,
                        ("square mile [mi²]", "square meter [m²]"): 2589988.110336,
                        ("square mile [mi²]", "square decametre [dam²]"): 25899.88110336,
                        ("square mile [mi²]", "square hectometre [hm²]"): 258.9988110336,
                        ("square mile [mi²]", "square kilometer [km²]"): 2.589988110336,
                        ("square mile [mi²]", "square inch [in²]"): 4014489600,
                        ("square mile [mi²]", "square foot [ft²]"): 27878400,
                        ("square mile [mi²]", "square yard [yd²]"): 3097600,
                        ("square mile [mi²]", "acre"): 640,
                        ("square mile [mi²]", "square mile [mi²]"): 1,

                        ("acre", "square centimeter [cm²]"): 40468564.224,
                        ("acre", "square decimetre [dm²]"): 404685.64224,
                        ("acre", "square meter [m²]"): 4046.8564224,
                        ("acre", "square decametre [dam²]"): 40.468564224,
                        ("acre", "square hectometre [hm²]"): 0.40468564224,
                        ("acre", "square kilometer [km²]"): 0.0040468564224,
                        ("acre", "square inch [in²]"): 6272640,
                        ("acre", "square foot [ft²]"): 43560,
                        ("acre", "square yard [yd²]"): 4840,
                        ("acre", "square mile [mi²]"): 0.0015625,
                        ("acre", "acre"): 1
    }

    factor = A_conversion_factors.get((input_unit, output_unit), 1)
    result = value * factor

    output_box_text.set(result)

def V_convert():
    input_unit = V_select_input.get()
    output_unit = V_select_output.get()
    value = entryInt.get()

    V_conversion_factors = {
                        ("cubic kilometer [km³]", "cubic mile [mi³]"): 0.239912,
                        ("cubic kilometer [km³]", "cubic meter [m³]"): 1e+9,
                        ("cubic kilometer [km³]", "barrel (US)"): 6.28981e+9,
                        ("cubic kilometer [km³]", "barrel (UK)"): 5.61171e+9,
                        ("cubic kilometer [km³]", "cubic yard [yd³]"): 1.30795e+9,
                        ("cubic kilometer [km³]", "cubic foot [ft³]"): 3.53147e+10,
                        ("cubic kilometer [km³]", "cubic decimeter [dm³]"): 1e+18,
                        ("cubic kilometer [km³]", "gallon (US)"): 2.64172e+10,
                        ("cubic kilometer [km³]", "gallon (UK)"): 2.19912e+10,
                        ("cubic kilometer [km³]", "liter [L]"): 1e+12,
                        ("cubic kilometer [km³]", "cubic inch [in³]"): 6.10237e+13,
                        ("cubic kilometer [km³]", "fluid ounce [fl oz (US)]"): 8.45351e+10,
                        ("cubic kilometer [km³]", "fluid ounce [fl oz (UK)]"): 7.04194e+10,
                        ("cubic kilometer [km³]", "cubic centimeter [cm³]"): 1e+18,
                        ("cubic kilometer [km³]", "milliliter [mL]"): 1e+15,
                        ("cubic kilometer [km³]", "cubic kilometer [km³]"): 1,

                        ("cubic mile [mi³]", "cubic meter [m³]"): 4.16818e+9,
                        ("cubic mile [mi³]", "barrel (US)"): 1.03987e+10,
                        ("cubic mile [mi³]", "barrel (UK)"): 9.26218e+9,
                        ("cubic mile [mi³]", "cubic yard [yd³]"): 2.14359e+9,
                        ("cubic mile [mi³]", "cubic foot [ft³]"): 5.78704e+10,
                        ("cubic mile [mi³]", "cubic decimeter [dm³]"): 4.16818e+12,
                        ("cubic mile [mi³]", "gallon (US)"): 1.10118e+11,
                        ("cubic mile [mi³]", "gallon (UK)"): 9.14397e+10,
                        ("cubic mile [mi³]", "liter [L]"): 4.16818e+12,
                        ("cubic mile [mi³]", "cubic inch [in³]"): 2.5515e+14,
                        ("cubic mile [mi³]", "fluid ounce [fl oz (US)]"): 3.53268e+11,
                        ("cubic mile [mi³]", "fluid ounce [fl oz (UK)]"): 2.94328e+11,
                        ("cubic mile [mi³]", "cubic centimeter [cm³]"): 4.16818e+12,
    }

    factor = V_conversion_factors.get((input_unit, output_unit), 1)
    result = value * factor

    output_box_text.set(result)

def box_reset():
    output_box_text.set("")
    entryInt.set(0)

def show_length_widgets():
    box_reset()
    T_convert_button.place_forget()
    T_select_input.place_forget()
    T_select_output.place_forget()
    T_Label.pack_forget()
    A_select_input.place_forget()
    A_select_output.place_forget()
    A_Label.pack_forget()
    A_convert_button.place_forget()
    V_select_input.place_forget()
    V_select_output.place_forget()
    V_Label.pack_forget()
    V_convert_button.place_forget()
    L_select_input.place(x=175, y=105)
    L_select_output.place(x=360, y=105)
    L_Label.pack(fill="both")
    L_convert_button.place(x=262, y=195)

def show_temperature_widgets():
    box_reset()
    L_select_input.place_forget()
    L_select_output.place_forget()
    L_Label.pack_forget()
    L_convert_button.place_forget()
    A_select_input.place_forget()
    A_select_output.place_forget()
    A_Label.pack_forget()
    A_convert_button.place_forget()
    V_select_input.place_forget()
    V_select_output.place_forget()
    V_Label.pack_forget()
    V_convert_button.place_forget()
    T_convert_button.place(x=262, y=195)
    T_select_input.place(x=175, y=105)
    T_select_output.place(x=360, y=105)
    T_Label.pack(fill="both")

def show_area_widgets():
    box_reset()
    T_convert_button.place_forget()
    T_select_input.place_forget()
    T_select_output.place_forget()
    T_Label.pack_forget()
    L_select_input.place_forget()
    L_select_output.place_forget()
    L_Label.pack_forget()
    L_convert_button.place_forget()
    V_select_input.place_forget()
    V_select_output.place_forget()
    V_Label.pack_forget()
    V_convert_button.place_forget()
    A_convert_button.place(x=262, y=195)
    A_select_input.place(x=175, y=105)
    A_select_output.place(x=360, y=105)
    A_Label.pack(fill="both")

def show_volume_widgets():
    box_reset()
    T_convert_button.place_forget()
    T_select_input.place_forget()
    T_select_output.place_forget()
    T_Label.pack_forget()
    L_select_input.place_forget()
    L_select_output.place_forget()
    L_Label.pack_forget()
    L_convert_button.place_forget()
    A_select_input.place_forget()
    A_select_output.place_forget()
    A_Label.pack_forget()
    A_convert_button.place_forget()
    V_convert_button.place(x=262, y=195)
    V_select_input.place(x=175, y=105)
    V_select_output.place(x=360, y=105)
    V_Label.pack(fill="both")

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


#this button frame is where all the buttons are which are used for manoeuvring through the app
sidebar = tk.Frame(window, background="black")
sidebar.rowconfigure(0, weight=1)
sidebar.rowconfigure(1, weight=1)
sidebar.rowconfigure(2, weight=1)
sidebar.rowconfigure(3, weight=1)
sidebar.columnconfigure(0, weight=1)
sidebar.pack(side="left", fill="y")

#Temperature
#This is where all the widgets regarding the Temperature section are

T_Label = ctk.CTkLabel(window, text="Temperature", font=("Arial", 26), text_color="white", bg_color="black")
T_Label.pack(fill="both")

T_convert_button = ctk.CTkButton(window, text="Convert", font=("Arial", 16), command=T_convert)
T_convert_button.place(x=262, y=195)

T_button = ctk.CTkButton(sidebar, text="Temperature", font=("Arial", 16), command=show_temperature_widgets)
T_button.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

T_select_input = customtkinter.CTkOptionMenu(window, values=["Celsius [°C]", 
                                                             "Fahrenheit [°F]", 
                                                             "kelvin [K]"], width=130)
T_select_input.place(x=175, y=105)
T_select_output = customtkinter.CTkOptionMenu(window, values=["Celsius [°C]", 
                                                              "Fahrenheit [°F]", 
                                                              "kelvin [K]"], width=130)
T_select_output.place(x=360, y=105)

#Length
#This is where all the widgets regarding the Length section are

L_Label = ctk.CTkLabel(window, text="Length", font=("Arial", 26), text_color="white", bg_color="black")

L_convert_button = ctk.CTkButton(window, text="Convert", font=("Arial", 16), command=L_convert)

L_button = ctk.CTkButton(sidebar, text="Length", font=("Arial", 16), command=show_length_widgets)
L_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

L_select_input = customtkinter.CTkOptionMenu(window, values=["centimeter [cm]", 
                                                             "decimeter [dm]", 
                                                             "meter [m]", 
                                                             "kilometer [km]", 
                                                             "inch [in]", 
                                                             "foot [ft]", 
                                                             "yard [yd]", 
                                                             "mile [mi]"], width=130)
L_select_output = customtkinter.CTkOptionMenu(window, values=["centimeter [cm]", 
                                                              "decimeter [dm]", 
                                                              "meter [m]", 
                                                              "kilometer [km]", 
                                                              "inch [in]", 
                                                              "foot [ft]", 
                                                              "yard [yd]", 
                                                              "mile [mi]"], width=130)

#Area
#This is where all the widgets regarding the Area section are

A_Label = ctk.CTkLabel(window, text="Area", font=("Arial", 26), text_color="white", bg_color="black")

A_convert_button = ctk.CTkButton(window, text="Convert", font=("Arial", 16), command=A_convert)

A_button = ctk.CTkButton(sidebar, text="Area", font=("Arial", 16), command=show_area_widgets)
A_button.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

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

#Volume
#This is where all  the widgets regarding the Volume section are

V_Label = ctk.CTkLabel(window, text="Volume", font=("Arial", 26), text_color="white", bg_color="black")

V_convert_button = ctk.CTkButton(window, text="Convert", font=("Arial", 16), command=V_convert)

V_select_input = customtkinter.CTkOptionMenu(window, values=["cubic kilometer [km³]",
                                                             "cubic mile [mi³]",
                                                             "cubic meter [m³]",
                                                             "barrel (US)",
                                                             "barrel (UK)",
                                                             "cubic yard [yd³]",
                                                             "cubic foot [ft³]",    
                                                             "cubic decimeter [dm³]",    
                                                             "gallon (US)",    
                                                             "gallon (UK)",    
                                                             "liter [L]",    
                                                             "cubic inch [in³]",    
                                                             "fluid ounce [fl oz (US)]",    
                                                             "fluid ounce [fl oz (UK)]",    
                                                             "cubic centimeter [cm³]",    
                                                             "milliliter [mL]"]
, width=130)
V_select_output = customtkinter.CTkOptionMenu(window, values=["cubic kilometer [km³]",
                                                             "cubic mile [mi³]",
                                                             "cubic meter [m³]",
                                                             "barrel (US)",
                                                             "barrel (UK)",
                                                             "cubic yard [yd³]",
                                                             "cubic foot [ft³]",    
                                                             "cubic decimeter [dm³]",    
                                                             "gallon (US)",    
                                                             "gallon (UK)",    
                                                             "liter [L]",    
                                                             "cubic inch [in³]",    
                                                             "fluid ounce [fl oz (US)]",    
                                                             "fluid ounce [fl oz (UK)]",    
                                                             "cubic centimeter [cm³]",    
                                                             "milliliter [mL]"], width=130)

V_button = ctk.CTkButton(sidebar, text="Volume", font=("Arial", 16), command=show_volume_widgets)
V_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

#copy to clipboard button coming soon




window.mainloop()