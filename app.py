#import dependecies
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, and_
import datetime as dt
from pandas.tseries.offsets import DateOffset
from flask import Flask, jsonify

####################################
# Database setup
####################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#reflect the existing database into the model
Base = automap_base()
#reflect the tables
Base.prepare(engine,reflect=True)

#save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#open the session
session = Session(engine)

####################################
# Create the flask routes
####################################
#create and setup flask
app = Flask(__name__)

#define dates in last year
endDate = session.query(Measurement.date).order_by(Measurement.date.desc()).first()
endDate = list(np.ravel(endDate))[0]
startDate = dt.date.fromisoformat(endDate)-pd.DateOffset(years=1)
startDate = startDate.strftime('%Y-%m-%d')
# #close the session
# session.close()

#define what to do when a use hits the index route
@app.route("/")
def home():
    #return all the routes that are available
    return (
        f"<strong>Available Routes:</strong><br/><br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/insert_start_date<br/>"
        f"/api/v1.0/insert_start_date/insert_end_date"
    )

#define what to do when a user hits a different [insert route] route
@app.route("/api/v1.0/precipitation")
def precipitaion():
    #open the session
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.prcp, Measurement.station).all()
    
    session.close()
    
    all_precipitation = []
    for date, prcp, station in results:
        precipitation_dict = {}
        precipitation_dict['date'] = date
        precipitation_dict['prcp'] = prcp
        precipitation_dict['station'] = station
        all_precipitation.append(precipitation_dict)
        
    return jsonify(all_precipitation)

@app.route("/api/v1.0/stations")
def stations():
    #open the session
    session = Session(engine)
    
    results = session.query(Station.station).all()
    
    session.close()
    
    all_station = list(np.ravel(results))
    
    return jsonify(all_station)

@app.route("/api/v1.0/tobs")
def tobs():
    #open the session
    session = Session(engine)
    
    results = session.query(Measurement.date, Measurement.tobs, Measurement.station)\
                        .filter(and_(Measurement.date>=startDate, Measurement.date<=endDate))\
                        .all()
    
    session.close()
    
    all_temps = []
    for date, tobs, station in results:
        temp_dict = {}
        temp_dict['date'] = date
        temp_dict['tobs'] = tobs
        temp_dict['station'] = station
        all_temps.append(temp_dict)
    
    return jsonify(all_temps)

@app.route("/api/v1.0/<start_date>")
def start(start_date):
    #open the session
    session = Session(engine)
    
    results = session.query(Measurement.date, \
                         func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs))\
                        .filter(Measurement.date>=start_date)\
                        .group_by(Measurement.date)\
                        .all()
    
    session.close()
    
    dates = []
    for result in results:
        date_dict = {}
        date_dict['date'] = result[0]
        date_dict['avg temp'] = result[1]
        date_dict['min temp'] = result[2]
        date_dict['max temp'] = result[3]
        dates.append(date_dict)
    
    return jsonify(dates)

@app.route("/api/v1.0/<start_date>/<end_date>")
def start_end(start_date,end_date):
    #open the session
    session = Session(engine)
    
    results = session.query(Measurement.date, \
                         func.avg(Measurement.tobs), func.min(Measurement.tobs), func.max(Measurement.tobs))\
                        .filter(and_(Measurement.date>=start_date,Measurement.date<=end_date))\
                        .group_by(Measurement.date)\
                        .all()
    
    session.close()
    
    dates = []
    for result in results:
        date_dict = {}
        date_dict['date'] = result[0]
        date_dict['avg temp'] = result[1]
        date_dict['min temp'] = result[2]
        date_dict['max temp'] = result[3]
        dates.append(date_dict)
    
    return jsonify(dates)

#define the main behavior
if __name__ == "__main__":
    app.run(debug=True)