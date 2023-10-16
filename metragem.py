# Digite uma metragem e veja isso em cm e mm:
import time
metragem = int(input("quantos metros? "))
centimetros = metragem*100
milimetro = metragem*1000
print(metragem, "metros tem", centimetros, "centimetros")
time.sleep(2)
print(metragem, "metros tem", milimetro, "milimetros")