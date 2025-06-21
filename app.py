import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime, timedelta

# Placeholder for model import
from model import predict_stock_price

STOCKS = {
    'NVIDIA': 'NVDA',
    'Amazon': 'AMZN',
    'Apple': 'AAPL'
}

st.title('Stock Price Prediction App')

stock_name = st.selectbox('Select a stock:', list(STOCKS.keys()))
ticker = STOCKS[stock_name]

st.write(f"You selected: {stock_name} ({ticker})")

# Date picker for prediction date
min_date = datetime.today() + timedelta(days=1)
max_date = datetime.today() + timedelta(days=30)
pred_date = st.date_input('Pick a date within the next month:', min_value=min_date, max_value=max_date)

# Download historical data
data_load_state = st.text('Loading data...')
data = yf.download(ticker, period='2y')
data_load_state.text('Loading data... done!')

if 'prediction_series' not in st.session_state:
    st.session_state['prediction_series'] = None
if 'predicted_price' not in st.session_state:
    st.session_state['predicted_price'] = None
if 'pred_date' not in st.session_state:
    st.session_state['pred_date'] = None

# Show chart with prediction if available
if (
    st.session_state['predicted_price'] is not None and
    st.session_state['pred_date'] is not None and
    st.session_state['prediction_series'] is not None
):
    chart_data = data['Close'].copy()
    
    # Generate future date range
    pred_series = st.session_state['prediction_series']
    last_date = chart_data.index[-1]
    future_dates = pd.date_range(start=last_date + timedelta(days=1), periods=len(pred_series))
    
    # Create series of future predictions
    future_prices = pd.Series(pred_series.flatten(), index=future_dates)
    
    # Combine and plot
    combined = pd.concat([chart_data, future_prices])
    combined.index = pd.to_datetime(combined.index)
    combined = combined.sort_index()
    
    st.line_chart(combined, use_container_width=True)


# Prediction logic
if st.button('Predict'):
    predicted_price, prediction_series = predict_stock_price(data, pred_date)
    st.session_state['predicted_price'] = predicted_price
    st.session_state['pred_date'] = pred_date
    st.session_state['prediction_series'] = prediction_series
    st.success(f"Predicted closing price for {stock_name} on {pred_date}: ${predicted_price:.2f}")