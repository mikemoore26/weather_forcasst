import streamlit as st
import plotly.express as px
import backend

# make the location, days, option widgets
location = st.text_input(placeholder="Enter Location", value="East New York",
                         key="location", label="Enter a Location")

days = st.slider(min_value=1, max_value=5, key="days", label="Enter the amount of days")


option  = st.selectbox(label="Select type of data", options=("Temperature", "Sky"))

st.subheader(f"{option} for the next {days} in {location}")

# create plots and images
if location:
    try:
        filtered_data = backend.get_data(location=location,days=days, option=option)

        if option == "Temperature" and filtered_data != None:
            data_temp = [data['main']['temp']  for data in filtered_data]
            data_temp = [data / 10 * (9/5) + 32 for data in data_temp]

            data_date = [data['dt_txt'] for data in filtered_data]

            figure = px.line(x=data_date, y=data_temp, labels={'x': "Date", 'y' : "Temperature"})
            st.plotly_chart(figure)

        if option == "Sky":

            images = {"Rain": "images/rain.png",
                      "Clouds": "images/cloud.png",
                      "Clear": "images/clear.png",
                      "Snow": "images/snow.png"}

            data_sky = [data['weather'][0]['main'] for data in filtered_data]
            sky_condition = [images[condition] for condition in data_sky]
            st.image(sky_condition, width=126)
    except KeyError:
        st.error("Please enter a valid key")