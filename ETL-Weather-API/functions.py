#importing necessary Libraies
import requests
import pandas as pd

#Necessary Variables
base_url='http://api.openweathermap.org/data/2.5/'
api_key='a8b63f4b297154f9f4b13387cacfdb4b'


#function to fetch current Weather Data
def fetch_current_weather(city):
    url=base_url+f'weather?q={city}&appid={api_key}'
    response=requests.get(url)
    data=response.json()

    current_weather={
        'CityID':[data['id']],
        'CityName' :[data['name']],
        'Latitude': [data['coord']['lat']],
        'Longitude':[data['coord']['lon']],
        'Weather': [data['weather'][0]['description']],
        'Temperature': [data['main']['temp'] - 273.15],  # Convert from Kelvin to Celsius
        'Humidity': [data['main']['humidity']],
        'Pressure': [data['main']['pressure']],
        'DateTime': [pd.to_datetime(data['dt'], unit='s')],
        'Visibility':[data['visibility']],
        'Sunrise':[pd.to_datetime(data['sys']['sunrise'], unit='s')],
        'Sunset':[pd.to_datetime(data['sys']['sunset'], unit='s')]
    }

    current_df= pd.DataFrame(current_weather)

    return current_df
    
#function to fetch 5-days forecase data
def fetch_forecast_weather(city):
    url=base_url+f'forecast?q={city}&appid={api_key}'
    response=requests.get(url)
    data=response.json()

    forecast_data=[]
    for entry in data['list']:
        forecast_data.append({
            'CityID': data['city']['id'],
            'DateTime': pd.to_datetime(entry['dt'], unit='s'),
            'Weather': entry['weather'][0]['description'],
            'Temperature': entry['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
            'Humidity': entry['main']['humidity'],
            'Pressure': entry['main']['pressure']

        })
    forecast_df = pd.DataFrame(forecast_data)
    return forecast_df



    