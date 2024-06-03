import http.client
from bs4 import BeautifulSoup

class Links:
    def obtieneLinks(url):
        conn = http.client.HTTPSConnection("www.besoccer.com")
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
        conn.request("GET", url, payload)
        res = conn.getresponse()
        data = res.read()
        soup = BeautifulSoup(data,"html.parser")
        arr = soup.find("div", class_ = "panel-body p0 match-list-new" ).findAll("a")
        partidos = dict()

        for i in arr:
            aux = str(i)
            local=BeautifulSoup(aux,"html.parser").find("div",class_="name").text
            partidos[local]=i.get("href")
        #print (partidos)
        return partidos
        
#Links.obtieneLinks("https://www.besoccer.com/competition/segunda_division")