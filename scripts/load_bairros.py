from core import models
from django.db import transaction

bairros_manaus = [
            { "bairro": "Adrianópolis", "longitude": -60.0100488, "latitude": -3.1016961 },
            { "bairro": "Aleixo", "longitude": -59.9941528, "latitude": -3.0869431 },
            { "bairro": "Alvorada", "longitude": -60.0404007, "latitude": -3.0752159 },
            { "bairro": "Aparecida", "longitude": -60.0300102, "latitude": -3.1173418 },
            { "bairro": "Armando Mendes", "longitude": -59.9421428, "latitude": -3.0897108 },
            { "bairro": "Betânia", "longitude": -59.9955978, "latitude": -3.1341656 },
            { "bairro": "Cachoeirinha", "longitude": -60.0057133, "latitude": -3.1268 },
            { "bairro": "Centro", "longitude": -60.0206598, "latitude": -3.1298957 },
            { "bairro": "Chapada", "longitude": -60.0288373, "latitude": -3.0967957 },
            { "bairro": "Cidade Nova", "longitude": -59.9854831, "latitude": -3.0362681 },
            { "bairro": "Colônia Antônio Aleixo", "longitude": -59.8938122, "latitude": -3.0876383 },
            { "bairro": "Colônia Oliveira Machado", "longitude": -60.001378, "latitude": -3.1497201 },
            { "bairro": "Colônia Santo Antônio", "longitude": -60.0101259, "latitude": -3.0373555 },
            { "bairro": "Colônia Terra Nova", "longitude": -60.0201653, "latitude": -3.0110435 },
            { "bairro": "Compensa", "longitude": -60.0578516, "latitude": -3.1037639 },
            { "bairro": "Coroado", "longitude": -59.9810602, "latitude": -3.0905755 },
            { "bairro": "Crespo", "longitude": -59.9825933, "latitude": -3.1436353 },
            { "bairro": "Distrito Industrial", "longitude": -59.9623665, "latitude": -3.123242 },
            { "bairro": "Dom Pedro", "longitude": -60.0461828, "latitude": -3.0885575 },
            { "bairro": "Educandos", "longitude": -60.0100488, "latitude": -3.1412091 },
            { "bairro": "Flores", "longitude": -60.0086036, "latitude": -3.054504 },
            { "bairro": "Glória", "longitude": -60.0353416, "latitude": -3.1227903 },
            { "bairro": "Japiim", "longitude": -59.9768139, "latitude": -3.1127248 },
            { "bairro": "Jorge Teixeira", "longitude": -59.9285217, "latitude": -3.0283517 },
            { "bairro": "Lírio do Vale", "longitude": -60.0678679, "latitude": -3.0727728 },
            { "bairro": "Margem Esquerda do Rio Negro", "longitude": -60.4022972, "latitude": -2.0588487 },
            { "bairro": "Margem Esquerda do Rio Solimões", "longitude": -60.0217314, "latitude": -3.1190275 },
            { "bairro": "Mauazinho", "longitude": -59.9392539, "latitude": -3.1225147 },
            { "bairro": "Monte das Oliveiras", "longitude": -59.9944179, "latitude": -3.0039494 },
            { "bairro": "Morro da Liberdade", "longitude": -60.001378, "latitude": -3.1365435 },
            { "bairro": "Nossa Senhora das Graças", "longitude": -60.0187201, "latitude": -3.1041608 },
            { "bairro": "Nova Esperança", "longitude": -60.0591935, "latitude": -3.083475 },
            { "bairro": "Novo Israel", "longitude": -60.0129391, "latitude": -3.027249 },
            { "bairro": "Parque 10 de Novembro", "longitude": -59.9970428, "latitude": -3.0716838 },
            { "bairro": "Paz", "longitude": -60.0288373, "latitude": -3.0573173 },
            { "bairro": "Petrópolis", "longitude": -59.9941528, "latitude": -3.1088793 },
            { "bairro": "Planalto", "longitude": -60.0548564, "latitude": -3.064695 },
            { "bairro": "Ponta Negra", "longitude": -60.0895564, "latitude": -3.0482142 },
            { "bairro": "Praça 14 de Janeiro", "longitude": -60.0129391, "latitude": -3.1215387 },
            { "bairro": "Presidente Vargas", "longitude": -60.0302827, "latitude": -3.1198871 },
            { "bairro": "Puraquequara", "longitude": -59.8453182, "latitude": -3.0586602 },
            { "bairro": "Raiz", "longitude": -59.9984879, "latitude": -3.1254752 },
            { "bairro": "Redenção", "longitude": -60.0404007, "latitude": -3.0532877 },
            { "bairro": "Santa Etelvina", "longitude": -60.0030611, "latitude": -2.9857472 },
            { "bairro": "Santa Luzia", "longitude": -60.0049908, "latitude": -3.1405003 },
            { "bairro": "Santo Agostinho", "longitude": -60.0649764, "latitude": -3.0924321 },
            { "bairro": "Santo Antônio", "longitude": -60.0447373, "latitude": -3.1159486 },
            { "bairro": "São Francisco", "longitude": -60.0057133, "latitude": -3.1092408 },
            { "bairro": "São Geraldo", "longitude": -60.0267097, "latitude": -3.1078082 },
            { "bairro": "São Jorge", "longitude": -60.0387102, "latitude": -3.1076222 },
            { "bairro": "São José Operário", "longitude": -59.9479207, "latitude": -3.0679738 },
            { "bairro": "São Lázaro", "longitude": -59.9955978, "latitude": -3.1407527 },
            { "bairro": "São Raimundo", "longitude": -60.0418462, "latitude": -3.1246412 },
            { "bairro": "Tancredo Neves", "longitude": -59.9424976, "latitude": -3.0544395 },
            { "bairro": "Tarumã", "longitude": -60.0606392, "latitude": -3.0078867 },
            { "bairro": "Vila Buriti", "longitude": -59.9651035, "latitude": -3.1402698 },
            { "bairro": "Vila da Prata", "longitude": -60.0476284, "latitude": -3.1072574 },
            { "bairro": "Zumbi dos Palmares", "longitude": -59.9479151, "latitude": -3.0811377 }
    ]

@transaction.atomic()
def run():
    try:
        for i in bairros_manaus:
            print(i)
            bairro = models.Bairro(
                nome=i['bairro'],
                longitude=i['longitude'],
                latitude=i['latitude']
            )
            bairro.save()
        print('Bairros salvos')
    except Exception as e:
        print(str(e))