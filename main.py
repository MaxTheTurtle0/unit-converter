import tkinter as tk

window = tk.Tk()
window.title("Unit Converter")
window.geometry("700x300")

#this is so that the user knows what unit he is converting
T = tk.Label(window, text="Temperature", font=("Arial", 24))
T.pack(pady=20)

#this is where the user is supposed to write his unit he wants converted
input_box = tk.Entry(window, width=12, font=("Arial", 14))
input_box.pack(side="left", padx="20", pady="20")

#this button frame is where all the buttons are which are used for manoeuvring through the app
buttonframe = tk.Frame(window)
buttonframe.rowconfigure(0, weight=1)
buttonframe.rowconfigure(1, weight=1)
buttonframe.rowconfigure(2, weight=1)
buttonframe.rowconfigure(3, weight=1)
buttonframe.columnconfigure(0, weight=1)

#these buttons changing to the unit which you want to convert(Temperature, Length, Area, Volume)
T_button = tk.Button(buttonframe, text="Temperature", font=("Arial", 16))
T_button.grid(row=0, column=0, sticky="nsew")


L_button = tk.Button(buttonframe, text="Length", font=("Arial", 16))
L_button.grid(row=1, column=0, sticky="nsew")

A_button = tk.Button(buttonframe, text="Area", font=("Arial", 16))
A_button.grid(row=2, column=0, sticky="nsew")

V_button = tk.Button(buttonframe, text="Volume", font=("Arial", 16))
V_button.grid(row=3, column=0, sticky="nsew")

buttonframe.pack(fill="both", expand=True, side="left", padx=20, pady=20, anchor="nw")

window.mainloop()