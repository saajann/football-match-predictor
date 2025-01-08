import streamlit as st
import pandas as pd

table = pd.read_csv('data/serie_a_league_table.csv')

features = ['team', 'wins', 'draws', 'losses', 'points']
table = table[features]

st.title('Serie A League Table')
st.table(table.reset_index(drop=True))