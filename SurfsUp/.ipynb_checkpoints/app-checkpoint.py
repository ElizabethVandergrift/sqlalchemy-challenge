# Import the dependencies.
import os
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import func
from flask import Flask, jsonify
#################################################
# Database Setup
#################################################
#engine = create_engine("sqlite:///../Resources/hawaii.sqlite", echo=False)
db_path = os.path.join(os.path.dirname(__file__), '../Resources/hawaii.sqlite')
engine = create_engine(f"sqlite:///{db_path}", echo=False)

# reflect an existing database into a new model
Base = automap_base()
Base.prepare(autoload_with=engine)
print(Base.classes.keys())
# reflect the tables

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
