# 🚗 Car Price Predictor

This project is a machine learning pipeline that predicts used car prices based on various features such as brand, model, year, fuel type, transmission, and more. It allows both programmatic use and a user-friendly interactive interface.

---

## 📌 Features

- 💡 Predict car prices based on real-world data
- 🧼 Preprocessing: outlier filtering, one-hot encoding, feature extraction
- 🔍 Model comparison and automatic best model selection
- 📦 Model export with `joblib` for future predictions
- 🖥️ Simple command-line & GUI (optional) interface
- 🧪 Easily integrate prediction with your own apps/scripts

---

## 🗂️ Project Structure

car-price-predictor/
├── data/                  # Raw and cleaned data (e.g., cardekho.csv)
├── notebooks/             # Jupyter notebooks for training, EDA, experimentation
├── src/                   # Source code modules
│   ├── model_utils.py     # Model training, evaluation, feature engineering
│   ├── predictor.py       # Module to load model & predict prices from input
│   └── ui.py              # (Optional) Streamlit app or CLI interface
├── requirements.txt       # Python dependencies
├── .gitignore             # Git ignore list
└── README.md              # Project documentation

---

## 🧠 How It Works

### 🔍 Model Selection Pipeline

1. **Data Preprocessing**
   - Drops missing or irrelevant data
   - One-hot encodes categorical variables (`fuel`, `transmission`, `owner`, `brand`)
   - Extracts features like:
     - `car_age` (capped at 20 years)
     - `km_per_year` (km driven divided by car age)

2. **Model Training & Evaluation**
   - Trains multiple regression models:
     - `RandomForestRegressor` (100 and 300 estimators)
     - `GradientBoostingRegressor`
     - `LinearRegression`
   - Evaluates each using:
     - Root Mean Squared Error (RMSE)
     - Relative RMSE (% of average price)

3. **Best Model Selection**
   - Automatically selects the model with the **lowest RMSE**
   - Saves the selected model as `./src/car_price_model.pkl` for future use

---

## 🧪 Usage

### 1. Run the UI to Predict Car Price

```bash
pip install -r requirements.txt
python src/ui.py

