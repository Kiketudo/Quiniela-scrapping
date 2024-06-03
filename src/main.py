from partido import Partido
from link import Links
from quiniela import Quiniela

simulacion = dict()
datos = Quiniela.obtenQuiniela()
primera= Links.obtieneLinks("https://www.besoccer.com/competition/primera_division")
segunda= Links.obtieneLinks("https://www.besoccer.com/competition/segunda_division")
partidos ={**primera,**segunda} 
print (partidos)
for partido in datos[0]['partidos']:
        local=partido["local"]
        visitante = partido["visitante"]
        simulacion[local+"-"+visitante]= Partido.simula(partidos[Quiniela.traduce(local)]+"/analysis") 

print (simulacion)
for i in simulacion:
        print(i+":"+simulacion[i])
        
   