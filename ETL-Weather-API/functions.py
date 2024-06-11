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
        'city_id':[data['id']],
        'city' :[data['name']],
        'latitude': [data['coord']['lat']],
        'longitud':[data['coord']['lon']],
        'weather': [data['weather'][0]['description']],
        'temperature_celsius': [data['main']['temp'] - 273.15],  # Convert from Kelvin to Celsius
        'humidity': [data['main']['humidity']],
        'pressure': [data['main']['pressure']],
        'datetime': [pd.to_datetime(data['dt'], unit='s')],
        'visibility':[data['visibility']],
        'sunrise':[pd.to_datetime(data['sys']['sunrise'], unit='s')],
        'sunset':[pd.to_datetime(data['sys']['sunset'], unit='s')]
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
            'city_id': data['city']['id'],
            'datetime': pd.to_datetime(entry['dt'], unit='s'),
            'weather': entry['weather'][0]['description'],
            'temperature_celsius': entry['main']['temp'] - 273.15,  # Convert from Kelvin to Celsius
            'humidity': entry['main']['humidity'],
            'pressure': entry['main']['pressure']

        })
    forecast_df = pd.DataFrame(forecast_data)
    return forecast_df



    