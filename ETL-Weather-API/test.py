
#importing necessary libraries
import functions as fn
import sql 
import pandas as pd
import configparser as cfp
from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

#parsing config files
config=cfp.ConfigParser()
config.read('ETL-Weather-API\config.ini')


#define necessary variables
all_current_weather_df = pd.DataFrame()
all_forecast_df = pd.DataFrame()

#reding data from config file
server=config['Sql Information']['server']
database=config['Sql Information']['database']
base_table=config['Sql Information']['base_table']
current_weather=config['Sql Information']['current_weather']
forecase_weather=config['Sql Information']['forecase_weather']
cities = config['main']['cities'].split(',')

def sqlalchemy_connnection(server,database):
    try:
        connection_string = f'mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server&Trusted_Connection=yes'
        engine=create_engine(connection_string)
        print('Connected')
        return engine
    except:
        print(f'Error Connecting to the Server:{server} database : {database}')


baseTblConn=sqlalchemy_connnection(server,database)
try:
    # Use engine.connect() to get a connection object
    conn = baseTblConn.connect()
    
    # Use the connection to execute the SQL query
    result = pd.read_sql_query(f"select 1", conn)
    print(result)
    
except Exception as e:
    print(f'Error executing query: {e}')
finally:
    conn.close()  # Close the connection after using it



