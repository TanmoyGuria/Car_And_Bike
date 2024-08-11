import pickle
import streamlit as st
import pandas as pd
import numpy as np
import requests
from streamlit_lottie import st_lottie
import json

model=pickle.load(open('car_price_model.pkl','rb'))
car=pd.read_csv("Car_and_bike_final.csv")
images=pd.read_csv("Car_image.csv")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Lottie animation
lottie_hello = load_lottieurl("https://lottie.host/df4867b4-55cd-4941-a269-3b30e645d0d0/kKKnpm2EJb.json")

col3, col4 = st.columns([3, 7])  # Adjust the ratio to fit your layout needs

with col4:
    st.title('Car Valuation')

with col3:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="low",  # Options: low, medium, high, canvas
        height=100,
        width=300,
        key=None,
    )

col1, col2 = st.columns([3, 7])

with col2:
    companies= sorted(car['Brand'].unique())
    option1 = st.selectbox('MAKER',companies,index=None,
        placeholder="Select the Manufacturer")

    name = car['Car Name'].loc[car['Brand'] == option1].unique()
    option2 = st.selectbox( 'MODEL', name,index=None,
        placeholder="Select the Model")

    # Get the image URL for the selected car name

    default_image_url = 'https://png.pngtree.com/png-vector/20190820/ourmid/pngtree-no-image-vector-illustration-isolated-png-image_1694547.jpg'
    image_url = images.loc[images['Title'] == option2, 'Image URL']

    if not image_url.empty:
        image_url = image_url.values[0]
    else:
        # Use a default image URL if the specific car image is not available
        image_url = default_image_url
    if option2:
        # Use custom CSS to set the image size
        st.markdown(
            f"""
        <style>
        .car-image-container {{
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 20px;
        }}
        .car-image {{
            width: 400px;
            height: 260px;
            object-fit: cover;
        }}
        </style>
        <div class="car-image-container">
            <img src="{image_url}" alt="{option2}" class="car-image">
        </div>
        """,
            unsafe_allow_html=True
        )


with col1:
    Location= sorted(car['City'].unique())
    Place = st.selectbox( 'City', Location,index=None,
        placeholder="Popular Cities")

    Transmission= sorted(car['Transmission Type'].unique())
    transmission_type = st.radio(
        "TRANSMISSION",Transmission,horizontal=True,index=None)

    Fuel= sorted(car['Fuel Type'].unique())
    fuel_type=st.selectbox( 'FUEL', Fuel,index=None,
        placeholder="Fuel type")

    import datetime
    current_year = datetime.datetime.now().year
    years_list = list(range(current_year, 2004, -1))
    Year = st.selectbox( 'SELECT MANUFACTURING YEAR', years_list,index=None,
        placeholder="Select the Year")

    Km_driven= st.number_input(
        "KILOMETERS", min_value=0,max_value=125000 , placeholder="Enter Kilometer Driven")



if st.button('CHECK VALUE', type='primary'):
    if option2 and Km_driven and fuel_type and transmission_type and Place and Year:

        prediction = model.predict(pd.DataFrame([[option2, Km_driven, fuel_type, transmission_type, Place, Year]],
                                                columns=['Car Name', 'Kilometers Driven (in Km)', 'Fuel Type',
                                                         'Transmission Type', 'City', 'Year']))

        predict = str(np.round(prediction[0], 2))


        st.markdown(
             f"""
            <div style="font-size:28px; text-align:center;">
                Rs. <span style="font-size:48px; font-weight:bold; color:#FF6347;">{predict}</span> Lakh
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.warning("Please select all the options before checking the value.")
