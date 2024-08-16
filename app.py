import os
from flask import Flask, send_from_directory
from flask import Flask

app = Flask(__name__)


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def serve_dashboard():
    return send_from_directory(app.static_folder, 'index.html')

# Suas rotas de API aqui
@app.route('/api/dollar', methods=['GET'])
def get_dollar_rate():
    dollar_rate = round(random.uniform(5.00, 6.00), 2)
    return jsonify({'rate': dollar_rate})

@app.route('/api/oil', methods=['GET'])
def get_oil_price():
    oil_price = round(random.uniform(70.00, 80.00), 2)
    return jsonify({'price': oil_price})

@app.route('/api/grains', methods=['GET'])
def get_grains_price():
    grains_price = round(random.uniform(10.00, 15.00), 2)
    return jsonify({'price': grains_price})

@app.route('/api/news', methods=['GET'])
def get_news():
    news = [
        {"title": "Gasolina sobe em todo o país", "date": "2024-08-15"},
        {"title": "Postos de gasolina investem em energia solar", "date": "2024-08-14"}
    ]
    return jsonify({'news': news})

@app.route('/api/fuel_prices', methods=['GET'])
def get_fuel_prices():
    fuel_prices = [
        {"city": "Curitiba", "price": 4.50},
        {"city": "Londrina", "price": 4.45},
        {"city": "Maringá", "price": 4.47}
    ]
    return jsonify({'prices': fuel_prices})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)