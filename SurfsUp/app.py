# Import the dependencies.
import os
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify
from datetime import datetime
#################################################
# Database Setup
#################################################
database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Resources', 'hawaii.sqlite')
engine = create_engine(f"sqlite:///{database_path}", echo=False)

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(engine, reflect=True)

# reflect the tables
print(Base.classes.keys())
# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(bind=engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    """List all available API routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/temp/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    """Return a list of precipitation data."""
    # Query all precipitation data
    results = session.query(Measurement.date, Measurement.prcp).all()
    # Convert list of tuples into dictionary
    precipitation_data = {date: prcp for date, prcp in results}
    return jsonify(precipitation_data)

@app.route("/api/v1.0/stations")
def stations():
    """Return a list of stations."""
    # Query all stations
    results = session.query(Station.station).all()
    # Convert list of tuples into normal list
    stations_list = [station for station, in results]
    return jsonify(stations_list)

@app.route("/api/v1.0/tobs")
def tobs():
    # Example start date
    start_date = datetime(2016, 8, 23)
    start_date_str = start_date.strftime('%Y-%m-%d')
    
    # Query the database
    results = session.query(Measurement.date, Measurement.tobs).filter(Measurement.date >= start_date_str).all()
    
    # Convert results to a dictionary
    tobs_list = []
    for date, tobs in results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        tobs_list.append(tobs_dict)
    
    return jsonify(tobs_list)

@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")
def temp(start=None, end=None):
    """Return TMIN, TAVG, TMAX for a given start or start-end range."""
    # Select statement
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    if not end:
        # Calculate TMIN, TAVG, TMAX for dates greater than start
        results = session.query(*sel).filter(Measurement.date >= start).all()
    else:
        # Calculate TMIN, TAVG, TMAX for dates between start and end
        results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    # Convert list of tuples into dictionary
    temperature_data = {
        "TMIN": results[0][0],
        "TAVG": results[0][1],
        "TMAX": results[0][2]
    }
    return jsonify(temperature_data)

if __name__ == "__main__":
    app.run(debug=True)