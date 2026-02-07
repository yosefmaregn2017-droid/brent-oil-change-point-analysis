from flask import Flask, render_template
import pandas as pd
import plotly.express as px

app = Flask(__name__)

PRICE_FILE = 'data/BrentOilPrices.csv'

@app.route('/')
def home():
    return "Brent Oil Change Point Analysis App"

@app.route('/plot')
def plot():
    df_prices = pd.read_csv(PRICE_FILE, parse_dates=['Date'])
    fig = px.line(df_prices, x='Date', y='Price', title='Brent Oil Prices')
    graph_html = fig.to_html(full_html=False)
    return graph_html

if __name__ == '__main__':
    app.run(debug=True)
from flask import render_template_string
import plotly.express as px

# Plot route
@app.route("/plot")
def plot():
    # Create a simple line chart of Brent Oil prices
    fig = px.line(df_prices, x="Date", y="Price", title="Brent Oil Prices Over Time")
    
    # Render the chart as HTML
    graph_html = fig.to_html(full_html=False)
    
    # Return as a web page
    return render_template_string("""
        <html>
            <head>
                <title>Brent Oil Prices</title>
            </head>
            <body>
                <h1>Brent Oil Prices Chart</h1>
                {{ graph | safe }}
            </body>
        </html>
    """, graph=graph_html)
