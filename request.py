import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'edad':1, 'grado':1, 'P2':1, 'P6':1, 'P12':1, 'P14':1, 'P21':1, 'P26':1, 'Intra_Cuali':1,'P1':1, 'P4':1,'P18':1, 'P23':1, 'P28':1, 'P30':1, 'Inter_Cuali':1, 'P5':1, 'P8':1, 'P9':1,'P17':1, 'P27':1, 'P29':1, 'Estres_Final':1, 'Estres_Cuali':1, 'P10':1, 'P13':1,'P16':1, 'P19':1, 'P22':1, 'P24':1, 'Adap_Cuali':1, 'P3':1, 'P7':1, 'P11':1, 'P15':1,'P20':1, 'P25':1, 'Impre_Cuali':1, 'Test_Total':1, 'Total_Cuanti':1,'Prom_Ponderado':1 })
print(r.json())
