#importing necessary libraries
import functions as fn
import pandas as pd


#define necessary variables
cities=['patan','kathmandu','bhaktapur']
all_current_weather_df = pd.DataFrame()
all_forecast_df = pd.DataFrame()


for city in cities:
    current_df=fn.fetch_current_weather(city)
    forecast_df=fn.fetch_forecast_weather(city)

    all_current_weather_df=pd.concat([all_current_weather_df,current_df])
    all_forecast_df=pd.concat([all_forecast_df,forecast_df])








