# 📈 Stock Price Prediction App

A web application that predicts future stock prices for popular stocks (Apple, Amazon, NVIDIA) using a time-series forecasting model (RNN). Built with **Streamlit**, **TensorFlow**, and **yfinance**.

---

## 🚀 Features

- 📊 Choose from well-known stocks: Apple, Amazon, or NVIDIA
- 📅 Select any date within the next 30 days
- 🤖 Predicts stock price for the selected date using a Recurrent Neural Network (RNN)
- 📈 Displays a line chart with historical prices + predicted future prices up to the selected date
- Built with real-time stock data from [Yahoo Finance](https://finance.yahoo.com/)

---

## 🛠️ Technologies Used

- [Streamlit](https://streamlit.io/) – web app framework
- [yfinance](https://github.com/ranaroussi/yfinance) – stock data API
- [TensorFlow / Keras](https://www.tensorflow.org/) – deep learning (RNN)
- [scikit-learn](https://scikit-learn.org/) – for data scaling
- Python 3.9+

---

## 📦 Installation

1. **Clone the repo**:
   ```bash
   git clone https://github.com/yourusername/stock-prediction-app.git
   cd stock-prediction-app
   ```

## Setup
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   If you encounter system package errors, try:
   ```bash
   pip install --user -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Project Structure
- `app.py`: Main Streamlit app (UI, chart, prediction trigger)
- `model.py`: RNN model logic and prediction function
- `requirements.txt`: Python dependencies

## How It Works
- Downloads the past 2 years of daily stock prices.
- Scales the data and trains a simple RNN model using the last 60-day window.
- Predicts one price per day up to your selected future date.
- Visualizes the actual and predicted prices on a line chart.

## Notes
- The RNN model is trained on-the-fly for each prediction (for demo purposes)
- For production, consider saving/loading pre-trained models for efficiency