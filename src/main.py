import requests
from flask import request, Flask
import json
from src.city_map import get_city

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
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

        # response = \
        #     f'{city_name} terá {description},\
        #      com temperatura de {temp}ºC,\
        #       máxima de {max_temp}ºC\
        #        e mínima de {min_temp}ºC'

        response =

        return json.dumps({
            "city_name": city_name,
            "description": description,
            "temp": f'{temp}ºC',
            "max_temp": f'{max_temp}ºC',
            "min_temp": f'{min_temp}ºC'
        })
    except Exception as ex:
        return f'Não foi possível obter os dados climaticos para o token {city}: {ex}'


app.run()
