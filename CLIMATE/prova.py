import pandas as pd
import numpy as np
import plotly_express as px

'''
# Climate Change V 1.0
Interactive web app to assess energy consumption per country
'''
df=pd.read_csv("/Users/dodo/Desktop/CLIMATE/country_energy.csv")

country="Australia"
years = range(1960,2016)
#emissions= df.iloc[country,4:]
#t.write(emissions)
lista_paesi=df['Country Name']

lista=lista_paesi.values.tolist()
a=lista.index(country)
print(a+2)