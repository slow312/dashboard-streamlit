import streamlit as st
import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/slow312/dashboard-streamlit/main/data/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv')
df.columns

#### Dataframe by Race ####

# Get relevant columns 
df_race = df.filter(['RACE/ETHNICITY','TOTAL NUMBER OF HIV DIAGNOSES','TOTAL NUMBER OF AIDS DIAGNOSES'])
# Get rid of irrelevant rows
df_race = df_race[df_race['TOTAL NUMBER OF HIV DIAGNOSES'].apply(lambda x: str(x).isdigit())]
df_race = df_race[df_race['TOTAL NUMBER OF AIDS DIAGNOSES'].apply(lambda x: str(x).isdigit())]
df_race = df_race[df_race['RACE/ETHNICITY'].str.contains('Unknown')==False ]
# Convert columns to integers
df_race['TOTAL NUMBER OF HIV DIAGNOSES'] = df_race['TOTAL NUMBER OF HIV DIAGNOSES'].astype(int)
df_race['TOTAL NUMBER OF AIDS DIAGNOSES'] = df_race['TOTAL NUMBER OF AIDS DIAGNOSES'].astype(int)
# Group by race and get sum of each group
df_race = df_race.groupby('RACE/ETHNICITY').sum()
len(df_race)

#### Dataframe by Year ####



# Turn groupby into Dataframe
df_race_final.columns






df_race['TOTAL NUMBER OF AIDS DIAGNOSES'] = df_race['TOTAL NUMBER OF AIDS DIAGNOSES'].astype(int)
df_race = df_race.groupby('RACE/ETHNICITY').sum()
df_race




df_NBHD = df.drop(['hiv_diagnoses_num_per_100k','concurrent_hiv_aids_among_all','aids_diagnoses_num_per_100k','borough'], axis = 1)

## Header ##
st.title('HIV/AIDS Diagnoses by Neighborhood, Age Group, and Race/Ethnicity')

## HIV/AIDS Diagnoses by Neighborhood ##
df_NBHD = df.drop(['race','age'], axis = 1)
st.subheader('HIV/AIDS Diagnoses by Neighborhood')

st.text('This dataframe and chart shows the number of HIV/AIDS diagnoses by neightborhood from 2020 to 2010')
st.dataframe(df_NBHD)

df_NBHD = df_NBHD.drop(['hiv_diagnoses_num_per_100k','concurrent_hiv_aids_among_all','aids_diagnoses_num_per_100k','borough'], axis = 1)
st.line_chart(df_NBHD)

## HIV/AIDS Diagnoses by Race ##
df_race = df.drop(['neighborhood','age'], axis =1)
st.subheader('HIV/AIDS Diagnoses by Race')

st.text('This dataframe and chart shows the number of HIV/AIDS diagnoses by race from 2020 to 2010')
st.dataframe(df_race)

df_race = df_race.drop(['hiv_diagnoses_num_per_100k','concurrent_hiv_aids_among_all','aids_diagnoses_num_per_100k','borough'], axis = 1)
st.bar_chart(df_race)

st.subheader('Code for this dashboard')
code = '''
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('dashboard-streamlit\data\HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv')

## Header ##
st.title('HIV/AIDS Diagnoses by Neighborhood, Age Group, and Race/Ethnicity')

## HIV/AIDS Diagnoses by Neighborhood ##
df_NBHD = df.drop(['race','age'], axis = 1)
st.subheader('HIV/AIDS Diagnoses by Neighborhood')

st.text('This dataframe and chart shows the number of HIV/AIDS diagnoses by neightborhood from 2020 to 2010')
st.dataframe(df_NBHD)

df_NBHD = df_NBHD.drop(['hiv_diagnoses_num_per_100k','concurrent_hiv_aids_among_all','aids_diagnoses_num_per_100k','borough'], axis = 1)
st.bar_chart(df_NBHD)

## HIV/AIDS Diagnoses by Race ##
df_race = df.drop(['neighborhood','age'], axis =1)
st.subheader('HIV/AIDS Diagnoses by Race')

st.text('This dataframe and chart shows the number of HIV/AIDS diagnoses by race from 2020 to 2010')
st.dataframe(df_race)

df_race = df_race.drop(['hiv_diagnoses_num_per_100k','concurrent_hiv_aids_among_all','aids_diagnoses_num_per_100k','borough'], axis = 1)
st.bar_chart(df_race)
'''
st.code(code, language='python')















