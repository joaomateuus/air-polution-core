from core import models
from django.db import transaction
import requests

estados = [
    {"estado": "Acre", "latitude": -8.77, "longitude": -70.55},
    {"estado": "Alagoas", "latitude": -9.71, "longitude": -35.73},
    {"estado": "Amazonas", "latitude": -3.07, "longitude": -61.66},
    {"estado": "Amapá", "latitude": 1.41, "longitude": -51.77},
    {"estado": "Bahia", "latitude": -12.96, "longitude": -38.51},
    {"estado": "Ceará", "latitude": -3.71, "longitude": -38.54},
    {"estado": "Distrito Federal", "latitude": -15.83, "longitude": -47.86},
    {"estado": "Espírito Santo", "latitude": -19.19, "longitude": -40.34},
    {"estado": "Goiás", "latitude": -16.64, "longitude": -49.31},
    {"estado": "Maranhão", "latitude": -2.55, "longitude": -44.30},
    {"estado": "Mato Grosso", "latitude": -12.64, "longitude": -55.42},
    {"estado": "Mato Grosso do Sul", "latitude": -20.51, "longitude": -54.54},
    {"estado": "Minas Gerais", "latitude": -18.10, "longitude": -44.38},
    {"estado": "Pará", "latitude": -5.53, "longitude": -52.29},
    {"estado": "Paraíba", "latitude": -7.06, "longitude": -35.55},
    {"estado": "Paraná", "latitude": -24.89, "longitude": -51.55},
    {"estado": "Pernambuco", "latitude": -8.28, "longitude": -35.07},
    {"estado": "Piauí", "latitude": -8.28, "longitude": -43.68},
    {"estado": "Rio de Janeiro", "latitude": -22.84, "longitude": -43.15},
    {"estado": "Rio Grande do Norte", "latitude": -5.22, "longitude": -36.52},
    {"estado": "Rondônia", "latitude": -11.22, "longitude": -62.80},
    {"estado": "Rio Grande do Sul", "latitude": -30.01, "longitude": -51.22},
    {"estado": "Roraima", "latitude": 1.89, "longitude": -61.22},
    {"estado": "Santa Catarina", "latitude": -27.33, "longitude": -49.44},
    {"estado": "Sergipe", "latitude": -10.90, "longitude": -37.07},
    {"estado": "São Paulo", "latitude": -23.55, "longitude": -46.64},
    {"estado": "Tocantins", "latitude": -10.25, "longitude": -48.25}
]

api_key: str = '954d710dc63014a43aaf61167742641a'
status_dict = {
    "1":"B",
    "2":"R",
    "3":"M",
    "4":"P",
    "5":"MP",
}


def save_estados():
    for i in estados:
        print(i)
        estado = models.Estado(
            nome=i['estado'],
            longitude=i['longitude'],
            latitude=i['latitude']
        )
        estado.save()
        print('Estados salvos')

def fetch_air_quality_data():
    estados = models.Estado.objects.all()
    for i in estados:
        params = {"lat": i.latitude, "lon": i.longitude, "appid": api_key}
        data = requests.get('http://api.openweathermap.org/data/2.5/air_pollution', params=params)
        values = data.json()['list'][0]['components']
        air_quality =  data.json()['list'][0]['main']['aqi']
        qualidade_ar = models.NivelPoluicao.objects.create(
            estado=i,
            concentracao_co2=values['co'],
            concentracao_no2=values['no2'],
            concentracao_no=values['no'],
            status=status_dict.get(str(air_quality))
        )
        print(qualidade_ar)


@transaction.atomic()
def run():
    try:
        save_estados()
        fetch_air_quality_data()
        
        print('\n')
        print('\n')
        print('Dados salvos com sucesso')
            
    except Exception as e:
        print(str(e))