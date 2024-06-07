# SurfsUp Weather Analysis and API

## Overview

This project involves analyzing weather data using pandas and creating a Flask API to provide weather information. The primary goal is to provide insights about weather trends in Hawaii and offer an easy-to-use API for accessing this weather data.

### Part 1: Pandas Weather Analysis

Using pandas, we perform an extensive analysis of the weather data stored in a SQLite database. The main steps include:

1. **Data Extraction and Cleaning**:
    - Extract weather data from the SQLite database.
    - Clean the data to handle missing values and ensure consistency.

2. **Descriptive Statistics**:
    - Calculate summary statistics such as mean, median, and standard deviation for temperature and precipitation.
    - Visualize data distribution through histograms and box plots.

3. **Trend Analysis**:
    - Analyze temperature and precipitation trends over different time periods.
    - Identify seasonal patterns and yearly variations.

4. **Station Analysis**:
    - Analyze data from different weather stations to find the most active stations.
    - Compare weather trends between various stations.

### Part 2: Creating the Weather API

Using Flask and SQLAlchemy, we create an API to serve weather information. The API provides several endpoints to access different types of weather data:

1. **Setup**:
    - Configure the Flask application and set up SQLAlchemy to interact with the SQLite database.
    - Reflect the existing database schema using SQLAlchemy's automap feature.

2. **API Routes**:
    - **Home Route (`/`)**: Provides a simple welcome message.
    - **Temperature Observations (`/api/v1.0/tobs`)**: Returns the dates and temperature observations for the last year of data.
    - **Precipitation (`/api/v1.0/precipitation`)**: Returns a JSON list of precipitation data.
    - **Stations (`/api/v1.0/stations`)**: Returns a list of weather stations.
    - **Temperature for Date Range (`/api/v1.0/<start>` and `/api/v1.0/<start>/<end>`)**: Returns temperature statistics (min, max, avg) for a given start or start-end date range.

## File Structure

- **app.py**: Flask application that defines the API routes.
- **Resources**:
- **hawaii.sqlite**: SQLite database containing the weather data.
- **weather_analysis.ipynb**: Jupyter notebook for the pandas weather analysis.
- **README.md**: This file.

## Setup and Usage

1. **Clone the Repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Set Up the Environment**:
    - Ensure you have Python 3.x installed.
    - Install the necessary packages:
      ```bash
      pip install -r requirements.txt
      ```

3. **Run the Flask Application**:
    ```bash
    python app.py
    ```
    - The application will start running on `http://127.0.0.1:5000/`.

4. **Access the API**:
    - Open a web browser and navigate to the available endpoints:
      - Home: `http://127.0.0.1:5000/`
      - Temperature Observations: `http://127.0.0.1:5000/api/v1.0/tobs`
      - Precipitation: `http://127.0.0.1:5000/api/v1.0/precipitation`
      - Stations: `http://127.0.0.1:5000/api/v1.0/stations`
      - Temperature for Date Range: `http://127.0.0.1:5000/api/v1.0/<start>` or `http://127.0.0.1:5000/api/v1.0/<start>/<end>`

## Conclusion

This project combines data analysis with API development to provide valuable weather insights. The pandas analysis reveals trends and patterns in the data, while the Flask API makes it easy to access this information programmatically. This combination of technologies offers a comprehensive solution for weather data analysis and retrieval.
