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
        "centimeter [cm]": {
            "decimeter [dm]": 0.1, 
            "meter [m]": 0.01, 
            "kilometer [km]": 0.00001, 
            "inch [in]": 0.393701, 
            "foot [ft]": 0.0328084, 
            "yard [yd]": 0.0109361, 
            "mile [mi]": 0.00000621371, 
            "centimeter [cm]": 1
        },
        "decimeter [dm]": {
            "meter [m]": 0.1, 
            "kilometer [km]": 0.0001, 
            "inch [in]": 3.93701, 
            "foot [ft]": 0.328084, 
            "yard [yd]": 0.109361, 
            "mile [mi]": 0.0000621371, 
            "centimeter [cm]": 10, 
            "decimeter [dm]": 1
        },
        "meter [m]": {
            "kilometer [km]": 0.001,
            "inch [in]": 39.3701,
            "foot [ft]": 3.28084,
            "yard [yd]": 1.09361,
            "mile [mi]": 0.000621371,
            "centimeter [cm]": 100,
            "decimeter [dm]": 10,
            "meter [m]": 1
        },
        "kilometer [km]": {
            "inch [in]": 39370.1,
            "foot [ft]": 3280.84,
            "yard [yd]": 1093.61,
            "mile [mi]": 0.621371,
            "centimeter [cm]": 1000000,
            "decimeter [dm]": 10000,
            "meter [m]": 1000,
            "kilometer [km]": 1
        },
        "inch [in]": {
            "kilometer [km]": 0.0000254,
            "meter [m]": 0.0254,
            "decimeter [dm]": 0.254,
            "centimeter [cm]": 2.54,
            "foot [ft]": 0.0833333,
            "yard [yd]": 0.0277778,
            "mile [mi]": 0.0000157828,
            "inch [in]": 1
        },
        "foot [ft]": {
            "kilometer [km]": 0.0003048,
            "meter [m]": 0.3048,
            "decimeter [dm]": 3.048,
            "centimeter [cm]": 30.48,
            "yard [yd]": 0.333333,
            "mile [mi]": 0.000189394,
            "inch [in]": 12,
            "foot [ft]": 1
        },
        "yard [yd]": {
            "kilometer [km]": 0.0009144,
            "meter [m]": 0.9144,
            "decimeter [dm]": 9.144,
            "centimeter [cm]": 91.44,
            "foot [ft]": 3,
            "mile [mi]": 0.000568182,
            "inch [in]": 36,
            "yard [yd]": 1
        },
        "mile [mi]": {
            "kilometer [km]": 1.609344,
            "meter [m]": 1609.344,
            "decimeter [dm]": 16093.44,
            "centimeter [cm]": 160934.4,
            "foot [ft]": 5280,
            "inch [in]": 36,
            "yard [yd]": 1760,
            "mile [mi]": 1
        }
    }

    factor = L_conversion_factors.get(input_unit, {}).get(output_unit, 1)
    result = value * factor

    output_box_text.set(result)

def A_convert():
    input_unit = A_select_input.get()
    output_unit = A_select_output.get()
    value = entryInt.get()

    A_conversion_factors = {
                        "square centimeter [cm²]": {
                            "square centimeter [cm²]": 1,
                            "square decimetre [dm²]": 0.01,
                            "square meter [m²]": 0.0001,
                            "square decametre [dam²]": 0.000001,
                            "square hectometre [hm²]": 0.00000001,
                            "square kilometer [km²]": 0.0000000001,
                            "square inch [in²]": 0.155,
                            "square foot [ft²]": 0.001076,
                            "square yard [yd²]": 0.0001196,
                            "square mile [mi²]": 0.00000003861,
                            "acre": 0.00002471
                        },
                        "square decimetre [dm²]": {
                            "square centimeter [cm²]": 100,
                            "square decimetre [dm²]": 1,
                            "square meter [m²]": 0.01,
                            "square decametre [dam²]": 0.0001,
                            "square hectometre [hm²]": 0.000001,
                            "square kilometer [km²]": 0.00000001,
                            "square inch [in²]": 15.5,
                            "square foot [ft²]": 0.1076,
                            "square yard [yd²]": 0.01196,
                            "square mile [mi²]": 0.000003861,
                            "acre": 0.002471
                        },
                        "square meter [m²]": {
                            "square centimeter [cm²]": 10000,
                            "square decimetre [dm²]": 100,
                            "square meter [m²]": 1,
                            "square decametre [dam²]": 0.01,
                            "square hectometre [hm²]": 0.0001,
                            "square kilometer [km²]": 0.000001,
                            "square inch [in²]": 1550,
                            "square foot [ft²]": 10.764,
                            "square yard [yd²]": 1.196,
                            "square mile [mi²]": 0.0000003861,
                            "acre": 0.000247
                        },
                        "square decametre [dam²]": {
                            "square centimeter [cm²]": 1000000,
                            "square decimetre [dm²]": 10000,
                            "square meter [m²]": 100,
                            "square decametre [dam²]": 1,
                            "square hectometre [hm²]": 0.01,
                            "square kilometer [km²]": 0.0001,
                            "square inch [in²]": 15500,
                            "square foot [ft²]": 107.639,
                            "square yard [yd²]": 11.9599,
                            "square mile [mi²]": 0.003861,
                            "acre": 2.471043946731
                        },
                        "square hectometre [hm²]": {
                            "square centimeter [cm²]": 10000000000,
                            "square decimetre [dm²]": 100000000,
                            "square meter [m²]": 10000,
                            "square decametre [dam²]": 100,
                            "square kilometer [km²]": 0.01,
                            "square inch [in²]": 1550003100,
                            "square foot [ft²]": 10763910.42,
                            "square yard [yd²]": 1195990.05,
                            "square mile [mi²]": 0.003861,
                            "acre": 247.105381,
                            "square hectometre [hm²]": 1
                        },
                        "square kilometer [km²]": {
                            "square meter [m²]": 1000000,
                            "square centimeter [cm²]": 1000000000000,
                            "square kilometer [km²]": 1,
                            "square decametre [dam²]": 10000,
                            "square hectometre [hm²]": 100,
                            "square mile [mi²]": 0.386102,
                            "square yard [yd²]": 1195990.05,
                            "square foot [ft²]": 10763910.42,
                            "square inch [in²]": 1550003100.01,
                            "hectare [ha]": 100,
                            "acre": 247.105381
                        },
                        "square inch [in²]": {
                            "square centimeter [cm²]": 6.4516,
                            "square decimetre [dm²]": 0.064516,
                            "square meter [m²]": 0.00064516,
                            "square decametre [dam²]": 0.0000064516,
                            "square hectometre [hm²]": 0.000000064516,
                            "square kilometer [km²]": 0.00000000064516,
                            "square foot [ft²]": 0.00694444,
                            "square yard [yd²]": 0.000771605,
                            "square mile [mi²]": 0.000000000249097,
                            "acre": 0.00000015942,
                            "square inch [in²]": 1
                        },
                        "square foot [ft²]": {
                            "square centimeter [cm²]": 929.03,
                            "square decimetre [dm²]": 9.2903,
                            "square meter [m²]": 0.092903,
                            "square decametre [dam²]": 0.00092903,
                            "square hectometre [hm²]": 0.0000092903,
                            "square kilometer [km²]": 0.000000092903,
                            "square inch [in²]": 144,
                            "square yard [yd²]": 0.11111,
                            "square mile [mi²]": 0.00000003587,
                            "acre": 0.000022957,
                            "square foot [ft²]": 1
                        },
                        "square yard [yd²]": {
                            "square centimeter [cm²]": 8361.27,
                            "square decimetre [dm²]": 836.127,
                            "square meter [m²]": 0.836127,
                            "square decametre [dam²]": 0.00836127,
                            "square hectometre [hm²]": 0.00000836127,
                            "square kilometer [km²]": 0.000000836127,
                            "square inch [in²]": 1296,
                            "square foot [ft²]": 9,
                            "square mile [mi²]": 0.00000032283,
                            "acre": 0.000206612,
                            "square yard [yd²]": 1
                        },
                        "square mile [mi²]": {
                            "square centimeter [cm²]": 25899881103.36,
                            "square decimetre [dm²]": 258998811.0336,
                            "square meter [m²]": 2589988.110336,
                            "square decametre [dam²]": 25899.88110336,
                            "square hectometre [hm²]": 258.9988110336,
                            "square kilometer [km²]": 2.589988110336,
                            "square inch [in²]": 4014489600,
                            "square foot [ft²]": 27878400,
                            "square yard [yd²]": 3097600,
                            "acre": 640,
                            "square mile [mi²]": 1
                        },
                        "acre": {
                            "square centimeter [cm²]": 40468564.224,
                            "square decimetre [dm²]": 404685.64224,
                            "square meter [m²]": 4046.8564224,
                            "square decametre [dam²]": 40.468564224,
                            "square hectometre [hm²]": 0.40468564224,
                            "square kilometer [km²]": 0.0040468564224,
                            "square inch [in²]": 6272640,
                            "square foot [ft²]": 43560,
                            "square yard [yd²]": 4840,
                            "square mile [mi²]": 0.0015625,
                            "acre": 1
                        }
    }

    factor = A_conversion_factors.get(input_unit, {}).get(output_unit, 1)
    result = value * factor

    output_box_text.set(result)

def V_convert():
    input_unit = V_select_input.get()
    output_unit = V_select_output.get()
    value = entryInt.get()

    V_conversion_factors = {
        "cubic kilometer [km³]": {
            "cubic mile [mi³]": 0.239912,
            "cubic meter [m³]": 1e+9,
            "cubic yard [yd³]": 1.30795e+9,
            "cubic foot [ft³]": 3.53147e+10,
            "cubic decimeter [dm³]": 1e+18,
            "gallon (US)": 2.64172e+10,
            "gallon (UK)": 2.19912e+10,
            "liter [L]": 1e+12,
            "cubic inch [in³]": 6.10237e+13,
            "fluid ounce [fl oz (US)]": 8.45351e+10,
            "fluid ounce [fl oz (UK)]": 7.04194e+10,
            "cubic centimeter [cm³]": 1e+18,
            "milliliter [mL]": 1e+15,
            "cubic kilometer [km³]": 1
        },
        "cubic mile [mi³]": {
            "cubic kilometer [km³]": 4.16818,
            "cubic meter [m³]": 4.16818e+12,
            "cubic yard [yd³]": 2.14335e+12,
            "cubic foot [ft³]": 5.76456e+13,
            "cubic decimeter [dm³]": 4.16818e+15,
            "gallon (US)": 1.09779e+11,
            "gallon (UK)": 9.19318e+10,
            "liter [L]": 4.16818e+12,
            "cubic inch [in³]": 2.51986e+14,
            "fluid ounce [fl oz (US)]": 3.47827e+11,
            "fluid ounce [fl oz (UK)]": 2.89183e+11,
            "cubic centimeter [cm³]": 4.16818e+21,
            "milliliter [mL]": 4.16818e+18,
            "cubic mile [mi³]": 1
        },
        "cubic meter [m³]": {
            "cubic kilometer [km³]": 1e-9,
            "cubic mile [mi³]": 2.3991e-10,
            "cubic yard [yd³]": 1.30795,
            "cubic foot [ft³]": 35.3147,
            "cubic decimeter [dm³]": 1000,
            "gallon (US)": 264.172,
            "gallon (UK)": 219.912,
            "liter [L]": 1000,
            "cubic inch [in³]": 61023.7,
            "fluid ounce [fl oz (US)]": 33814,
            "fluid ounce [fl oz (UK)]": 35195,
            "cubic centimeter [cm³]": 1e+6,
            "milliliter [mL]": 1e+6,
            "cubic meter [m³]": 1
        },
        "cubic yard [yd³]": {
            "cubic kilometer [km³]": 7.64555e-10,
            "cubic mile [mi³]": 8.73494e-11,
            "cubic meter [m³]": 0.764555,
            "cubic foot [ft³]": 27,
            "cubic decimeter [dm³]": 764.555,
            "gallon (US)": 201.974,
            "gallon (UK)": 168.178,
            "liter [L]": 764.555,
            "cubic inch [in³]": 46656,
            "fluid ounce [fl oz (US)]": 25852.7,
            "fluid ounce [fl oz (UK)]": 27008.6,
            "cubic centimeter [cm³]": 7.64555e+5,
            "milliliter [mL]": 7.64555e+5,
            "cubic yard [yd³]": 1
        },
        "cubic foot [ft³]": {
            "cubic kilometer [km³]": 2.83168e-11,
            "cubic mile [mi³]": 6.79357e-12,
            "cubic meter [m³]": 0.0283168,
            "cubic yard [yd³]": 0.037037,
            "cubic decimeter [dm³]": 28.3168,
            "gallon (US)": 7.48052,
            "gallon (UK)": 6.22884,
            "liter [L]": 28.3168,
            "cubic inch [in³]": 1728,
            "fluid ounce [fl oz (US)]": 957.506,
            "fluid ounce [fl oz (UK)]": 996.614,
            "cubic centimeter [cm³]": 28316.8,
            "milliliter [mL]": 28316.8,
            "cubic foot [ft³]": 1
        },
        "cubic decimeter [dm³]": {
            "cubic kilometer [km³]": 1e-18,
            "cubic mile [mi³]": 2.39912e-16,
            "cubic meter [m³]": 0.001,
            "cubic yard [yd³]": 0.00130795,
            "cubic foot [ft³]": 0.0353147,
            "gallon (US)": 0.264172,
            "gallon (UK)": 0.219912,
            "liter [L]": 1,
            "cubic inch [in³]": 0.0610237,
            "fluid ounce [fl oz (US)]": 0.033814,
            "fluid ounce [fl oz (UK)]": 0.0284131,
            "cubic centimeter [cm³]": 1000,
            "milliliter [mL]": 1000,
            "cubic decimeter [dm³]": 1
        },
        "gallon (US)":{
            "cubic kilometer [km³]": 3.78541e-11,
            "cubic mile [mi³]": 9.09473e-12,
            "cubic meter [m³]": 0.00378541,
            "cubic yard [yd³]": 0.00576456,
            "cubic foot [ft³]": 0.133681,
            "gallon (UK)": 0.83267382,
            "cubic decimeter [dm³]": 3.78541,
            "liter [L]": 3.78541,
            "cubic inch [in³]": 231,
            "fluid ounce [fl oz (US)]": 128,
            "fluid ounce [fl oz (UK)]": 153.722,
            "cubic centimeter [cm³]": 3785.41,
            "milliliter [mL]": 3785.41,
            "gallon (US)": 1
        },
        "gallon (UK)": {
            "cubic kilometer [km³]": 4.54609e-13,
            "cubic mile [mi³]": 1.20095e-12,
            "cubic meter [m³]": 0.00454609,
            "cubic yard [yd³]": 0.00163961,
            "cubic foot [ft³]": 0.160543,
            "cubic decimeter [dm³]": 4.54609,
            "gallon (US)": 1.20095,
            "liter [L]": 4.54609,
            "cubic inch [in³]": 277.419,
            "fluid ounce [fl oz (US)]": 153.722,
            "fluid ounce [fl oz (UK)]": 160,
            "cubic centimeter [cm³]": 4546.09,
            "milliliter [mL]": 4546.09,
            "gallon (UK)": 1
        },
        "liter [L]": {
            "cubic kilometer [km³]": 1e-12,
            "cubic mile [mi³]": 2.39912e-13,
            "cubic meter [m³]": 0.001,
            "cubic yard [yd³]": 0.764555,
            "cubic foot [ft³]": 28.3168,
            "cubic decimeter [dm³]": 1,
            "gallon (US)": 0.264172,
            "gallon (UK)": 0.219969,
            "cubic inch [in³]": 0.0610237,
            "fluid ounce [fl oz (US)]": 33.814,
            "fluid ounce [fl oz (UK)]": 35.1951,
            "cubic centimeter [cm³]": 1000,
            "milliliter [mL]": 1000,
            "liter [L]": 1
        },
        "cubic inch [in³]": {
            "cubic kilometer [km³]": 1.63871e-14,
            "cubic mile [mi³]": 3.93147e-12,
            "cubic meter [m³]": 1.63871e-5,
            "cubic yard [yd³]": 0.0000214335,
            "cubic foot [ft³]": 0.000578704,
            "cubic decimeter [dm³]": 0.0163871,
            "gallon (US)": 0.004329,
            "gallon (UK)": 0.00529115,
            "liter [L]": 0.0163871,
            "fluid ounce [fl oz (US)]": 0.00173387,
            "fluid ounce [fl oz (UK)]": 0.00176838,
            "cubic centimeter [cm³]": 0.163871,
            "milliliter [mL]": 0.163871,
            "cubic inch [in³]": 1
        },
        "fluid ounce [fl oz (US)]": {
            "cubic kilometer [km³]": 2.95735e-5,
            "cubic mile [mi³]": 7.48915e-6,
            "cubic meter [m³]": 0.0000295735,
            "cubic yard [yd³]": 0.000037037,
            "cubic foot [ft³]": 0.00104438,
            "cubic decimeter [dm³]": 0.0295735,
            "gallon (US)": 0.0078125,
            "gallon (UK)": 0.00650521,
            "liter [L]": 0.0295735,
            "cubic inch [in³]": 0.578704,
            "fluid ounce [fl oz (UK)]": 1.04084227,
            "cubic centimeter [cm³]": 29.5735,
            "milliliter [mL]": 29.5735,
            "fluid ounce [fl oz (US)]": 1
        },
        "fluid ounce [fl oz (UK)]": {
            "cubic kilometer [km³]": 2.84131e-5,
            "cubic mile [mi³]": 6.79395e-6,
            "cubic meter [m³]": 0.0000284131,
            "cubic yard [yd³]": 0.0000353147,
            "cubic foot [ft³]": 0.000957506,
            "cubic decimeter [dm³]": 0.0284131,
            "gallon (US)": 0.00625,
            "gallon (UK)": 0.00595238,
            "liter [L]": 0.0284131,
            "cubic inch [in³]": 0.568261,
            "fluid ounce [fl oz (US)]": 0.96076036,
            "cubic centimeter [cm³]": 28.4131,
            "milliliter [mL]": 28.4131,
            "fluid ounce [fl oz (UK)]": 1
        },
        "cubic centimeter [cm³]": {
            "cubic kilometer [km³]": 1e-15,
            "cubic mile [mi³]": 2.39912e-14,
            "cubic meter [m³]": 1e-6,
            "cubic yard [yd³]": 1.30795e-6,
            "cubic foot [ft³]": 3.53147e-5,
            "cubic decimeter [dm³]": 0.001,
            "gallon (US)": 0.000264172,
            "gallon (UK)": 0.000219969,
            "liter [L]": 0.001,
            "cubic inch [in³]": 0.0610237,
            "fluid ounce [fl oz (US)]": 0.033814,
            "fluid ounce [fl oz (UK)]": 0.0351951,
            "milliliter [mL]": 1,
            "cubic centimeter [cm³]": 1
        },
        "milliliter [mL]": {
            "cubic kilometer [km³]": 1e-15,
            "cubic mile [mi³]": 2.39912e-14,
            "cubic meter [m³]": 1e-6,
            "cubic yard [yd³]": 1.30795e-6,
            "cubic foot [ft³]": 3.53147e-5,
            "cubic decimeter [dm³]": 0.001,
            "gallon (US)": 0.000264172,
            "gallon (UK)": 0.000219969,
            "liter [L]": 0.001,
            "cubic inch [in³]": 0.0610237,
            "fluid ounce [fl oz (US)]": 0.033814,
            "fluid ounce [fl oz (UK)]": 0.0351951,
            "cubic centimeter [cm³]": 1,
            "milliliter [mL]": 1
        }
    }

    factor = V_conversion_factors.get(input_unit, {}).get(output_unit, 1)
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

theme_s = ctk.get_appearance_mode()

def copy_to_clipboard():
    window.clipboard_clear()
    window.clipboard_append(output_box_text.get())

#this is the button that will change the theme of the app
def change_theme():
    theme = ctk.get_appearance_mode()
    if theme == "Dark":
        ctk.set_appearance_mode("light")
        theme_s = ctk.get_appearance_mode()
    else:
        ctk.set_appearance_mode("dark")
        theme_s = ctk.get_appearance_mode()


theme = ctk.get_appearance_mode()
theme_button = ctk.CTkButton(window, textvariable=theme, command=change_theme, width=10, height=1, font=("Arial", 14), text= theme_s)
theme_button.place(x=200, y=250)

#this is where the user can see the result of the conversion
output_box_text = ctk.StringVar()
output_box = ctk.CTkEntry(window, width=130, font=("Arial", 14), textvariable=output_box_text)
#disabling the Entry so that the user cant input anything in it
output_box.configure(state="disabled")
output_box.place(x=360, y=150)

#this is where the user is supposed to write his unit he wants converted
entryInt = tk.DoubleVar()
input_box = ctk.CTkEntry(window, width=130, font=("Arial", 14),  textvariable = entryInt)
#set the input type to number only
input_box.configure(validate="key")
input_box.configure(validatecommand=(input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.place(x=175, y=150)


#this button frame is where all the buttons are located which are used for manoeuvring through the app
sidebar = ctk.CTkFrame(window, fg_color=("darkgrey","black"), corner_radius=0)
sidebar.rowconfigure(0, weight=1)
sidebar.rowconfigure(1, weight=1)
sidebar.rowconfigure(2, weight=1)
sidebar.rowconfigure(3, weight=1)
sidebar.columnconfigure(0, weight=1)
sidebar.pack(side="left", fill="y")

#Temperature
#This is where all the widgets regarding the Temperature section are

T_Label = ctk.CTkLabel(window, text="Temperature", font=("Arial", 26), text_color=("black", "white"), bg_color=("darkgrey", "black") )
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
#This is where all the widgets regarding the Volume section are

V_Label = ctk.CTkLabel(window, text="Volume", font=("Arial", 26), text_color="white", bg_color="black")

V_convert_button = ctk.CTkButton(window, text="Convert", font=("Arial", 16), command=V_convert)

V_select_input = customtkinter.CTkOptionMenu(window, values=["cubic kilometer [km³]",
                                                             "cubic mile [mi³]",
                                                             "cubic meter [m³]",
                                                             "cubic yard [yd³]",
                                                                
                                                             "cubic decimeter [dm³]",    
                                                             "gallon (US)",    
                                                             "gallon (UK)",    
                                                             "liter [L]",    
                                                             "cubic inch [in³]",    
                                                             "fluid ounce [fl oz (US)]",    
                                                             "fluid ounce [fl oz (UK)]",    
                                                             "cubic centimeter [cm³]",    
                                                             "milliliter [mL]"], width=130)
V_select_output = customtkinter.CTkOptionMenu(window, values=["cubic kilometer [km³]",
                                                             "cubic mile [mi³]",
                                                             "cubic meter [m³]",
                                                             "cubic yard [yd³]",
                                                                
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

copy_button = customtkinter.CTkButton(window, text="copy", font=("Airal", 11), width=1, command=copy_to_clipboard)
copy_button.place(x=495, y=150)

window.mainloop()