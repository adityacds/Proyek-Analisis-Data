import streamlit as st
import pandas as pd
import plotly.express as px

data = pd.read_csv("./dataset/hour.csv") 

st.title("Bike Sharing Data Visualization")

# Sidebar Menu
st.sidebar.title("Menu Options")

visualization_option = st.sidebar.selectbox("Select Visualization", ["Total Rental Bikes Over Time", "Weather Distribution", "Humidity Distribution", "Rental Bikes by Month"])

show_raw_data = st.sidebar.checkbox("Show Raw Data")


# Raw Data
if show_raw_data:
    st.subheader("Raw Data")
    st.dataframe(data)

# Visualisasi Data
st.subheader("Data Visualization")

if visualization_option == "Total Rental Bikes Over Time":
    fig = px.line(data, x='dteday', y='cnt', title='Total Rental Bikes Over Time')
    st.plotly_chart(fig, use_container_width=True)

elif visualization_option == "Weather Distribution":
    fig_weather = px.histogram(data, x='weathersit', title='Weather Distribution')
    st.plotly_chart(fig_weather, use_container_width=True)

    st.subheader("Weather Categories Description")
    st.text("- 1: Clear, Few clouds, Partly cloudy, Partly cloudy")
    st.text("- 2: Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist")
    st.text("- 3: Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds")
    st.text("- 4: Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog")

    fig_cnt_vs_weather = px.scatter(data, x='weathersit', y='cnt', title='Count of Rental Bikes vs Weather')
    st.plotly_chart(fig_cnt_vs_weather, use_container_width=True)

elif visualization_option == "Humidity Distribution":
    fig_humidity = px.histogram(data, x='hum', title='Humidity Distribution')
    st.plotly_chart(fig_humidity, use_container_width=True)

elif visualization_option == "Rental Bikes by Month":
    avg_by_month = data.groupby('mnth')['cnt'].mean().reset_index()
    fig_avg_by_month = px.bar(avg_by_month, x='mnth', y='cnt', title='Average Rental Bikes by Month')
    st.plotly_chart(fig_avg_by_month, use_container_width=True)
