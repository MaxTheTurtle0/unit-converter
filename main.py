import tkinter as tk
import customtkinter as ctk
import customtkinter
import pyperclip

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
        ("centimeter [cm]", "centimeter [cm]"): 1,
        ("decimeter [dm]", "meter [m]"): 0.1,
        ("decimeter [dm]", "kilometer [km]"): 0.0001,
        ("decimeter [dm]", "inch [in]"): 3.93701,
        ("decimeter [dm]", "foot [ft]"): 0.328084,
        ("decimeter [dm]", "yard [yd]"): 0.109361,
        ("decimeter [dm]", "mile [mi]"): 0.0000621371,
        ("decimeter [dm]", "centimeter [cm]"): 10,
        ("decimeter [dm]", "decimeter [dm]"): 1,
        ("meter [m]", "kilometer [km]"): 0.001,
        ("meter [m]", "inch [in]"): 39.3701,
        ("meter [m]", "foot [ft]"): 3.28084,
        ("meter [m]", "yard [yd]"): 1.09361,
        ("meter [m]", "mile [mi]"): 0.000621371,
        ("meter [m]", "centimeter [cm]"): 100,
        ("meter [m]", "decimeter [dm]"): 10, 
        ("meter [m]", "meter [m]"): 1,
        ("kilometer [km]", "inch [in]"): 39370.1,
        ("kilometer [km]", "foot [ft]"): 3280.84,
        ("kilometer [km]", "yard [yd]"): 1093.61,
        ("kilometer [km]", "mile [mi]"): 0.621371,
        ("kilometer [km]", "centimeter [cm]"): 1000000,
        ("kilometer [km]", "decimeter [dm]"): 10000,
        ("kilometer [km]", "meter [m]"): 1000,
        ("kilometer [km]", "kilometer [km]"): 1,
        ("inch [in]", "kilometer [km]"): 0.0000254,
        ("inch [in]", "meter [m]"): 0.0254,
        ("inch [in]", "decimeter [dm]"): 0.254,
        ("inch [in]", "centimeter [cm]"): 2.54,
        ("inch [in]", "foot [ft]"): 0.0833333,
        ("inch [in]", "yard [yd]"): 0.0277778,
        ("inch [in]", "mile [mi]"): 0.0000157828,
        ("inch [in]", "inch [in]"): 1,
        ("foot [ft]", "kilometer [km]"): 0.0003048,
        ("foot [ft]", "meter [m]"): 0.3048,
        ("foot [ft]", "decimeter [dm]"): 3.048,
        ("foot [ft]", "centimeter [cm]"): 30.48,
        ("foot [ft]", "yard [yd]"): 0.333333,
        ("foot [ft]", "yard [yd]"): 0.333333,
        ("foot [ft]", "mile [mi]"): 0.000189394,
        ("foot [ft]", "inch [in]"): 12,
        ("foot [ft]", "foot [ft]"): 1,
        ("yard [yd]", "kilometer [km]"): 0.0009144,
        ("yard [yd]", "meter [m]"): 0.9144,
        ("yard [yd]", "decimeter [dm]"): 9.144,
        ("yard [yd]", "centimeter [cm]"): 91.44,
        ("yard [yd]", "foot [ft]"): 3,
        ("yard [yd]", "inch [in]"): 36,
        ("yard [yd]", "mile [mi]"): 0.000568182,
        ("yard [yd]", "yard [yd]"): 1,
        ("mile [mi]", "kilometer [km]"): 1.609344,
        ("mile [mi]", "meter [m]"): 1609.344,
        ("mile [mi]", "decimeter [dm]"): 16093.44,
        ("mile [mi]", "centimeter [cm]"): 160934.4,
        ("mile [mi]", "foot [ft]"): 5280,
        ("mile [mi]", "inch [in]"): 36,
        ("mile [mi]", "yard [yd]"): 1760,
        ("mile [mi]", "mile [mi]"): 1
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

                        ("cubic mile [mi³]", "cubic kilometer [km³]"): 4.16818,
                        ("cubic mile [mi³]", "cubic meter [m³]"): 4.16818e+12,
                        ("cubic mile [mi³]", "barrel (US)"): 1.10169e+10,
                        ("cubic mile [mi³]", "barrel (UK)"): 9.82494e+9,
                        ("cubic mile [mi³]", "cubic yard [yd³]"): 2.14335e+12,
                        ("cubic mile [mi³]", "cubic foot [ft³]"): 5.76456e+13,
                        ("cubic mile [mi³]", "cubic decimeter [dm³]"): 4.16818e+15,
                        ("cubic mile [mi³]", "gallon (US)"): 1.09779e+11,
                        ("cubic mile [mi³]", "gallon (UK)"): 9.19318e+10,
                        ("cubic mile [mi³]", "liter [L]"): 4.16818e+12,
                        ("cubic mile [mi³]", "cubic inch [in³]"): 2.51986e+14,
                        ("cubic mile [mi³]", "fluid ounce [fl oz (US)]"): 3.47827e+11,
                        ("cubic mile [mi³]", "fluid ounce [fl oz (UK)]"): 2.89183e+11,
                        ("cubic mile [mi³]", "cubic centimeter [cm³]"): 4.16818e+21,
                        ("cubic mile [mi³]", "milliliter [mL]"): 4.16818e+18,
                        ("cubic mile [mi³]", "cubic mile [mi³]"): 1,

                        ("cubic meter [m³]", "cubic kilometer [km³]"): 1e-9,
                        ("cubic meter [m³]", "cubic mile [mi³]"): 2.3991e-10,
                        ("cubic meter [m³]", "barrel (US)"): 6.28981,
                        ("cubic meter [m³]", "barrel (UK)"): 5.61171,
                        ("cubic meter [m³]", "cubic yard [yd³]"): 1.30795,
                        ("cubic meter [m³]", "cubic foot [ft³]"): 35.3147,
                        ("cubic meter [m³]", "cubic decimeter [dm³]"): 1000,
                        ("cubic meter [m³]", "gallon (US)"): 264.172,
                        ("cubic meter [m³]", "gallon (UK)"): 219.912,
                        ("cubic meter [m³]", "liter [L]"): 1000,
                        ("cubic meter [m³]", "cubic inch [in³]"): 61023.7,
                        ("cubic meter [m³]", "fluid ounce [fl oz (US)]"): 33814,
                        ("cubic meter [m³]", "fluid ounce [fl oz (UK)]"): 35195,
                        ("cubic meter [m³]", "cubic centimeter [cm³]"): 1e+6,
                        ("cubic meter [m³]", "milliliter [mL]"): 1e+6,
                        ("cubic meter [m³]", "cubic meter [m³]"): 1,
                        
                        ("barrel (US)", "cubic kilometer [km³]"): 1.58987e-10,
                        ("barrel (US)", "cubic mile [mi³]"): 1.58987e-9,
                        ("barrel (US)", "cubic meter [m³]"): 0.158987,
                        ("barrel (US)", "barrel (UK)"): 0.832674,
                        ("barrel (US)", "cubic yard [yd³]"): 0.00413323,
                        ("barrel (US)", "cubic foot [ft³]"): 0.0238095,
                        ("barrel (US)", "cubic decimeter [dm³]"): 0.158987,
                        ("barrel (US)", "gallon (US)"): 42,
                        ("barrel (US)", "gallon (UK)"): 34.9723,
                        ("barrel (US)", "liter [L]"): 158.987,
                        ("barrel (US)", "cubic inch [in³]"): 9702.83,
                        ("barrel (US)", "fluid ounce [fl oz (US)]"): 5376,
                        ("barrel (US)", "fluid ounce [fl oz (UK)]"): 4480.4,
                        ("barrel (US)", "cubic centimeter [cm³]"): 158987,
                        ("barrel (US)", "milliliter [mL]"): 158987,
                        ("barrel (US)", "barrel (US)"): 1,

                        ("barrel (UK)", "cubic kilometer [km³]"): 1.78002e-10,
                        ("barrel (UK)", "cubic mile [mi³]"): 2.02816e-11,
                        ("barrel (UK)", "cubic meter [m³]"): 0.158987,
                        ("barrel (UK)", "cubic yard [yd³]"): 0.00476188,
                        ("barrel (UK)", "cubic foot [ft³]"): 0.163659,
                        ("barrel (UK)", "cubic decimeter [dm³]"): 158.987,
                        ("barrel (UK)", "gallon (US)"): 42,
                        ("barrel (UK)", "gallon (UK)"): 34.9723,
                        ("barrel (UK)", "liter [L]"): 158.987,
                        ("barrel (UK)", "cubic inch [in³]"): 9702.69,
                        ("barrel (UK)", "fluid ounce [fl oz (US)]"): 5376,
                        ("barrel (UK)", "fluid ounce [fl oz (UK)]"): 5600,
                        ("barrel (UK)", "cubic centimeter [cm³]"): 158987.295,
                        ("barrel (UK)", "milliliter [mL]"): 158987.295,
                        ("barrel (UK)", "barrel (UK)"): 1,

                        ("cubic yard [yd³]", "cubic kilometer [km³]"): 7.64555e-10,
                        ("cubic yard [yd³]", "cubic mile [mi³]"): 8.73494e-11,
                        ("cubic yard [yd³]", "cubic meter [m³]"): 0.764555,
                        ("cubic yard [yd³]", "barrel (US)"): 201.974,
                        ("cubic yard [yd³]", "barrel (UK)"): 168.178,
                        ("cubic yard [yd³]", "cubic foot [ft³]"): 27,
                        ("cubic yard [yd³]", "cubic decimeter [dm³]"): 764.555,
                        ("cubic yard [yd³]", "gallon (US)"): 201.974,
                        ("cubic yard [yd³]", "gallon (UK)"): 168.178,
                        ("cubic yard [yd³]", "liter [L]"): 764.555,
                        ("cubic yard [yd³]", "cubic inch [in³]"): 46656,
                        ("cubic yard [yd³]", "fluid ounce [fl oz (US)]"): 25852.7,
                        ("cubic yard [yd³]", "fluid ounce [fl oz (UK)]"): 27008.6,
                        ("cubic yard [yd³]", "cubic centimeter [cm³]"): 7.64555e+5,
                        ("cubic yard [yd³]", "milliliter [mL]"): 7.64555e+5,
                        ("cubic yard [yd³]", "cubic yard [yd³]"): 1,

                        ("cubic foot [ft³]", "cubic kilometer [km³]"): 2.83168e-11,
                        ("cubic foot [ft³]", "cubic mile [mi³]"): 6.79357e-12,
                        ("cubic foot [ft³]", "cubic meter [m³]"): 0.0283168,
                        ("cubic foot [ft³]", "barrel (US)"): 0.178108,
                        ("cubic foot [ft³]", "barrel (UK)"): 0.158987,
                        ("cubic foot [ft³]", "cubic yard [yd³]"): 0.037037,
                        ("cubic foot [ft³]", "cubic decimeter [dm³]"): 28.3168,
                        ("cubic foot [ft³]", "gallon (US)"): 7.48052,
                        ("cubic foot [ft³]", "gallon (UK)"): 6.22884,
                        ("cubic foot [ft³]", "liter [L]"): 28.3168,
                        ("cubic foot [ft³]", "cubic inch [in³]"): 1728,
                        ("cubic foot [ft³]", "fluid ounce [fl oz (US)]"): 957.506,
                        ("cubic foot [ft³]", "fluid ounce [fl oz (UK)]"): 996.614,
                        ("cubic foot [ft³]", "cubic centimeter [cm³]"): 28316.8,
                        ("cubic foot [ft³]", "milliliter [mL]"): 28316.8,
                        ("cubic foot [ft³]", "cubic foot [ft³]"): 1,

                        ("cubic decimeter [dm³]", "cubic kilometer [km³]"): 1e-18,
                        ("cubic decimeter [dm³]", "cubic mile [mi³]"): 2.39912e-16,
                        ("cubic decimeter [dm³]", "cubic meter [m³]"): 0.001,
                        ("cubic decimeter [dm³]", "barrel (US)"): 0.00628981,
                        ("cubic decimeter [dm³]", "barrel (UK)"): 0.00561171,
                        ("cubic decimeter [dm³]", "cubic yard [yd³]"): 0.00130795,
                        ("cubic decimeter [dm³]", "cubic foot [ft³]"): 0.0353147,
                        ("cubic decimeter [dm³]", "gallon (US)"): 0.264172,
                        ("cubic decimeter [dm³]", "gallon (UK)"): 0.219912,
                        ("cubic decimeter [dm³]", "liter [L]"): 1,
                        ("cubic decimeter [dm³]", "cubic inch [in³]"): 0.0610237,
                        ("cubic decimeter [dm³]", "fluid ounce [fl oz (US)]"): 0.033814,
                        ("cubic decimeter [dm³]", "fluid ounce [fl oz (UK)]"): 0.0284131,
                        ("cubic decimeter [dm³]", "cubic centimeter [cm³]"): 1000,
                        ("cubic decimeter [dm³]", "milliliter [mL]"): 1000,
                        ("cubic decimeter [dm³]", "cubic decimeter [dm³]"): 1,

                        ("gallon (US)", "cubic kilometer [km³]"): 3.78541e-11,
                        ("gallon (US)", "cubic mile [mi³]"): 9.09473e-12,
                        ("gallon (US)", "cubic meter [m³]"): 0.00378541,
                        ("gallon (US)", "barrel (US)"): 0.0238095,
                        ("gallon (US)", "barrel (UK)"): 0.0269817,
                        ("gallon (US)", "cubic yard [yd³]"): 0.00576456,
                        ("gallon (US)", "cubic foot [ft³]"): 0.133681,
                        ("gallon (US)", "gallon (UK)"): 0.83267382,
                        ("gallon (US)", "cubic decimeter [dm³]"): 3.78541,
                        ("gallon (US)", "liter [L]"): 3.78541,
                        ("gallon (US)", "cubic inch [in³]"): 231,
                        ("gallon (US)", "fluid ounce [fl oz (US)]"): 128,
                        ("gallon (US)", "fluid ounce [fl oz (UK)]"): 153.722,
                        ("gallon (US)", "cubic centimeter [cm³]"): 3785.41,
                        ("gallon (US)", "milliliter [mL]"): 3785.41,
                        ("gallon (US)", "gallon (US)"): 1,

                        ("gallon (UK)", "cubic kilometer [km³]"): 4.54609e-13,
                        ("gallon (UK)", "cubic mile [mi³]"): 1.20095e-12,
                        ("gallon (UK)", "cubic meter [m³]"): 0.00454609,
                        ("gallon (UK)", "barrel (US)"): 0.0238095,
                        ("gallon (UK)", "barrel (UK)"): 0.0211868,
                        ("gallon (UK)", "cubic yard [yd³]"): 0.00163961,
                        ("gallon (UK)", "cubic foot [ft³]"): 0.160543,
                        ("gallon (UK)", "cubic decimeter [dm³]"): 4.54609,
                        ("gallon (UK)", "gallon (US)"): 1.20095,
                        ("gallon (UK)", "liter [L]"): 4.54609,
                        ("gallon (UK)", "cubic inch [in³]"): 277.419,
                        ("gallon (UK)", "fluid ounce [fl oz (US)]"): 153.722,
                        ("gallon (UK)", "fluid ounce [fl oz (UK)]"): 160,
                        ("gallon (UK)", "cubic centimeter [cm³]"): 4546.09,
                        ("gallon (UK)", "milliliter [mL]"): 4546.09,
                        ("gallon (UK)", "gallon (UK)"): 1,

                        ("liter [L]", "cubic kilometer [km³]"): 1e-12,
                        ("liter [L]", "cubic mile [mi³]"): 2.39912e-13,
                        ("liter [L]", "cubic meter [m³]"): 0.001,
                        ("liter [L]", "barrel (US)"): 0.023810,
                        ("liter [L]", "barrel (UK)"): 0.0284131,
                        ("liter [L]", "cubic yard [yd³]"): 0.764555,
                        ("liter [L]", "cubic foot [ft³]"): 28.3168,
                        ("liter [L]", "cubic decimeter [dm³]"): 1,
                        ("liter [L]", "gallon (US)"): 0.264172,
                        ("liter [L]", "gallon (UK)"): 0.219969,
                        ("liter [L]", "cubic inch [in³]"): 0.0610237,
                        ("liter [L]", "fluid ounce [fl oz (US)]"): 33.814,
                        ("liter [L]", "fluid ounce [fl oz (UK)]"): 35.1951,
                        ("liter [L]", "cubic centimeter [cm³]"): 1000,
                        ("liter [L]", "milliliter [mL]"): 1000,
                        ("liter [L]", "liter [L]"): 1
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

def copy_to_clipboard():
    pyperclip.copy(output_box_text.get())

#this is where the user can see the result of the conversion
output_box_text = ctk.StringVar()
output_box = ctk.CTkEntry(window, width=130, font=("Arial", 14), textvariable=output_box_text)
#disabling the Entry so that the user cant input anything in it
output_box.configure(state="disabled")
output_box.place(x=360, y=150)

#this is where the user is supposed to write his unit he wants converted
entryInt = tk.IntVar()
input_box = ctk.CTkEntry(window, width=130, font=("Arial", 14),  textvariable = entryInt)
#set the input type to number only
input_box.configure(validate="key")
input_box.configure(validatecommand=(input_box.register(lambda val: val.isdigit() or val == "." or val == "-"), '%S'))
input_box.place(x=175, y=150)


#this button frame is where all the buttons are located which are used for manoeuvring through the app
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
#This is where all the widgets regarding the Volume section are

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
                                                             "milliliter [mL]"], width=130)
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

copy_button = customtkinter.CTkButton(window, text="copy", font=("Airal", 11), width=1, command=copy_to_clipboard)
copy_button.place(x=495, y=150)


window.mainloop()