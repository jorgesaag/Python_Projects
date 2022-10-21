import pandas as pd

#Evaluar los Ejes Equivalentes, W18 (ESAL Equivalent Single Axle Load), y generar
#los posibles escenarios de cargas de tránsito para un pavimento que se empleará en
#un camino TIPO A4 con las siguientes características:

#Camino de 2 carriles (3.5m) y 1 acotamiento externo (2.5m) y acotamiento interno (1m).
#Velocidad de proyecto de 110 km/h.
#TPDA de 31759 veh/día por sentido.
#Carriles por sentido: 2.
#Periodo de diseño n = 20 años
#Tasa anual de crecimiento de r = 2.5%.

data = {"Tipo de vehículo" : ["A2 (4 Neum)", "B2 (6 Neum)", "C2 (6 Neum)", "C3 (10 Neum)",
        "T3-S2 (18 Neum)", "T3-S3 (22 Neum)", "T3-S2-R4 (34 Neum)"], "%" : [70.1, 2.3, 6.1, 3.0, 11.4, 3.9, 3.2]}

df = pd.DataFrame(data)

print(df)