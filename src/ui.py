import tkinter as tk
from tkinter import ttk, messagebox
from car_price_predictor import predict_price, BRANDS, MODELS, FUELS, TRANSMISSIONS, OWNERS


class CarPriceApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Car Price Estimator")
        self.geometry("400x580")
        self.configure(padx=10, pady=10)

        self.create_widgets()

    def create_widgets(self):
        # Brand
        ttk.Label(self, text="Brand:").pack(anchor="w")
        self.brand_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.brand_var, values=sorted(
            BRANDS), state="readonly").pack(fill="x")

        # Model
        ttk.Label(self, text="Model:").pack(anchor="w", pady=(10, 0))
        self.model_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.model_var, values=sorted(
            MODELS), state="readonly").pack(fill="x")

        # Year
        ttk.Label(self, text="Year:").pack(anchor="w", pady=(10, 0))
        self.year_entry = ttk.Entry(self)
        self.year_entry.pack(fill="x")

        # KM Driven
        ttk.Label(self, text="KM Driven:").pack(anchor="w", pady=(10, 0))
        self.km_entry = ttk.Entry(self)
        self.km_entry.pack(fill="x")

        # Fuel
        ttk.Label(self, text="Fuel:").pack(anchor="w", pady=(10, 0))
        self.fuel_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.fuel_var,
                     values=FUELS, state="readonly").pack(fill="x")

        # Transmission
        ttk.Label(self, text="Transmission:").pack(anchor="w", pady=(10, 0))
        self.transmission_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.transmission_var,
                     values=TRANSMISSIONS, state="readonly").pack(fill="x")

        # Owner
        ttk.Label(self, text="Owner:").pack(anchor="w", pady=(10, 0))
        self.owner_var = tk.StringVar()
        ttk.Combobox(self, textvariable=self.owner_var,
                     values=OWNERS, state="readonly").pack(fill="x")

        # Engine
        ttk.Label(self, text="Engine (cc):").pack(anchor="w", pady=(10, 0))
        self.engine_entry = ttk.Entry(self)
        self.engine_entry.pack(fill="x")

        # Max Power
        ttk.Label(self, text="Max Power (bhp):").pack(anchor="w", pady=(10, 0))
        self.power_entry = ttk.Entry(self)
        self.power_entry.pack(fill="x")

        # Seats
        ttk.Label(self, text="Seats:").pack(anchor="w", pady=(10, 0))
        self.seats_entry = ttk.Entry(self)
        self.seats_entry.pack(fill="x")

        # Predict Button
        ttk.Button(self, text="Estimate Price",
                   command=self.predict_price).pack(pady=15)

        self.result_label = ttk.Label(
            self, text="", font=("Arial", 14), foreground="blue")
        self.result_label.pack()

    def predict_price(self):
        try:
            brand = self.brand_var.get()
            model = self.model_var.get()
            name = f"{brand} {model}"

            car = {
                'name': name,
                'year': int(self.year_entry.get()),
                'km_driven': int(self.km_entry.get()),
                'fuel': self.fuel_var.get(),
                'transmission': self.transmission_var.get(),
                'owner': self.owner_var.get(),
                'engine': float(self.engine_entry.get()),
                'max_power': float(self.power_entry.get()),
                'seats': float(self.seats_entry.get())
            }

            price = predict_price(car)
            self.result_label.config(
                text=f"Estimated Price: ${price/18:,.0f}")

        except ValueError as ve:
            messagebox.showerror("Input Error", f"Invalid number input: {ve}")
        except Exception as e:
            messagebox.showerror("Error", f"Something went wrong:\n{e}")


if __name__ == "__main__":
    app = CarPriceApp()
    app.mainloop()
