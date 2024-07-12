import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

# Sample data: Load your weather data here
data_url = 'https://raw.githubusercontent.com/jbrownlee/Datasets/master/daily-min-temperatures.csv'
weather_data = pd.read_csv(data_url, parse_dates=['Date'])

# Preprocessing: Add a 'Heatwave' column based on a temperature threshold
weather_data['Year'] = weather_data['Date'].dt.year
weather_data['Month'] = weather_data['Date'].dt.month
weather_data['Day'] = weather_data['Date'].dt.day

# Define a heatwave as a day with a temperature above 30 degrees Celsius (example threshold)
weather_data['Heatwave'] = weather_data['Temp'] > 30
# Display the first few rows of the dataframe
weather_data.head()
