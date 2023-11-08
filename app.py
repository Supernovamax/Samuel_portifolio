import streamlit as st
import time
import pandas as pd
import numpy as np
import torch
import requests
from transformers import pipeline

st.set_page_config(page_title="Samuel Portfolio", page_icon="📈")


with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Samuel's Portfolio")
    choice = st.radio("Navigation", ["About Sam","Uber Project", "Plotting", "Attached files", "Contact" ])
    st.info("This project application helps you understand more about Samuel and his capabilities in detail😊.")

if choice == "About Sam":
    st.title("Hi am sam")
    
if choice == "Uber Project": 
    st.title('Uber pickups in NYC')

    DATE_COLUMN = 'date/time'
    DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
    
    @st.cache_data
    def load_data(nrows):
        data = pd.read_csv(DATA_URL, nrows=nrows)
        lowercase = lambda x: str(x).lower()
        data.rename(lowercase, axis='columns', inplace=True)
        data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
        return data
    
    # Create a text element and let the reader know the data is loading.
    data_load_state = st.text('Loading data...')
    # Load 10,000 rows of data into the dataframe.
    data = load_data(10000)
    # Notify the reader that the data was successfully loaded.
    data_load_state.text('Loading data...done!')
    data_load_state.text("Done! (using st.cache_data)")
    
    if st.checkbox('Show raw data'):
        st.subheader('Raw data')
        st.write(data)
    
    st.subheader('Number of pickups by hour')
    
    hist_values = np.histogram(
        data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
    st.bar_chart(hist_values)
    
    
    hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
    filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
    st.subheader(f'Map of all pickups at {hour_to_filter}:00')
    st.map(filtered_data)

if choice == "Plotting":
    
    st.markdown("# Plotting Demo")
    st.sidebar.header("Plotting Demo")
    st.write(
        """This demo illustrates a combination of plotting and animation with
    Streamlit. We're generating a bunch of random numbers in a loop for around
    5 seconds. Enjoy!"""
    )
    
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)
    
    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)
    
    progress_bar.empty()
    
    # Streamlit widgets automatically run the script from top to bottom. Since
    # this button is not connected to any other logic, it just causes a plain
    # rerun.
    st.button("Re-run")

if choice == "Contact":
    st.title("You can contact me via:")    
    
    API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
    headers = {"Authorization": "Bearer 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"}
    
    def query(payload):
    	response = requests.post(API_URL, headers=headers, json=payload)
    	return response.json()
    	
    output = query({
    	"inputs": "Can you please let us know more details about your ",
    })

if choice == "Attached files": 
    st.title("Download final project report here")
