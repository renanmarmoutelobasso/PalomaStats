from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/api/dollar', methods=['GET'])
def get_dollar_rate():
    # Simulação de cotação do dólar
    dollar_rate = round(random.uniform(5.00, 6.00), 2)
    return jsonify({'rate': dollar_rate})

@app.route('/api/oil', methods=['GET'])
def get_oil_price():
    # Simulação de preço do barril de petróleo
    oil_price = round(random.uniform(70.00, 80.00), 2)
    return jsonify({'price': oil_price})

@app.route('/api/grains', methods=['GET'])
def get_grains_price():
    # Simulação de cotação de grãos
    grains_price = round(random.uniform(10.00, 15.00), 2)
    return jsonify({'price': grains_price})

@app.route('/api/news', methods=['GET'])
def get_news():
    # Simulação de notícias relacionadas a postos de gasolina
    news = [
        {"title": "Gasolina sobe em todo o país", "date": "2024-08-15"},
        {"title": "Postos de gasolina investem em energia solar", "date": "2024-08-14"}
    ]
    return jsonify({'news': news})

@app.route('/api/fuel_prices', methods=['GET'])
def get_fuel_prices():
    # Simulação de preços de combustíveis no estado do Paraná
    fuel_prices = [
        {"city": "Curitiba", "price": 4.50},
        {"city": "Londrina", "price": 4.45},
        {"city": "Maringá", "price": 4.47}
    ]
    return jsonify({'prices': fuel_prices})

if __name__ == '__main__':
    app.run(debug=True)
