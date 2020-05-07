# Importing Flask
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import datetime

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
    return (
        f"Welcome to Home page!<br/>"
        f"Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")
def prcp():
    session = Session(engine)

    # query the database 
    results = session.query(Measurement.date,Measurement.prcp).\
              filter(Measurement.date > datetime.date(2016, 8, 23)).\
              order_by(Measurement.date.desc()).all()

    session.close()

    # create a dictionary of the result 
    prcp_values = []
    for date,prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = date
        prcp_dict["prcp"] = prcp
        prcp_values.append(prcp_dict)
    return jsonify(prcp_values)


if __name__ == "__main__":
    app.run(debug=True)









