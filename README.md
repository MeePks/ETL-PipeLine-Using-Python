This project implements an ETL (Extract, Transform, Load) pipeline that retrieves weather data from the OpenWeatherMap API, processes it, and stores it in a SQL Server database. The stored data is then used for visualization in Tableau.

Features

Data Extraction: Fetches current weather and 5-day/3-hour forecast data for multiple cities from the OpenWeatherMap API.

Data Transformation: Converts temperature from Kelvin to Celsius and adjusts datetime from UTC to Nepal Time (NPT).

Data Loading: Inserts the transformed data into SQL Server tables using SQLAlchemy.

Environment Variables: Securely manages API keys using environment variables to avoid exposure in the repository.

Visualization: Prepares data for visualization in Tableau for comprehensive weather analysis.




Technologies Used

Python: For scripting and data processing.

SQLAlchemy: For database interactions.

Pandas: For data manipulation and transformation.

OpenWeatherMap API: For fetching weather data.

SQL Server: For data storage.

Tableau: For data visualization.




Getting Started

Set up Config File to store your API key. To create API key you can visit 'https://home.openweathermap.org/users/sign_up' and signup to generate your API key.

Configure the SQL Server connection in the Config file.

Run the Python script to fetch, transform, and load data into the SQL Server database.

Connect Tableau to the SQL Server database to visualize the data.



Prerequisites

Python 3.x

SQL Server

Tableau



Usage

Clone the repository.

Set your OpenWeatherMap API keyinto the config file. I have setup config_sample.ini which you need to rename into config.ini file and seup necessary variable.

Configure your SQL Server connection string.

Run the ETL script.
