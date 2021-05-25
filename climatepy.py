import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px
from countryinfo import CountryInfo
from geopy.exc import GeocoderTimedOut
from geopy.geocoders import Nominatim
import plotly.graph_objects as go


'''
# Climate Change V 1.0
Interactive web app to assess energy consumption per country.  
There could be discrepancies due to insufficient data recording for some years and/or countries
  
  
  
'''

energy_df=st.cache(pd.read_csv)("country_energy.csv") #1st file energy consumption per capita
fossil_df=st.cache(pd.read_csv)("fossil.csv") #2nd file fossil fuel energy %
co2_df=st.cache(pd.read_csv)("CO2.csv") #3rd file CO2 emissions
renewables_df=st.cache(pd.read_csv)("RENEWABLES.csv") #4th file renewables energy %

country_list=energy_df['Country Name'].values.tolist() #each df has the same country list

#data selection
countries=st.sidebar.multiselect('Country',country_list)
period=st.sidebar.slider("Period",1960,2020, (1960,2020))
min_year=period[0]
max_year=period[1]
'''
You have selected data regarding:
'''
for country in countries:
    st.write("-" + country)
st.write("between", min_year, "and", max_year)

#data retrieval
years_range = range(min_year, max_year+1)
country_indexes = []
for country in countries:
    country_indexes.append(country_list.index(country))
min_year_index = min_year-1956 #index for 1960 is 4; for '61 is 5; for '62 is 6; etc
max_year_index = max_year-1956 #same as above
energy = energy_df.iloc[country_indexes, min_year_index:max_year_index+1]
energy = energy.T #inverts axes
energy_mult = []
for country in countries:
    energy_mult.append((energy_df.iloc[country_list.index(country), min_year_index:max_year_index+1]).tolist())
st.write(energy_mult)
energysum=[]
for country in energy_mult:
    sumens = 0
    for year in country:
        if np.isnan(year) == False:
            sumens += year
    energysum.append(sumens)
st.write('aaaaaa')
st.write(energysum)
fossil = fossil_df.iloc[country_indexes, min_year_index:max_year_index+1]
co2 = co2_df.iloc[country_indexes, min_year_index:max_year_index+1]
renewables = renewables_df.iloc[country_indexes, min_year_index:max_year_index+1]

#city capital lat lon map
def findGeocode(city): 
    try: 
        geolocator = Nominatim(user_agent="climate") 
        return geolocator.geocode(city) 
    except GeocoderTimedOut: 
        return findGeocode(city)
cap_list=[]
lat=[]
lon=[]
iso=[]
value=[]
for country in countries:
    try:
        capital=CountryInfo(country)
        capital=capital.capital()
        cap_list.append(capital)
        code=CountryInfo(country)
        code=code.iso(3)
        iso.append(code)
        a=1
        value.append(a)
    except:
        pass
for i in cap_list:
    loc=findGeocode(i)
    lat.append(loc.latitude)
    lon.append(loc.longitude)
st.write(lat)
st.write(lon)
df_location=pd.DataFrame(list(zip(lat,lon)),columns=["lat","lon"])
st.write(country_list)
df_coucode=pd.DataFrame(list(zip(iso,countries,energysum)),columns=["iso","country","value"])
st.write(df_coucode)
st.sidebar.map(df_location)
figcol=go.Figure(data=go.Choropleth(
    locations=df_coucode['iso'],
    z=df_coucode['value'],
    #color="Blue",
))
st.write(figcol)

#graphs
energy_graph=px.line(x=years_range, y=energy_mult) #color=countries)
energy_graph.update_layout(
    title="Energy Consumption (as kg of oil equivalent) Per Capita In "+ str(countries[0:-1]),
    xaxis_title="period",
    yaxis_title="energy use",
    #color_title="country"
)
st.plotly_chart(energy_graph)
my_expander = st.beta_expander('Show more')
my_expander.write('INFO DA METTERE')
'''
&nbsp;
'''
fossil_graph=px.line(x=years_range, y=fossil)
fossil_graph.update_layout(
    title="Percentage Of Energy Derived From Fossil Fuels In " + countries,
    xaxis_title="period",
    yaxis_title="%",
)
st.plotly_chart(fossil_graph)
my_expander = st.beta_expander('Show more')
my_expander.write('INFO DA METTERE')
'''
&nbsp;
'''
renewables_graph=px.line(x=years_range, y=renewables)
renewables_graph.update_layout(
    title="Percentage Of Energy Derived From Renewable Sources In " + countries,
    xaxis_title="period",
    yaxis_title="%"
)
st.plotly_chart(renewables_graph)
my_expander = st.beta_expander('Show more')
my_expander.write('INFO DA METTERE')
''' 
&nbsp;
'''
co2_graph=px.line(x=years_range, y=co2)
co2_graph.update_layout(
    title="CO2 Emissions (in Kt) In " + countries,
    xaxis_title="period",
    yaxis_title="emissions",
)
st.plotly_chart(co2_graph)
my_expander = st.beta_expander('Show more')
my_expander.write('INFO DA METTERE')
