# Import the dependencies.
from flask import Flask

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
# Declare a Base using `automap_base()`
Base = automap_base()
# Use the Base class to reflect the database tables
Base.prepare(autoload_with=engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station


#################################################
# Flask Setup
#################################################
# Initialise the Flask App
app = Flask(__name__)

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        F"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>",
        f"/api/v1.0/start<br/>",
        f"/api/v1.0/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
# Create a session
session = Session(engine)

# Query date and precipitation data
results = session.query(Measurement.date, Measurement.prcp).all()

session.close()

# Convery results to a list
dateprcp = list(np.ravel(results))

return jsonify(dateprcp)

@app.route("/api/v1.0/stations")
# Create a session
session = Session(engine)

# Query listof station data
sel = [Measurement.station,
      func.count(Measurement.station)]
results = session.query(*sel).\
    group_by(Measurement.station).\
    order_by(desc(func.count(Measurement.station))).all()

session.close()

# Convery results to a list
stations = list(np.ravel(results))

return jsonify(stations)

@app.route("/api/v1.0/tobs")
# Create a session
session = Session(engine)

# Query list of tempeerature data
sel = [Measurement.tobs]
temp_frequency = session.query(*sel).\
    filter(Measurement.station == 'USC00519281').\
    filter(Measurement.date >= query_date).all()

session.close()

# Convery results to a list
tobs = list(np.ravel(temp_frequency)

return jsonify(tobs)

@app.route("/api/v1.0/start")
# Create a session
session = Session(engine)

# Query list of specific temp data
sel = [func.min(Measurement.tobs),
    func.max(Measurement.tobs),
    func.avg(Measurement.tobs)]
summary_stats1 = session.query(*sel).\
    filter(Measurement.station == 'USC00519281').\
    order_by(Measurement.station).all()

session.close()

# Convery results to a list
specifictemp = list(np.ravel(summary_stats1)

return jsonify(specifictemp)

if --name-- == '--main--':
    app.run(debug=True)







