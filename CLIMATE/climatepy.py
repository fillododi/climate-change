import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

'''
# Climate Change V 1.0
Interactive web app to assess energy consumption per country
'''
dfa=st.cache(pd.read_csv)("country_energy.csv") #1st file energy consumption per capita
dfb=st.cache(pd.read_csv)("fossil.csv")#2nd file fossil fuel
dfc=st.cache(pd.read_csv)("CO2.csv")
#st.write(dfa)
lista_paesi=dfa['Country Name'] #it's the same list
lista=lista_paesi.values.tolist()
country=st.sidebar.selectbox('SELECT_COUNTRY',lista_paesi)
period=st.sidebar.slider("period",1960,2021, (1960,2021))
st.write(period)
firsty=period[0]
sndy=period[1]
st.write(firsty)
st.write(sndy)
#country=(country[0])->only if multiselect
years = range(firsty,sndy+1)
b=sndy
st.write(b)
a=lista.index(country)
emissionsa= dfa.iloc[a+2,4:(b+5)] #emission for dfa
emissionsb= dfb.iloc[a+2,4:(b+5)] #emission for dfb
emissionsc= dfc.iloc[a+2,4:(b+5)]#emissions CO2 dfc
figa=px.line(x=years, y=emissionsa) #it'd be useful to add a checkbox to display everything or only a part
figa.update_layout(
    title="Energy Consumption PC"+" "+country,
    xaxis_title="period",
    yaxis_title="emissions",
)#px.line, Line Plot with plotly.express
#Plotly Express is the easy-to-use, high-level interface to Plotly, which operates on a variety of types of data and produces easy-to-style figures. With px.line, each data point is represented as a vertex (which location is given by the x and y columns) of a polyline mark in 2D space.


st.plotly_chart(figa)
figb=px.line(x=years, y=emissionsb)
figb.update_layout(
    title="Fossil Fuel Consumption PC in"+" "+country,
    xaxis_title="period",
    yaxis_title="emissions",
)
st.plotly_chart(figb)

figc=px.line(x=years, y=emissionsc)
figc.update_layout(
    title="CO2 emissions in"+" "+country,
    xaxis_title="period",
    yaxis_title="emissions",
)
st.plotly_chart(figc)

#In questo grafico riusciamo a vedere quelle che sono le emissioni.

