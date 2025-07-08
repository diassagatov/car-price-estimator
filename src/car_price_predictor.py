import pandas as pd
import joblib

# Load your trained model (make sure the file is in the same folder)
model = joblib.load("./src/car_price_model.pkl")

# Update these lists with your exact categories from training:
BRANDS = ['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
          'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
          'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
          'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
          'Ambassador', 'Ashok', 'Isuzu', 'Opel']
MODELS = ['Swift', 'Rapid', 'City', 'i20', 'Xcent', 'Wagon', '800', 'Etios',
          'Figo', 'Duster', 'Zen', 'KUV', 'Ertiga', 'Alto', 'Verito', 'WR-V',
          'SX4', 'Tigor', 'Baleno', 'Enjoy', 'Omni', 'Vitara', 'Verna', 'GO',
          'Safari', 'Compass', 'Fortuner', 'Innova', 'B', 'Amaze', 'Pajero',
          'Ciaz', 'Jazz', 'A6', 'Corolla', 'New', 'Manza', 'i10', 'Ameo',
          'Vento', 'EcoSport', 'X1', 'Celerio', 'Polo', 'Eeco', 'Scorpio',
          'Freestyle', 'Passat', 'Indica', 'XUV500', 'Indigo', 'Terrano',
          'Creta', 'KWID', 'Santro', 'Q5', 'ES', 'XF', 'Wrangler', 'Rover',
          'S-Class', '5', 'X4', 'Superb', 'E-Class', 'Hector', 'XC40', 'Q7',
          'Elantra', 'XE', 'Nexon', 'CLA', 'Glanza', '3', 'Camry', 'XC90',
          'Ritz', 'Grand', 'Matiz', 'Zest', 'Getz', 'Elite', 'Brio', 'Hexa',
          'Sunny', 'Micra', 'Ssangyong', 'Quanto', 'Accent', 'Ignis',
          'Marazzo', 'Tiago', 'Thar', 'Sumo', 'Bolero', 'GL-Class', 'Beat',
          'A-Star', 'XUV300', 'Nano', 'GTI', 'V40', 'CR-V', 'EON', 'RediGO',
          'Captiva', 'Fiesta', 'Seltos', 'Civic', 'Sail', 'Venture',
          'Classic', 'BR-V', 'Ecosport', 'Aria', 'TUV', 'Bolt', 'Accord',
          'Xylo', 'Grande', 'S-Cross', 'Yaris', 'Tavera', 'Linea',
          'Endeavour', 'Aveo', 'Triber', 'Fusion', 'Octavia', 'A4', 'XL6',
          'Santa', 'Spark', 'Aspire', 'Optra', 'Mobilio', 'BRV', 'X6',
          'Cruze', 'GLA', '6', 'NuvoSport', 'Scala', 'Lodgy', 'Pulse',
          'Supro', 'Sonata', 'Renault', 'Kicks', 'Jetta', 'M-Class', 'Teana',
          'Yeti', 'Q3', 'Gurkha', 'Logan', 'A3', 'Dzire', 'Ikon', 'Fluence',
          'Xenon', 'One', '7', 'S60', 'Lancer', 'X7', 'Fabia', 'Platinum',
          'Captur', 'Gypsy', 'Koleos', 'CLASSIC', 'Harrier', 'Punto',
          'Avventura', 'Laura', 'Leyland', 'MUX', 'Astra', 'Tucson',
          'Esteem', 'Winger', 'Qualis', 'Spacio', 'Venue', 'CrossPolo',
          'Kodiaq', 'D-Max', 'X3', 'Land', 'X5', 'Trailblazer', 'MU', 'GLC',
          'XC60', 'S90', 'S-Presso']
FUELS = ['Diesel', 'Petrol', 'CNG', 'LPG']  # example fuels
TRANSMISSIONS = ['Manual', 'Automatic']
OWNERS = ['First Owner', 'Second Owner', 'Third Owner',
          'Fourth & Above Owner', 'Test Drive Car']


def encode_one_hot(value, valid_values, prefix):
    """
    One-hot encode `value` given valid categories in `valid_values`.
    Returns dict with keys like prefix_value: 1 or 0.
    """
    if value not in valid_values:
        # Value unseen during training; encode all zeros
        print(
            f"Warning: '{value}' not in training categories for {prefix}. Encoding all zeros.")
        return {f"{prefix}_{v}": 0 for v in valid_values}
    return {f"{prefix}_{v}": int(v == value) for v in valid_values}


def prepare_input(car):
    """
    Prepare input DataFrame row from a car dict for prediction.
    """
    brand = car['name'].split()[0]

    # For model_encoded, if you have a mapping dict or logic, implement here
    model_encoded = 0

    data = {}
    data.update(encode_one_hot(brand, BRANDS, 'brand'))
    data.update(encode_one_hot(car['fuel'], FUELS, 'fuel'))
    data.update(encode_one_hot(
        car['transmission'], TRANSMISSIONS, 'transmission'))
    data.update(encode_one_hot(car['owner'], OWNERS, 'owner'))

    data['model_encoded'] = model_encoded
    data['km_driven'] = car['km_driven']
    data['engine'] = car['engine']
    data['max_power'] = car['max_power']
    data['seats'] = car['seats']
    data['car_age'] = 2025 - car['year']

    # Fill missing columns that model expects with zeros
    for col in model.feature_names_in_:
        if col not in data:
            data[col] = 0

    df = pd.DataFrame([data])
    df = df[model.feature_names_in_]
    return df


def predict_price(car):
    """
    Predict car price from car info dict.
    """
    df = prepare_input(car)
    price = model.predict(df)[0]
    return price
