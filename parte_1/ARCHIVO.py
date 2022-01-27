import pandas as pd 
import json
import csv

def obtenerPorcentaje(tipo, array, total, f):
    for fila in array:
        porcentaje= int(fila)/int(total)
        f.append('%s' % round(porcentaje, 2))
    fila_completa= "%s, " % tipo + ', '.join(f) + ", %s" % total
    return fila_completa

fieldnames = ("Nombre","Valor", "Tipo")
df= pd.read_csv("archivoCsv.csv", header=None, 
names=["Nombre", "Valor","Tipo"])
df.to_json("test.json", orient = "records")

suma_fila_1=[]
fila_1=[]
f_1=[]
total_1=0

suma_fila_2=[]
fila_2=[]
f_2=[]
total_2=0

suma_fila_3=[]
fila_3=[]
f_3=[]
total_3=0

suma_fila_4=[]
fila_4=[]
f_4=[]
total_4=0

tipo=0
fila_1_completa=""
fila_2_completa=""
fila_3_completa=""
fila_4_completa=""
with open("test.json", "r") as acv_json:
    df_json=json.load(acv_json)
    for r in df_json:
        if r["Tipo"] == 1:
            suma_fila_1.append(r["Valor"])
            fila_1.append('%s' % r["Valor"]) 
        if r["Tipo"] == 2:
            suma_fila_2.append(r["Valor"])
            fila_2.append('%s' % r["Valor"]) 
        if r["Tipo"] == 3:
            suma_fila_3.append(r["Valor"])
            fila_3.append('%s' % r["Valor"]) 
        if r["Tipo"] == 4:
            suma_fila_4.append(r["Valor"])
            fila_4.append('%s' % r["Valor"]) 
            
    total_1=sum(suma_fila_1)
    total_2=sum(suma_fila_2)
    total_3=sum(suma_fila_3)
    total_4=sum(suma_fila_4)
    fila_1_completa=obtenerPorcentaje(1, fila_1, total_1, f_1)
    fila_2_completa=obtenerPorcentaje(2, fila_2, total_2, f_2)
    fila_3_completa=obtenerPorcentaje(3, fila_3, total_3, f_3)
    fila_4_completa=obtenerPorcentaje(4, fila_4, total_4, f_4)
    envio=[
            [fila_1_completa],
            [fila_2_completa],
            [fila_3_completa],
            [fila_4_completa]
    ]
    file_name="cualquiera.csv"
    file = open(file_name, "w", )
    with file:
        writer = csv.writer(file)
        writer.writerows(envio)
    file.close()



        
