from flask import Flask, request, jsonify
from flask_cors import CORS
from lib.csv_reader import read_csv, get_absolute_path
import os

app = Flask(__name__)
CORS(app)

@app.route('/fetch-countries', methods=['GET'])
def fetch_countries():
    """
    : @route: /fetch-countries
    : @method: GET
    : @desc: This function returns the names of countries without duplication.
    """
    return_buffer = []
    temp_buffer = []
    data = read_csv(get_absolute_path('data/suicide-rates-by-country.csv'))

    """ Lamda Function to compare two strings """
    compare = lambda w1, w2: True if w1 == w2 else False

    """ Populating a list with country names only """
    for i in range(len(data) - 1):
        if data[i][0] == data[i + 1][0]:
            temp_buffer.append(data[i][0])

    """ Removing Duplications from the list(return_buffer) """
    for i in range(len(temp_buffer) - 1):
        if not compare(temp_buffer[i], temp_buffer[i + 1]):
            return_buffer.append(temp_buffer[i])
    del temp_buffer
    return jsonify(return_buffer)

@app.route('/get-stats', methods=['GET'])
def get_stats():
    """
    : @route: /get-stats
    : @method: GET
    : @desc: This function returns the data for a country when given a country name.
    """
    country_name = request.args.get('cn')
    country_data = []
    data = read_csv(get_absolute_path('data/suicide-rates-by-country.csv'))
    for i in range(len(data) - 1):
        if data[i][0] == country_name:
            temp = {
                'name': data[i][0],
                'year': data[i][2],
                'suicide_rate': data[i][3]
            }
            country_data.append(temp)
    return jsonify(country_data)

if __name__ == '__main__':
    app.run(debug=True)