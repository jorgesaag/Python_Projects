import pandas as pd
import csv

df = pd.read_csv (r'C:\Users\Jorge Salinas\Desktop\Model_Importation_GOR0470E22_PK_CHAPA_Slabs.csv')
list = df['Slabs'].tolist()
list_wo_char = []

for i in list:
    numeric_filter = filter(str.isdigit, i)
    numeric_string = "".join(numeric_filter)
    list_wo_char.append(numeric_string)

with open('Model_Importation_GOR0470E22_PK_CHAPA_Slabs_solonúmeros.csv', 'w', newline='') as csv_1:
  csv_out = csv.writer(csv_1)
  csv_out.writerows([list_wo_char[index]] for index in range(0, len(list_wo_char)))


