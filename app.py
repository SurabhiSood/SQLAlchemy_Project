# Importing Flask
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime
import html

date_yr = datetime.date(2016, 8, 23)

# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing Database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect = True)

# Save the reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create an app
app = Flask(__name__)

# Define Route
@app.route('/')
def home():
    print("Welcome to Home page")
#    <img src="Images/surfs-up.png">
    return (
        f"Welcome to Home page!<br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date/<start_date><br/>"
        f"/api/v1.0/start_date<start_date>/end_date<end_date>"
        )

# Defining Routes

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)

    # query the database 
    results = session.query(Measurement.date,Measurement.prcp).\
              filter(Measurement.date > date_yr).\
              order_by(Measurement.date.desc()).all()

    session.close()

    # create a dictionary of the result 
    prcp_values = []
    for date,prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict['prcp'] = prcp
        prcp_values.append(prcp_dict)
    return jsonify(prcp_values)


@app.route("/api/v1.0/stations")
def stat():
    session = Session(engine)

    # query the database
    results_station = session.query(Station.name)

    session.close()
    
    # create a list for list of stations
    station_list=[]
    for st in results_station:
        station_list.append(st)
    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tob():
    session = Session(engine)

    # query the database
    results_tobs = session.query(Measurement.date,Measurement.tobs).\
                   filter(Measurement.station=='USC00519281').\
                   filter(Measurement.date > date_yr).all()
    session.close()

    # create a list of temp observations for the previous year
    tobs_list=[]
    for temp in results_tobs:
        tobs_list.append(temp)
    return jsonify(tobs_list)


'''When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date.'''    

@app.route("/api/v1.0/start_date/<start_date>")
def calc_temps(start_date):
    session =  Session(engine)

    result_sd = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).all()
    
    session.close()

    return jsonify(result_sd)

'''When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive.'''    

@app.route("/api/v1.0/start_date<start_date>/end_date<end_date>")
def calc_temp(start_date,end_date):
    session = Session(engine)

    result_ob = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
                filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

    session.close()

    return jsonify(result_ob)
    

if __name__ == "__main__":
    app.run(debug=True)





