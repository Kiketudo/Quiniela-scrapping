import http.client
from bs4 import BeautifulSoup
from random import randint


class Partido:
    
    @staticmethod
    def simula(url):
        conn = http.client.HTTPSConnection("www.besoccer.com")
        payload = ""

        headers = {
            'authority': "www.besoccer.com",
            'accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            'accept-language': "es-ES,es;q=0.9,en;q=0.8",
            'cache-control': "max-age=0",
            'cookie': "_ga_5PSWF822NW=GS1.1.1674577454.1.1.1674577668.18.0.0; _fbp=fb.1.1674577674964.332168671; _gid=GA1.2.125546551.1676551719; _ga_HZYHXD4GZ0=GS1.1.1676551718.2.1.1676552082.0.0.0; _ga=GA1.2.229469835.1674577454",
            'if-modified-since': "Thu, 16 Feb 2023 12:54:42 GMT",
            'referer': "https://www.besoccer.com/match/girona-fc/almeria/202349624",
            'sec-ch-ua': "^\^Chromium^^;v=^\^110^^, ^\^Not",
            'sec-ch-ua-mobile': "?0",
            'sec-ch-ua-platform': "^\^Windows^^",
            'sec-fetch-dest': "document",
            'sec-fetch-mode': "navigate",
            'sec-fetch-site': "same-origin",
            'sec-fetch-user': "?1",
            'upgrade-insecure-requests': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
            }
        conn.request("GET", url, payload, headers)

        res = conn.getresponse()
        data = res.read()

        # print(data.decode("utf-8"))
        # 896
        '''
        class MyHTMLParser(HTMLParser):
            def __init__(self):
                super().__init__()
                self.in_price_tag = False
                self.divs_text = []  # Initialize an empty list to store div text
            def handle_starttag(self, tag, attrs):
                attrs = dict(attrs)
                if tag == 'div':
                    if attrs.get('class') == 'elo-label team1-c':
                        self.in_price_tag = True
                        print("Encountered class :", attrs.get('class'))
                    else:
                        self.in_price_tag = False

            def handle_data(self, data):
                #print("Print data", data)
                if self.in_price_tag:
                    print("Print data", data)
                    self.price = data
                    self.divs_text.append(data)

        parser = MyHTMLParser()
        parser.feed(data.decode("utf-8"))
        #print(parser.divs_text)
        print(parser.price)
        '''
        analis = dict()
        clases = ["elo-label team1-c", "elo-label color-grey2", "elo-label team2-c"]
        for i in clases:
            soup = BeautifulSoup(data, "html.parser")
            arr = soup.find("div", class_=i).findAll("div")
            analis[BeautifulSoup(str(arr[1]), "html.parser").find("div").text] = float(BeautifulSoup(
                str(arr[0]), "html.parser").find("div").text.replace("%", ""))
        print(analis)
        value = randint(0, 100)
        print(value)
        y = dict(sorted(analis.items(), key=lambda item: item[1]))
        print(y)
        l1 = list()
        for i in y:
            l1.append(i)
        print(l1)

        segundoNum = round(y[l1[1]])+round(y[l1[0]])
        if value <= round(y[l1[0]]):
            resultado=l1[0]
            print(l1[0])
        elif round(y[l1[0]]) < value <= segundoNum:
            resultado=l1[1]
            print(l1[1])
        else:
            resultado=l1[2]
            print(l1[2])

        return resultado
