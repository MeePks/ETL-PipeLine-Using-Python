#importing necessary libraries
import functions as fn
import sql 
import pandas as pd


#define necessary variables
cities=['patan','kathmandu','bhaktapur','Pokhara']
all_current_weather_df = pd.DataFrame()
all_forecast_df = pd.DataFrame()
server='DESKTOP-8VLOSDR'
database='WeatherETL'
base_table='Cities'
current_weather='CurrentWeather'
forecase_weather='ForecastWeather'




for city in cities:
    current_df=fn.fetch_current_weather(city)
    all_current_weather_df=pd.concat([all_current_weather_df,current_df])
    forecast_df=fn.fetch_forecast_weather(city)
    all_forecast_df=pd.concat([all_forecast_df,forecast_df])



cities_df=all_current_weather_df[['CityID', 'CityName', 'Latitude', 'Longitude']].drop_duplicates()
sql.insert_into_base_table(server,database,base_table,cities_df)
sql.insert_into_other_tables(server,database,current_weather,forecase_weather,all_current_weather_df,all_forecast_df)







