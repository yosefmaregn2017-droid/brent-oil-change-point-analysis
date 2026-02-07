from flask import Flask, jsonify
import pandas as pd
import os

app = Flask(__name__)

# Paths to your CSV files
DATA_FOLDER = os.path.join(os.getcwd(), "data")
PRICE_FILE = os.path.join(DATA_FOLDER, "BrentOilPrices.csv")
EVENTS_FILE = os.path.join(DATA_FOLDER, "BrentOilEvents.csv")

# Load data once on server start
try:
    df_prices = pd.read_csv(PRICE_FILE, parse_dates=['Date'])
    df_events = pd.read_csv(EVENTS_FILE, parse_dates=['Date'])
except FileNotFoundError as e:
    print(f"File not found: {e}")
    df_prices = pd.DataFrame()
    df_events = pd.DataFrame()


@app.route("/")
def home():
    return jsonify({"message": "Brent Oil Analysis API is running"})


@app.route("/prices")
def get_prices():
    """Return Brent Oil price data"""
    if df_prices.empty:
        return jsonify({"error": "Price data not loaded"}), 404
    return jsonify(df_prices.to_dict(orient="records"))


@app.route("/events")
def get_events():
    """Return Brent Oil events data"""
    if df_events.empty:
        return jsonify({"error": "Events data not loaded"}), 404
    return jsonify(df_events.to_dict(orient="records"))


@app.route("/change-points")
def get_change_points():
    """Return placeholder for change point analysis results"""
    # You can later replace this with your model output
    return jsonify({
        "message": "Change point analysis endpoint",
        "change_points": [
            "2020-03-01",
            "2021-06-15",
            "2022-02-10"
        ]
    })


if __name__ == "__main__":
    app.run(debug=True)
