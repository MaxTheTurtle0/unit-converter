#Temperature dictionaries

t_values = ["Celsius [°C]", 
            "Fahrenheit [°F]", 
            "kelvin [K]"]

t_conversion_factors = {
        "Celsius [°C]": {"Fahrenheit [°F]": lambda x: x * 1.8 + 32, "kelvin [K]": lambda x: x + 273.15},
        "Fahrenheit [°F]": {"Celsius [°C]": lambda x: (x - 32) / 1.8, "kelvin [K]": lambda x: (x + 459.67) * 5/9},
        "kelvin [K]": {"Celsius [°C]": lambda x: x - 273.15, "Fahrenheit [°F]": lambda x: x * 9/5 - 459.67},
    }

#Length dictionaries

l_values = ["centimeter [cm]", 
            "decimeter [dm]", 
            "meter [m]", 
            "kilometer [km]", 
            "inch [in]", 
            "foot [ft]", 
            "yard [yd]", 
            "mile [mi]"]

l_conversion_factors = {
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

#Area dictionaries

a_values = ["square centimeter [cm²]", 
            "square decimetre [dm²]", 
            "square meter [m²]", 
            "square decametre [dam²]",
            "square hectometre [hm²]", 
            "square kilometer [km²]", 
            "square inch [in²]", 
            "square foot [ft²]", 
            "square yard [yd²]", 
            "square mile [mi²]",
            "acre"]

a_conversion_factors = {
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

#Volume dictionaries

v_values = ["cubic kilometer [km³]",
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
            "milliliter [mL]"]

v_conversion_factors = {
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

#Mass dictionaries

m_values = ["miligram [mg]",
            "gram [g]",
            "kilogram [kg]",
            "ton [t]",
            "pound [lb]",
            "ounce [oz]",
            "stone [st]",
            "ton long [ton (UK)]",
            "ton short [ton (US)]"]

m_conversion_factors = {
        "miligram [mg]": {
            "gram [g]": 0.001,
            "kilogram [kg]": 1e-6,	
            "ton [t]": 1e-9,
            "pound [lb]": 2.20462e-6,
            "ounce [oz]": 3.5274e-5,
            "stone [st]": 1.57473e-7,
            "ton long [ton (UK)]": 9.84207e-10,
            "ton short [ton (US)]": 1.10231e-9,
            "miligram [mg]": 1,
        },
        "gram [g]": {
            "miligram [mg]": 1000,
            "kilogram [kg]": 0.001,
            "ton [t]": 1e-6,
            "pound [lb]": 0.00220462,
            "ounce [oz]": 0.035274,
            "stone [st]": 1.57473e-5,
            "ton long [ton (UK)]": 9.84207e-8,
            "ton short [ton (US)]": 1.10231e-7,
            "gram [g]": 1
        },

        "kilogram [kg]": {
            "miligram [mg]": 1000000,
            "gram [g]": 1000,
            "ton [t]": 0.001,
            "pound [lb]": 2.20462,
            "ounce [oz]": 35.274,
            "stone [st]": 0.157473,
            "ton long [ton (UK)]": 9.84207e-5,
            "ton short [ton (US)]": 0.00110231,
            "kilogram [kg]": 1
        },

        "ton [t]": {
            "miligram [mg]": 1000000000,
            "gram [g]": 1000000,
            "kilogram [kg]": 1000,
            "pound [lb]": 2204.62,
            "ounce [oz]": 35274,
            "stone [st]": 157.473,
            "ton long [ton (UK)]": 0.984207,
            "ton short [ton (US)]": 1.10231,
            "ton [t]": 1
        },

        "pound [lb]": {
            "miligram [mg]": 453592,
            "gram [g]": 453.592,
            "kilogram [kg]": 0.453592,
            "ton [t]": 0.000453592,
            "ounce [oz]": 16,
            "stone [st]": 0.0714286,
            "ton long [ton (UK)]": 0.000446429,
            "ton short [ton (US)]": 0.0005,
            "pound [lb]": 1
        },

        "ounce [oz]": {
            "miligram [mg]": 28349.5,
            "gram [g]": 28.3495,
            "kilogram [kg]": 0.0283495,
            "ton [t]": 2.835e-5,
            "pound [lb]": 0.0625,
            "stone [st]": 0.00446429,
            "ton long [ton (UK)]": 2.79082e-5,
            "ton short [ton (US)]": 3.125e-5,
            "ounce [oz]": 1
        },

        "stone [st]": {
            "miligram [mg]": 6350293,
            "gram [g]": 6350.29,
            "kilogram [kg]": 6.35029,
            "ton [t]": 0.00635029,
            "pound [lb]": 14,
            "ounce [oz]": 224,
            "ton long [ton (UK)]": 0.00625,
            "ton short [ton (US)]": 0.007,
            "stone [st]": 1
        },

        "ton long [ton (UK)]": {
            "miligram [mg]": 1016047000,
            "gram [g]": 1016047,
            "kilogram [kg]": 1016.05,
            "ton [t]": 1.01605,
            "pound [lb]": 2240,
            "ounce [oz]": 35840,
            "stone [st]": 160,
            "ton short [ton (US)]": 1.12,
            "ton long [ton (UK)]": 1
        },

        "ton short [ton (US)]": {
            "miligram [mg]": 907184740,
            "gram [g]": 907184.74,
            "kilogram [kg]": 907.185,
            "ton [t]": 0.907185,
            "pound [lb]": 2000,
            "ounce [oz]": 32000,
            "stone [st]": 142.857,
            "ton long [ton (UK)]": 0.892857,
            "ton short [ton (US)]": 1
        }
    }

#Time dictionaries

ti_values = ["picosecond [ps]",
             "nanosecond [ns]", 
             "microsecond [µs]", 
             "milisecond [ms]", 
             "second [s]", 
             "minute [min]", 
             "hour [h]", 
             "day [d]", 
             "week [wk]", 
             "month [mo]", 
             "year [yr]"]

ti_conversion_factors = {
        "picosecond [ps]": {
            "nanosecond [ns]": 0.001,
            "microsecond [µs]": 1e-6,
            "milisecond [ms]": 1e-9,
            "second [s]": 1e-12,
            "minute [min]": 1.66667e-14,
            "hour [h]": 2.77778e-16,
            "day [d]": 1.15741e-17,
            "week [wk]": 1.65344e-18,
            "month [mo]": 3.80517e-19,
            "year [yr]": 3.171e-20,
            "picosecond [ps]": 1
        },

        "nanosecond [ns]": {
            "picosecond [ps]": 1000,
            "microsecond [µs]": 0.001,
            "milisecond [ms]": 1e-6,
            "second [s]": 1e-9,
            "minute [min]": 1.66667e-11,
            "hour [h]": 2.77778e-13,
            "day [d]": 1.15741e-14,
            "week [wk]": 1.65344e-15,
            "month [mo]": 3.80517e-16,
            "year [yr]": 3.171e-17,
            "nanosecond [ns]": 1
        },

        "microsecond [µs]": {
            "picosecond [ps]": 1000000,
            "nanosecond [ns]": 1000,
            "milisecond [ms]": 0.001,
            "second [s]": 1e-6,
            "minute [min]": 1.66667e-8,
            "hour [h]": 2.77778e-10,
            "day [d]": 1.15741e-11,
            "week [wk]": 1.65344e-12,
            "month [mo]": 3.80517e-13,
            "year [yr]": 3.171e-14,
            "microsecond [µs]": 1
        },

        "milisecond [ms]": {
            "picosecond [ps]": 1000000000,
            "nanosecond [ns]": 1000000,
            "microsecond [µs]": 1000,
            "second [s]": 0.001,
            "minute [min]": 1.66667e-5,
            "hour [h]": 2.77778e-7,
            "day [d]": 1.15741e-8,
            "week [wk]": 1.65344e-9,
            "month [mo]": 3.80517e-10,
            "year [yr]": 3.171e-11,
            "milisecond [ms]": 1
        },

        "second [s]": {
            "picosecond [ps]": 1000000000000,
            "nanosecond [ns]": 1000000000,
            "microsecond [µs]": 1000000,
            "milisecond [ms]": 1000,
            "minute [min]": 0.0166667,
            "hour [h]": 0.000277778,
            "day [d]": 1.15741e-5,
            "week [wk]": 1.65344e-6,
            "month [mo]": 3.80517e-7,
            "year [yr]": 3.171e-8,
            "second [s]": 1
        },

        "minute [min]": {
            "picosecond [ps]": 60000000000000,
            "nanosecond [ns]": 60000000000,
            "microsecond [µs]": 60000000,
            "milisecond [ms]": 60000,
            "second [s]": 60,
            "hour [h]": 0.0166667,
            "day [d]": 0.000694444,
            "week [wk]": 9.9206e-5,
            "month [mo]": 2.28311e-5,
            "year [yr]": 1.9026e-6,
            "minute [min]": 1
        },

        "hour [h]": {
            "picosecond [ps]": 3600000000000000,
            "nanosecond [ns]": 3600000000000,
            "microsecond [µs]": 3600000000,
            "milisecond [ms]": 3600000,
            "second [s]": 3600,
            "minute [min]": 60,
            "day [d]": 0.0416667,
            "week [wk]": 0.00595238,
            "month [mo]": 0.00136895,
            "year [yr]": 0.000114079,
            "hour [h]": 1
        },

        "day [d]": {
            "picosecond [ps]": 86400000000000000,
            "nanosecond [ns]": 86400000000000,
            "microsecond [µs]": 86400000000,
            "milisecond [ms]": 86400000,
            "second [s]": 86400,
            "minute [min]": 1440,
            "hour [h]": 24,
            "week [wk]": 0.142857,
            "month [mo]": 0.0328767,
            "year [yr]": 0.00273973,
            "day [d]": 1
        },

        "week [wk]": {
            "picosecond [ps]": 604800000000000000,
            "nanosecond [ns]": 604800000000000,
            "microsecond [µs]": 604800000000,
            "milisecond [ms]": 604800000,
            "second [s]": 604800,
            "minute [min]": 10080,
            "hour [h]": 168,
            "day [d]": 7,
            "month [mo]": 0.230137,
            "year [yr]": 0.0191781,
            "week [wk]": 1
        },

        "month [mo]": {
            "picosecond [ps]": 2628000000000000000,
            "nanosecond [ns]": 2628000000000000,
            "microsecond [µs]": 2628000000000,
            "milisecond [ms]": 2628000000,
            "second [s]": 2628000,
            "minute [min]": 43800,
            "hour [h]": 730.001,
            "day [d]": 30.4167,
            "week [wk]": 4.34524,
            "year [yr]": 0.0833333,
            "month [mo]": 1
        },

        "year [yr]": {
            "picosecond [ps]": 31540000000000000000,
            "nanosecond [ns]": 31540000000000000,
            "microsecond [µs]": 31540000000000,
            "milisecond [ms]": 31540000000,
            "second [s]": 31540000,
            "minute [min]": 525600,
            "hour [h]": 8760,
            "day [d]": 365,
            "week [wk]": 52.1429,
            "month [mo]": 12,
            "year [yr]": 1
        }
    }


#Pressure dictionaries

p_values = [
    "bar [bar]",
    "pascal [Pa]",
    "kilopascal [kPa]",
    "megapascal [MPa]",
    "atmosphere [atm]",
    "millibar [mbar]",
    "hectopascal [hPa]"
]

p_conversion_factors = {
    "bar [bar]": {
        "bar [bar]": 1,
        "pascal [Pa]": 100000,
        "kilopascal [kPa]": 100,
        "megapascal [MPa]": 0.1,
        "atmosphere [atm]": 0.986923,
        "millibar [mbar]": 1000,
        "hectopascal [hPa]": 1000,
    },

    "pascal [Pa]": {
        "bar [bar]": 1e-5,
        "pascal [Pa]": 1,
        "kilopascal [kPa]": 0.001,
        "megapascal [MPa]": 1e-6,
        "atmosphere [atm]": 9.86923e-6,
        "millibar [mbar]": 0.01,
        "hectopascal [hPa]": 0.01,
    },

    "kilopascal [kPa]": {
        "bar [bar]": 0.01,
        "pascal [Pa]": 1000,
        "kilopascal [kPa]": 1,
        "megapascal [MPa]": 0.001,
        "atmosphere [atm]": 0.00986923,
        "millibar [mbar]": 10,
        "hectopascal [hPa]": 10,
    },
    
    "megapascal [MPa]": {
        "bar [bar]": 10,
        "pascal [Pa]": 1000000,
        "kilopascal [kPa]": 1000,
        "megapascal [MPa]": 1,
        "atmosphere [atm]": 9.86923,
        "millibar [mbar]": 10000,
        "hectopascal [hPa]": 10000,
    },

    "atmosphere [atm]": {
        "bar [bar]": 1.01325,
        "pascal [Pa]": 101325,
        "kilopascal [kPa]": 101.325,
        "megapascal [MPa]": 0.101325,
        "atmosphere [atm]": 1,
        "millibar [mbar]": 1013.25,
        "hectopascal [hPa]": 1013.25,
    },

    "millibar [mbar]": {
        "bar [bar]": 0.001,
        "pascal [Pa]": 100,
        "kilopascal [kPa]": 0.1,
        "megapascal [MPa]": 0.0001,
        "atmosphere [atm]": 0.000986923,
        "millibar [mbar]": 1,
        "hectopascal [hPa]": 1,
    },

    "hectopascal [hPa]": {
        "bar [bar]": 0.001,
        "pascal [Pa]": 100,
        "kilopascal [kPa]": 0.1,
        "megapascal [MPa]": 0.0001,
        "atmosphere [atm]": 0.000986923,
        "millibar [mbar]": 1,
        "hectopascal [hPa]": 1,
    }
}