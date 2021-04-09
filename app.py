import requests
import json
from flask import request, Flask
from flask_cors import cross_origin
from src.city_map import get_city

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/forecast', methods=['GET'])
@cross_origin()
def home():
    try:
        city = get_city(request.args.get('city'))
        req = requests.get(f'https://api.hgbrasil.com/weather?woeid={city}')
        result = dict(json.loads(req.text))['results']

        forecast = result['forecast']

        temp = result['temp']
        max_temp = forecast[0]['max']
        min_temp = forecast[0]['min']

        city_name = result['city_name']
        description = str(result['description']).lower()

        return json.dumps({
            "city_name": city_name,
            "description": description,
            "temp": f'{temp}ºC',
            "max_temp": f'{max_temp}ºC',
            "min_temp": f'{min_temp}ºC'
        })
    except Exception as ex:
        return f'Não foi possível obter os dados climaticos: {ex}'


@app.route('/')
def index():
    return "<h1>Welcome to Forecast Weather API!</h1>"


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)
