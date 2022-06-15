

# load library
import streamlit as st
import numpy as np
import pandas as pd
import pandas_profiling

from pandas_datareader import data as pdr
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

import math
import statistics
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt
import yfinance as yf
import datetime
from data_statistics import DSSC_FC_MVP_Visualization as vz

# print title of web app
st.title("Financial Consultation Stock Market Analysis and Prediction")
st.markdown(">Welcome to the Website")

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')

# Load data from yahoo finance.
start=dt.date(2021,1,1)
end=dt.date(2021,12,31)
data=pdr.get_data_yahoo("IBM", start, end)

data1=pdr.get_data_yahoo("MSFT", start, end)

#fill nan vale with next value within columns
data.fillna(method="ffill",inplace=True)

# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')


def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
     return df.to_csv().encode('utf-8')

csv = convert_df(data)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='data.csv',
     mime='text/csv',
 )


# create checkbox
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)




st.subheader('A complete Profile Report of data')
pr=ProfileReport(data)
st_profile_report(pr)



