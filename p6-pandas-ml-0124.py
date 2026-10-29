import pandas as pd
import numpy as np

serie_amigos=["Pedro","Morgan","Farfan","Adrian","Jesse","Eliseo","Mario"]
print("---- Serie listado de amigos NC 0124")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print("--- Serie listado valor de billetes MX   NC 0124")
billetes=pd.Series(serie_billetes)
print(billetes)

serie_billetes=[20,50,100,200,500,1000]
serie_bletres=["veinte","cincuenta","cien","dosciento","quinientos","mil"]
print("--- Serie listado nombre y valor de billetes MX   NC 0124")
tablabilletes=pd.Series(serie_billetes,serie_bletres)
print(tablabilletes)
#diccionario dataframe
# diccionario de valor monedas y nombre
dic_monedas={
      "serie_billetes":[20,50,100,200,500,1000],
      "serie_bletres":["veinte","cincuenta","cien","dosciento","quinientos","mil"]
}

tablabilletes=pd.DataFrame(dic_monedas,index=("A","B","C","D","E","F"))
print(tablabilletes)

print("Casa de cambio de Alan Romero NC 0124")