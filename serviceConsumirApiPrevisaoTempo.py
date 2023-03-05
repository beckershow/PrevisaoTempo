import requests
import json

class ServiceConsumirApiPrevisaoTempo:

    # http://api.openweathermap.org/geo/1.0/direct?q = {city name}, {state code}, {country code} & limit = {limit} & appid = {API key}

    def __init__(self):
        self = self
        self.KEY_API = '2b3cac54f83fc274e7178749104b0e8b'

    def consultar_previsaotempo(self, cidade, pais):
        # url de consulta, 5 dias de 3 em 3 horas, a unica que foi encontrado
        base_url = "http://api.openweathermap.org/data/2.5/forecast?lang=pt_br&units=metric&"

        # Cidade
        city_name = cidade

        # Pais
        pais_name = pais

        # completa
        complete_url = base_url + "appid=" + self.KEY_API + "&q=" + city_name + "," + pais_name

        response = requests.get(complete_url)

        print(response.json())

        return response.json()