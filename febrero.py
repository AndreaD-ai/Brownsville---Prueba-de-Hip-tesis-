import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import scipy.stats as ss
from scipy.special import ndtri

#Se le el csv de Fronteras, que contiene a US-Canada Border y a US-Mexico Border del año 1996 a febrero de 2020
fronteras= pd.read_csv('front2.csv')

#Se cambia el formato de la fecha
fronteras["Date"]= pd.to_datetime(fronteras["Date"], format ="%m/%d/%Y")

#Se seleccionan los datos que se desean, en nuestro caso la frontera de
#Brownsville y Pedestrians
es_Brow=fronteras["Port Name"]== "Brownsville"
es_PD=fronteras["Measure"]=="Pedestrians"

#Se seleccionan los años 2000 al 2008
es_2009=fronteras["Date"].dt.strftime("%Y")=="2009"
es_2008=fronteras["Date"].dt.strftime("%Y")=="2008"
es_2007=fronteras["Date"].dt.strftime("%Y")=="2007"
es_2006=fronteras["Date"].dt.strftime("%Y")=="2006"
es_2005=fronteras["Date"].dt.strftime("%Y")=="2005"
es_2004=fronteras["Date"].dt.strftime("%Y")=="2004"
es_2003=fronteras["Date"].dt.strftime("%Y")=="2003"
es_2002=fronteras["Date"].dt.strftime("%Y")=="2002"
es_2001=fronteras["Date"].dt.strftime("%Y")=="2001"
es_2000=fronteras["Date"].dt.strftime("%Y")=="2000"

#Se seleccionan los meses de enero, febrero y marzo 
es_enero=fronteras["Date"].dt.strftime("%m")=="01"
es_febrero=fronteras["Date"].dt.strftime("%m")=="02"
es_marzo=fronteras["Date"].dt.strftime("%m")=="03"

#Se seleccionan los años 2000-2008, febrero, Brownsville y Pedestrians
primer_mes = fronteras[es_Brow & (es_2008 | es_2007 | es_2006 | es_2005 | es_2004 | es_2003 | es_2002 | es_2001 | es_2000) & es_febrero &es_PD]
#print(primer_mes)

##FEBRERO
#Significacia del 10%
#Valor en la tabla -1.28

#media de 2000-2008 febrero
print("Media 2000-2008")
dd = primer_mes["Value"].mean()
print(dd)
print(" ")

#Desviación estándar de 2000-2008 febrero
print("Desviación Estándar")
ds = primer_mes["Value"].std()
print(ds)
print(" ")

#n
print("n")
dc = primer_mes["Value"].count()
print(dc)
print(" ")


#Raíz de n
print("Raíz n")
dnfin = dc**(.5)
print(dnfin)
print(" ")


print("Valor de f(z)")
a = ss.norm.cdf(-1.28)
print(a)
print(" ")

print("Valor de z")
b = ndtri(0.10027256795444206)
print(b)
print(" ")

#Se considera 230000.5 como hipoteisis alternativa
print("Valor crítico")
ffin = ((dd-230000.5)/(ds/dnfin))
print(ffin)
print(" ")


#Valor crítico = -0.01978173411585926 cae dentro de valor de z, por lo que la
#hipotesis es aceptada

x=primer_mes['Date']
y=primer_mes['Value']
plt.plot(x,y)
#plt.show()
plt.savefig('Brownsville - 2000-2008 - febrero.png')

