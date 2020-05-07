# Importing Flask
from flask import Flask, jsonify
import csv

file_prc = "prcp.csv"

# Create an app
app = Flask(__name__)

# Define Route
@app.route('/')
def home():
    print("Welcome to Home page")
    return (
        f"Welcome to Home page!"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
        )

@app.route("/api/v1.0/precipitation")

if __name__ == "__main__":
    app.run(debug=True)









