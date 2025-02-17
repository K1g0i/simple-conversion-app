
import customtkinter as ctk

class UnitConverterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Unit Converter")
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="Select Conversion Type", font=("Arial", 20))
        self.label.pack(pady=20)

        self.weight_button = ctk.CTkButton(self, text="Weight", command=self.open_weight_converter)
        self.weight_button.pack(pady=10, fill="x", padx=50)

        self.length_button = ctk.CTkButton(self, text="Length", command=self.open_length_converter)
        self.length_button.pack(pady=10, fill="x", padx=50)

        self.speed_button = ctk.CTkButton(self, text="Speed", command=self.open_speed_converter)
        self.speed_button.pack(pady=10, fill="x", padx=50)

        self.temperature_button = ctk.CTkButton(self, text="Temperature", command=self.open_temperature_converter)
        self.temperature_button.pack(pady=10, fill="x", padx=50)

    def open_weight_converter(self):
        WeightConverter(self)

    def open_length_converter(self):
        LengthConverter(self)

    def open_speed_converter(self):
        SpeedConverter(self)

    def open_temperature_converter(self):
        TemperatureConverter(self)

class WeightConverter(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Weight Converter")
        self.geometry("300x400")
        self.label = ctk.CTkLabel(self, text="Weight Converter", font=("Arial", 18))
        self.label.pack(pady=20)

        self.from_label = ctk.CTkLabel(self, text= "From:")
        self.from_label.pack()

        self.from_combobox = ctk.CTkComboBox(self, values=["Kilograms (Kg)", "Pounds (lb)", "Grams"])
        self.from_combobox.pack(pady=5)
        self.from_combobox.set("Kilograms (Kg)")

        self.input_label = ctk.CTkLabel(self, text="Enter Value: ")
        self.input_label.pack()

        self.input_entry = ctk.CTkEntry(self)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<KeyRelease>", self.calculate_result)

        self.to_label = ctk.CTkLabel(self, text="To:")
        self.to_label.pack()

        self.to_combobox = ctk.CTkComboBox(self, values=["Kilograms (Kg)", "Pounds (lb)", "Grams"])
        self.to_combobox.pack(pady=5)
        self.to_combobox.set("Pounds (lb)")

        self.result_label=ctk.CTkLabel(self, text="Result:")
        self.result_label.pack()

        self.result_value = ctk.CTkLabel(self, text="0.0", font=("Arial", 16))
        self.result_value.pack(pady=5)


    def calculate_result(self, event=None):
        try:
            from_unit = self.from_combobox.get()
            to_unit = self.to_combobox.get()
            value = float(self.input_entry.get())

            conversion_factors = {
                ("Kilograms (Kg)", "Pounds (lb)"): 2.20462,
                ("Kilograms (Kg)", "Grams"): 1000,
                ("Pounds (lb)", "Kilograms (Kg)"): 0.453592,
                ("Pounds (lb)", "Grams"): 453.592,
                ("Grams", "Kilograms (Kg)"): 0.001,
                ("Grams", "Pounds (lb)"): 0.00220462
            }

            if from_unit == to_unit:
                result = value
            else:
                result = value * conversion_factors.get((from_unit, to_unit), 1)

            self.result_value.configure(text=f"{result:.2f}")
        except ValueError:
            self.result_value.configure(text="Invalid input")

        

class LengthConverter(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Length Converter")
        self.geometry("300x400")
        label = ctk.CTkLabel(self, text="Length Converter", font=("Arial", 18))
        label.pack(pady=20)

        self.from_label = ctk.CTkLabel(self, text= "From:")
        self.from_label.pack()

        self.from_combobox = ctk.CTkComboBox(self, values=["Metres (m)", "Kilometres (km)", "Miles (mi)", "Feet (ft)"])
        self.from_combobox.pack(pady=5)
        self.from_combobox.set("Metres (m)")

        self.input_label = ctk.CTkLabel(self, text="Enter Value: ")
        self.input_label.pack()

        self.input_entry = ctk.CTkEntry(self)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<KeyRelease>", self.calculate_result)

        self.to_label = ctk.CTkLabel(self, text="To:")
        self.to_label.pack()

        self.to_combobox = ctk.CTkComboBox(self, values=["Metres (m)", "Kilometres (km)", "Miles (mi)", "Feet (ft)"])
        self.to_combobox.pack(pady=5)
        self.to_combobox.set("Miles (mi)")

        self.result_label=ctk.CTkLabel(self, text="Result:")
        self.result_label.pack()

        self.result_value = ctk.CTkLabel(self, text="0.0", font=("Arial", 16))
        self.result_value.pack(pady=5)


    def calculate_result(self, event=None):
        try:
            from_unit = self.from_combobox.get()
            to_unit = self.to_combobox.get()
            value = float(self.input_entry.get())

            conversion_factors = {
                ("Metres (m)", "Kilometres (km)"): 0.001,
                ("Metres (m)", "Miles (mi)"): 0.000621371,
                ("Metres (m)", "Feet (ft)"): 3.28084,
                ("Kilometres (km)", "Meters (m)"): 1000,
                ("Kilometres (km)", "Miles (mi)"): 0.621371,
                ("Kilometres (km)", "Feet (ft)"): 3280.84,
                ("Miles (mi)", "Metres (m)"): 1609.34,
                ("Miles (mi)", "Kilometres (km)"): 1.60934,
                ("Miles (mi)", "Feet (ft)"): 5280,
                ("Feet (ft)", "Metres (m)"): 0.3048,
                ("Feet (ft)", "Kilometres (km)"): 0.0003048,
                ("Feet (ft)", "Miles (mi)"): 0.000189394
            }

            if from_unit == to_unit:
                result = value
            else:
                result = value * conversion_factors.get((from_unit, to_unit), 1)

            self.result_value.configure(text=f"{result:.2f}")
        except ValueError:
            self.result_value.configure(text="Invalid input")
       

class SpeedConverter(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Speed Converter")
        self.geometry("300x400")
        label = ctk.CTkLabel(self, text="Speed Converter", font=("Arial", 18))
        label.pack(pady=20)

        self.from_label = ctk.CTkLabel(self, text= "From:")
        self.from_label.pack()

        self.from_combobox = ctk.CTkComboBox(self, values=["Km/h", "mph", "m/s"])
        self.from_combobox.pack(pady=5)
        self.from_combobox.set("Km/h")

        self.input_label = ctk.CTkLabel(self, text="Enter Value: ")
        self.input_label.pack()

        self.input_entry = ctk.CTkEntry(self)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<KeyRelease>", self.calculate_result)

        self.to_label = ctk.CTkLabel(self, text="To:")
        self.to_label.pack()

        self.to_combobox = ctk.CTkComboBox(self, values=["Km/h", "mph", "m/s"])
        self.to_combobox.pack(pady=5)
        self.to_combobox.set("mph")

        self.result_label=ctk.CTkLabel(self, text="Result:")
        self.result_label.pack()

        self.result_value = ctk.CTkLabel(self, text="0.0", font=("Arial", 16))
        self.result_value.pack(pady=5)


    def calculate_result(self, event=None):
        try:
            from_unit = self.from_combobox.get()
            to_unit = self.to_combobox.get()
            value = float(self.input_entry.get())

            conversion_factors = {
                ("Km/h", "mph"): 0.621371,
                ("Km/h", "m/s"): 0.277778,
                ("mph", "Km/h"): 1.60934,
                ("mph", "m/s"): 0.44704,
                ("m/s", "Km/h)"): 3.6,
                ("m/s", "mph"): 2.23694
            }

            if from_unit == to_unit:
                result = value
            else:
                result = value * conversion_factors.get((from_unit, to_unit), 1)

            self.result_value.configure(text=f"{result:.2f}")
        except ValueError:
            self.result_value.configure(text="Invalid input")
        

class TemperatureConverter(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Temperature Converter")
        self.geometry("300x400")
        label = ctk.CTkLabel(self, text="Temperature Converter", font=("Arial", 18))
        label.pack(pady=20)

        self.from_label = ctk.CTkLabel(self, text= "From:")
        self.from_label.pack()

        self.from_combobox = ctk.CTkComboBox(self, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.from_combobox.pack(pady=5)
        self.from_combobox.set("Celsius")

        self.input_label = ctk.CTkLabel(self, text="Enter Value: ")
        self.input_label.pack()

        self.input_entry = ctk.CTkEntry(self)
        self.input_entry.pack(pady=5)
        self.input_entry.bind("<KeyRelease>", self.calculate_result)

        self.to_label = ctk.CTkLabel(self, text="To:")
        self.to_label.pack()

        self.to_combobox = ctk.CTkComboBox(self, values=["Celsius", "Fahrenheit", "Kelvin"])
        self.to_combobox.pack(pady=5)
        self.to_combobox.set("Fahrenheit")

        self.result_label=ctk.CTkLabel(self, text="Result:")
        self.result_label.pack()

        self.result_value = ctk.CTkLabel(self, text="0.0", font=("Arial", 16))
        self.result_value.pack(pady=5)


    def calculate_result(self, event=None):
        try:
            from_unit = self.from_combobox.get()
            to_unit = self.to_combobox.get()
            value = float(self.input_entry.get())

            if from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = value *9/5 + 32
            elif from_unit =="Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
            else:
                result = value

            self.result_value.configure(text=f"{result:.2f}")
        except ValueError:
            self.result_value.configure(text="Invalid input")
        

if __name__ == "__main__":
    ctk.set_appearance_mode("System") 
    ctk.set_default_color_theme("blue")

    app = UnitConverterApp()
    app.mainloop()