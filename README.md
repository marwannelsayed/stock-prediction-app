# Stock Prediction App

A streamlined web app to:
- Show well-known stocks (NVIDIA, Amazon, Apple)
- Predict daily stock prices up to 30 days ahead
- Allow users to choose a date within the next month
- Display the prediction for that date

## Key Technologies
- Streamlit: simple web app interface
- yfinance: get historical stock data
- Keras (RNN): time-series forecasting
- NumPy & pandas: data handling

## Setup
1. Install dependencies:
   ```bash
   pip install streamlit yfinance keras tensorflow numpy pandas
   ```
2. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py`: Main Streamlit app
- `model.py`: Model training and prediction logic
- `requirements.txt`: Python dependencies