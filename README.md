# Car Value Predictor

This project is a machine learning application designed to predict the value of used cars based on various features such as brand, model, year, mileage, and more. The project involves data collection through web scraping, building an AI model, and deploying the model using Streamlit.

## Table of Contents

- [Overview](#overview)
- [Data Collection](#data-collection)
- [Model Building](#model-building)
- [Deployment](#deployment)

## Overview

The Car Value Predictor project aims to provide an accurate estimation of used car prices. By analyzing a wide range of features, the AI model predicts the market value of a car, helping users make informed buying or selling decisions.

## Data Collection

Data was collected by scraping the [Car and Bike](https://www.carandbike.com/) website using Python's `BeautifulSoup` and `requests` libraries. The dataset includes various attributes such as:

- Car make and model
- Year of manufacture
- Mileage
- Engine capacity
- Fuel type
- Transmission type
- Price

## Model Building

The AI model was built using the following steps:

1. **Data Preprocessing**: Cleaning the data and handling missing values.
2. **Feature Engineering**: Creating new features and transforming existing ones.
3. **Model Selection**: Experimenting with various regression models including Linear Regression, Decision Trees, and XGBoost.
4. **Hyperparameter Tuning**: Using Grid Search and Cross-Validation to optimize model performance.
5. **Evaluation**: Measuring the model's accuracy using metrics like Mean Absolute Error (MAE) and R-squared.

## Deployment

The final model was deployed using [Streamlit](https://streamlit.io/), enabling users to input car details and get an instant price prediction. The app is lightweight, easy to use, and accessible through a web browser.

## App Link
[Link](https://car-and-bike.onrender.com)

