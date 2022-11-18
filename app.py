import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/slow312/dashboard-streamlit/main/data/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv')

# Fix column names 
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
df.columns = df.columns.str.lower()
df.columns.values

#### Put together dataframes ####
df_race = df.filter(['race_ethnicity','total_number_of_hiv_diagnoses','total_number_of_aids_diagnoses'])
# Get rid of irrelevant rows
df_race = df_race[df_race['total_number_of_hiv_diagnoses'].apply(lambda x: str(x).isdigit())]
df_race = df_race[df_race['total_number_of_aids_diagnoses'].apply(lambda x: str(x).isdigit())]
df_race = df_race[df_race['race_ethnicity'].str.contains('Unknown')==False ]
# Convert columns to integers
df_race['total_number_of_hiv_diagnoses'] = df_race['total_number_of_hiv_diagnoses'].astype(int)
df_race['total_number_of_aids_diagnoses'] = df_race['total_number_of_aids_diagnoses'].astype(int)
# Group by race and get sum of each group
df_race = df_race.groupby('race_ethnicity').sum()

df_year = df.filter(['year','total_number_of_hiv_diagnoses','total_number_of_aids_diagnoses'])
# Get rid of irrelevant rows
df_year = df_year[df_year['total_number_of_hiv_diagnoses'].apply(lambda x: str(x).isdigit())]
df_year = df_year[df_year['total_number_of_aids_diagnoses'].apply(lambda x: str(x).isdigit())]
# Convert columns to integers
df_year['total_number_of_hiv_diagnoses'] = df_year['total_number_of_hiv_diagnoses'].astype(int)
df_year['total_number_of_aids_diagnoses'] = df_year['total_number_of_aids_diagnoses'].astype(int)
# Group by year and get sum of each group
df_year = df_year.groupby('year').sum()

#### Putting together streamlit dashboard ####
st.title('HIV/AIDS Diagnoses by Year and Race/Ethnicity')

st.subheader('HIV/AIDS Diagnoses by Race/Ethnicity')
st.text('This dataframe and chart shows the number of HIV/AIDS diagnoses by Race/Ethnicity')
st.dataframe(df_race)
st.bar_chart(df_race)

st.subheader('HIV/AIDS Diagnoses by Year')
st.text('This dataframe and chart shows the number of HIV/AIDS diagnoses by Year')
st.dataframe(df_year)
st.line_chart(df_year)

st.subheader('This is the code used for the dataset')
st.dataframe(df)
code = '''
import streamlit as st
import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/slow312/dashboard-streamlit/main/data/HIV_AIDS_Diagnoses_by_Neighborhood__Age_Group__and_Race_Ethnicity.csv')

# Fix column names 
df.columns = df.columns.str.replace('[^A-Za-z0-9]+', '_')
df.columns = df.columns.str.lower()
df.columns.values

#### Put together dataframes ####
df_race = df.filter(['race_ethnicity','total_number_of_hiv_diagnoses','total_number_of_aids_diagnoses'])
# Get rid of irrelevant rows
df_race = df_race[df_race['total_number_of_hiv_diagnoses'].apply(lambda x: str(x).isdigit())]
df_race = df_race[df_race['total_number_of_aids_diagnoses'].apply(lambda x: str(x).isdigit())]
df_race = df_race[df_race['race_ethnicity'].str.contains('Unknown')==False ]
# Convert columns to integers
df_race['total_number_of_hiv_diagnoses'] = df_race['total_number_of_hiv_diagnoses'].astype(int)
df_race['total_number_of_aids_diagnoses'] = df_race['total_number_of_aids_diagnoses'].astype(int)
# Group by race and get sum of each group
df_race = df_race.groupby('race_ethnicity').sum()

df_year = df.filter(['year','total_number_of_hiv_diagnoses','total_number_of_aids_diagnoses'])
# Get rid of irrelevant rows
df_year = df_year[df_year['total_number_of_hiv_diagnoses'].apply(lambda x: str(x).isdigit())]
df_year = df_year[df_year['total_number_of_aids_diagnoses'].apply(lambda x: str(x).isdigit())]
# Convert columns to integers
df_year['total_number_of_hiv_diagnoses'] = df_year['total_number_of_hiv_diagnoses'].astype(int)
df_year['total_number_of_aids_diagnoses'] = df_year['total_number_of_aids_diagnoses'].astype(int)
# Group by year and get sum of each group
df_year = df_year.groupby('year').sum()
'''
st.code(code, language='python')


















