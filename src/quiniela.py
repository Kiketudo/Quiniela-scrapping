import http.client
import pandas as pd
import json

class Quiniela:
    def obtenQuiniela():
        conn = http.client.HTTPSConnection("www.loteriasyapuestas.es")

        payload = ""

        headers = {
            'authority': "www.loteriasyapuestas.es",
            'accept': "application/json, text/javascript, */*; q=0.01",
            'accept-language': "es-ES,es;q=0.9,en;q=0.8",
            'content-type': "application/json",
            'origin': "https://juegos.loteriasyapuestas.es",
            'referer': "https://juegos.loteriasyapuestas.es/",
            'sec-ch-ua': "^\^Chromium^^;v=^\^110^^, ^\^Not",
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': "^\^Windows^^",
            'sec-fetch-dest': "empty",
            'sec-fetch-mode': "cors",
            'sec-fetch-site': "same-site",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            }

        conn.request("GET", "/servicios/fechav3?game_id=LAQU&fecha_sorteo=20230312", payload, headers)
        res = conn.getresponse()
        data = res.read()
        datos  = json.loads(data)
        return datos
        
        for partido in datos[0]['partidos']:
            local=partido["local"]
            visitante=partido["visitante"]
            print(local, visitante)
    def traduce(nombre):
        if nombre== "Real Sociedad":
            return "R. Sociedad"
        elif nombre== 'Betis':
            return "Real Betis"
        elif nombre== "Athletic Club":
            return "Athletic"
        elif nombre== "At. Madrid":
            return "Atlético"
        elif nombre== "Alavés":
            return "Deportivo Alavés"
        elif nombre== "Lugo":
            return "CD Lugo"
        elif nombre== "Ibiza":
            return "UD Ibiza"
        elif nombre== "Lugo":
            return "CD Lugo"
        elif nombre== "Andorra":
            return "FC Andorra"
        elif nombre== "Sporting":
            return "Real Sporting"
        elif nombre== "R. Zaragoza":
            return "Real Zaragoza"
        elif nombre== "Valladolid":
            return "Real Valladolid"
        elif nombre== "Cartagena":
            return "FC Cartagena"
        
        else:
            return nombre

#Quiniela.obtenQuiniela()
#print (Quiniela.traduce("Deprotivo Alav�s"))
