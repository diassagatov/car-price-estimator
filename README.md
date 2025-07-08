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

![image](https://github.com/user-attachments/assets/ae386d66-5c3f-4e54-afbb-ef0aa4b33153)
