from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
import pandas as pd

def sqlalchemy_connnection(server,database):
    try:
        connection_string = f'mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'
        engine=create_engine(connection_string)
        return engine
    except:
        print(f'Error Connecting to the Server:{server} database : {database}')


def table_exists(engine,table_name):
    try:
        result=pd.read_sql_query(f"select top 1 '1' from {table_name}",engine)
        return True
    except SQLAlchemyError:
        return False


def insert_into_base_table(server,database,base_table,cities_df):
    baseTblConn=sqlalchemy_connnection(server,database)
    if table_exists(baseTblConn,base_table):
        existing_cities=pd.read_sql_table(base_table,baseTblConn)
        new_cities= cities_df[~cities_df['CityID'].isin(existing_cities['CityID'])]
        if not new_cities.empty:
            new_cities.to_sql(base_table,baseTblConn,if_exists='append',index=False)
    else:
        cities_df.to_sql(base_table,baseTblConn,if_exists='append',index=False)

def insert_into_other_tables(server,database,current_weather,forecase_weather,all_current_weather_df,all_forecast_df):
    engine=sqlalchemy_connnection(server,database)
    all_current_weather_df.to_sql(current_weather, engine, if_exists='append', index=False)
    all_forecast_df.to_sql(forecase_weather, engine, if_exists='append', index=False)




