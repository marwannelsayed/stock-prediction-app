import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense, Reshape
from datetime import datetime

def predict_stock_price(data: pd.DataFrame, target_date):
    close_prices = data['Close'].values.reshape(-1, 1)

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(close_prices)

    window_size = 60
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i - window_size:i, 0])
        y.append(scaled_data[i, 0])

    X = np.array(X)
    y = np.array(y)
    X = X.reshape((X.shape[0], X.shape[1], 1))

    # Define and train RNN
    model = Sequential([
        SimpleRNN(50, activation='relu', input_shape=(X.shape[1], 1)),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    model.fit(X, y, epochs=5, batch_size=32, verbose=0)

    # Predict until target_date
    days_to_predict = (target_date - datetime.today().date()).days
    last_window = scaled_data[-window_size:].flatten()
    preds = []

    for _ in range(days_to_predict):
        inp = last_window[-window_size:].reshape(1, window_size, 1)
        pred = model.predict(inp, verbose=0)[0][0]
        preds.append(pred)
        last_window = np.append(last_window, pred)

    predicted_scaled = np.array(preds).reshape(-1, 1)
    predicted_prices = scaler.inverse_transform(predicted_scaled)
    
    return float(predicted_prices[-1]), predicted_prices
