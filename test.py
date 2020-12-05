import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'Date Posted'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    #data = pd.read_csv(DATA_URL, nrows=nrows)
    #data = pd.read_csv("statement.csv",skiprows=9,nrows=116)
    data = pd.read_csv("statement.csv")

    # First Bank Card	Transaction Type	Date Posted	 Transaction Amount	Description
    data = pd.read_csv("statement.csv",
        header=0,
        names=["First Bank Card",	"Transaction Type",	"Date Posted",	 "Transaction Amount", "Description"],
        parse_dates=["Date Posted"])    
    #data['Date Posted'] = pd.to_datetime(data['Date Posted'], format="%Y%m%d")
    #lowercase = lambda x: str(x).lower()
    #data.rename(lowercase, axis='columns', inplace=True)
    #data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

data_load_state = st.text('Loading data...')
data = load_data(10000)
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Number of txns by month')
hist_values = np.histogram(data[DATE_COLUMN].dt.month, bins=12, range=(1,12))[0]
st.bar_chart(hist_values)

st.subheader('Number of txns by bank card')
hist_values = np.histogram(data["First Bank Card"], bins=12, range=(1,12))[0]
st.bar_chart(hist_values)

# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)