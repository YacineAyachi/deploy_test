
# DATA_URL = ('https://univlyon2fr-my.sharepoint.com/:f:/g/personal/yayachi_univ-lyon2_fr/EmWXiTs2d_xGt573tGCT52YBPJ5GhnbINEbjv9gONCx_3g?e=mU2xYP')
import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'

data = pd.read_csv('neufs.csv')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
