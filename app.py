from flask import Flask, render_template, jsonify
from database.model import get_countries, get_country_by_id
import os
from dotenv import load_dotenv

# Завантажуємо змінні середовища
load_dotenv(os.path.join(os.path.dirname(__file__), 'config/.env'))

# Ініціалізуємо Flask додаток
app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/')
def index():
    """Головна сторінка зі списком країн"""
    countries = get_countries()
    return render_template('index.html', countries=countries)

@app.route('/country/<int:country_id>')
def country_page(country_id):
    """Сторінка деталей про конкретну країну"""
    country = get_country_by_id(country_id)
    if country is None:
        return render_template('404.html'), 404
    else:
        return render_template('country.html', country=country)

@app.route('/api/countries')
def api_countries():
    """API для отримання всіх країн"""
    countries = get_countries()
    return jsonify(countries)

@app.route('/api/country/<int:country_id>')
def api_country(country_id):
    """API для отримання інформації про конкретну країну"""
    country = get_country_by_id(country_id)
    if country is None:
        return jsonify({'error': 'Country not found'}), 404
    return jsonify(country)

@app.errorhandler(404)
def not_found(error):
    """Обработка помилки 404"""
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    """Обработка помилки 500"""
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':

    debug_mode = os.getenv('FLASK_ENV', 'development') == 'development'
    port = int(os.getenv('FLASK_PORT', 5000))
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode
    )
