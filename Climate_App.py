# Importing Flask
from flask import Flask

# Create an app
app = Flask(__name__)

# Define Route
@app.route('/')
def home():
    return (
        f"Welcome to Home page!"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
        )









