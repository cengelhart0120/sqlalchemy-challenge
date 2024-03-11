# Importing dependencies
import numpy as np
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflecting an existing database into a new model
Base = automap_base()

# Reflecting the tables
Base.prepare(autoload_with=engine)

# Saving references to each table
measurement_ref = Base.classes.measurement
station_ref = Base.classes.station

#################################################
# Flask Setup
#################################################

app = Flask(__name__)

#################################################
# Flask Routes
#################################################

# 1. "/"
   
@app.route("/")
def welcome():
    
    # Starting at the homepage and listing all available routes
    return (
        f"Welcome to my Climate API!<br/>"
        f"Available Routes:<br/>"
        f"/<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/2016-08-23<br/>"
        f"/api/v1.0/2016-08-23/2017-08-23"
    )

# 2. "/api/v1.0/precipitation"
 
@app.route("/api/v1.0/precipitation")
def precipitation():
    
    # Creating the session (link) from Python to the database
    session = Session(engine)
    
    # Querying for the last 12 months of precipitation data
    date_and_prcp = session.query(measurement_ref.date, measurement_ref.prcp).\
        filter(measurement_ref.date <= dt.date(2017, 8, 23)).\
        filter(measurement_ref.date >= dt.date(2016, 8, 23)).\
        all()
    
    # Closing the session
    session.close()
    
    # Creating a dictionary from the row data and appending to a list of all_prcp
    all_prcp = []
    for date, prcp in date_and_prcp:
        prcp_dict = {}
        prcp_dict[date] = prcp
        all_prcp.append(prcp_dict)
        
    # Returning the JSON representation of the dictionary
    return jsonify(all_prcp)

# 3. "/api/v1.0/stations"

@app.route("/api/v1.0/stations")
def stations():
    
    # Creating the session (link) from Python to the database
    session = Session(engine)
    
    # Querying for all stations
    stations = session.query(station_ref.station).all()
    
    # Closing the session
    session.close()
    
    # Converting list of tuples into normal list
    all_stations = list(np.ravel(stations))
    
    # Returning a JSON list of all_stations
    return jsonify(all_stations)
    
# 4. "/api/v1.0/tobs"

@app.route("/api/v1.0/tobs")
def tobs():
    
    # Creating the session (link) from Python to the database
    session = Session(engine)
    
    # Querying for the last 12 months of temperature data from the most-active station, USC00519281
    temps = session.query(measurement_ref.tobs).\
        filter(measurement_ref.date <= dt.date(2017, 8, 23)).\
        filter(measurement_ref.date >= dt.date(2016, 8, 23)).\
        filter(measurement_ref.station=='USC00519281').\
        all()
    
    # Closing the session
    session.close()
    
    # Converting list of tuples into normal list
    all_temps = list(np.ravel(temps))
    
    # Returning a JSON list of all_temps
    return jsonify(all_temps)
    
# 5. "/api/v1.0/<start>"

@app.route("/api/v1.0/<start>")
def temp_calcs_from_start(start):
    
    # Creating the session (link) from Python to the database
    session = Session(engine)
    
    # Querying for all the temperature data and saving it to a variable
    all_temps_query = session.query(measurement_ref.date, measurement_ref.tobs).all()
    
    # Creating a dictionary from the row data and appending to a list of all_temps_list
    all_temps_list = []
    for date, tobs in all_temps_query:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["tobs"] = tobs
        all_temps_list.append(tobs_dict)
    
    # Searching the dictionary for the input start date
    for row in all_temps_list:
        search_date = row['date']
        
        # If the start date is found, querying as appropriate to return tobs_min, tobs_max, tobs_avg for all the dates greater than or equal to the start date
        if search_date == start:
            start_query = session.\
                query(func.min(measurement_ref.tobs), func.max(measurement_ref.tobs), func.avg(measurement_ref.tobs)).\
                filter(measurement_ref.date >= start).\
                all()
            
            start_query_data = list(np.ravel(start_query))
            
            return jsonify(start_query_data)
        
    # If the start date is not found, returning an error message
    return jsonify({"error": "Start date not found. Acceptable start dates range from 2010-01-01 to 2017-08-23 (inclusive)."}), 404
            
    # Closing the session
    session.close()        
    
# 6. "/api/v1.0/<start>/<end>"

@app.route("/api/v1.0/<start>/<end>")
def temp_calcs_from_start_to_end(start, end):
    
    # Ensuring that the input start date is before, or the same as, the input end date
    if start <= end:
        
        # Creating the session (link) from Python to the database
        session = Session(engine)
        
        # Querying for all the temperature data and saving it to a variable
        all_temps_query = session.query(measurement_ref.date, measurement_ref.tobs).all()
        
        # Creating a dictionary from the row data and appending to a list of all_temps_list
        all_temps_list = []
        for date, tobs in all_temps_query:
            tobs_dict = {}
            tobs_dict["date"] = date
            tobs_dict["tobs"] = tobs
            all_temps_list.append(tobs_dict)
            
        # Searching the dictionary for the start date
        for row in all_temps_list:
            search_start_date = row['date']
            
            # If the start date is found, initiating search for the end date
            if search_start_date == start:
                for row in all_temps_list:
                    search_end_date = row['date']
                    
                    # If the end date is found, querying as appropriate to return tobs_min, tobs_max, tobs_avg for all the dates inclusive of the start and end dates
                    if search_end_date == end:
                        start_to_end_query = session.\
                            query(func.min(measurement_ref.tobs), func.max(measurement_ref.tobs), func.avg(measurement_ref.tobs)).\
                            filter(measurement_ref.date >= start).\
                            filter(measurement_ref.date <= end).\
                            all()
                        
                        start_to_end_query_data = list(np.ravel(start_to_end_query))
                        
                        return jsonify(start_to_end_query_data)
                    
                # If the end date is not found, returning an error message
                return jsonify({"error": "End date not found. Acceptable end dates range from 2010-01-01 to 2017-08-23 (inclusive)."}), 404
                
        # If the start date is not found, returning an error message
        return jsonify({"error": "Start date not found. Acceptable start dates range from 2010-01-01 to 2017-08-23 (inclusive)."}), 404
                        
    # If the start date is not before, or the same as, the end date, returning an error message
    return jsonify({"error": "Your start date cannot be after your end date."}), 404
    
    # Closing the session
    session.close()

if __name__ == "__main__":
    app.run(debug=True)