import streamlit as st
import pandas as pd
import numpy as np
import plotly_express as px

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
country=st.sidebar.selectbox('Country',country_list)
period=st.sidebar.slider("Period",1960,2020, (1960,2020))
min_year=period[0]
max_year=period[1]
st.write("You selected data regarding", country, "between", min_year, "and", max_year)

#data retrieval
years_range = range(min_year, max_year+1)
country_index = country_list.index(country)
min_year_index = min_year-1956 #index for 1960 is 4; for '61 is 5; for '62 is 6; etc
max_year_index = max_year-1956 #same as above
energy = energy_df.iloc[country_index, min_year_index:max_year_index+1]
fossil = fossil_df.iloc[country_index, min_year_index:max_year_index+1]
co2 = co2_df.iloc[country_index, min_year_index:max_year_index+1]
renewables = renewables_df.iloc[country_index, min_year_index:max_year_index+1]

#graphs
energy_graph=px.line(x=years_range, y=energy)
energy_graph.update_layout(
    title="Energy Consumption (as kg of oil equivalent) Per Capita In " + country,
    xaxis_title="period",
    yaxis_title="energy use",
)
st.plotly_chart(energy_graph)
my_expander = st.beta_expander('Show more')
my_expander.write('INFO DA METTERE')
'''
&nbsp;
'''
fossil_graph=px.line(x=years_range, y=fossil)
fossil_graph.update_layout(
    title="Percentage Of Energy Derived From Fossil Fuels In " + country,
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
    title="Percentage Of Energy Derived From Renewable Sources In " + country,
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
    title="CO2 Emissions (in Kt) In " + country,
    xaxis_title="period",
    yaxis_title="emissions",
)
st.plotly_chart(co2_graph)
my_expander = st.beta_expander('Show more')
my_expander.write('INFO DA METTERE')