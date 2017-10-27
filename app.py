
# coding: utf-8

# In[36]:

from flask import Flask, jsonify
import pandas as pd
from sqlalchemy import *
from sqlalchemy.ext.automap import automap_base
from datetime import date
from sqlalchemy.orm import Session


#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#################################################
# Database Setup
#################################################

# Create route /api/v1.0/precipitation
@app.route("/")
def welcome():
	return (
        f"Available Routes:<br/>"

        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/temp<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/stations"
    )

@app.route('/api/v1.0/precipitation')
def prcp():
	# Create an engine to connecting to hawaii_hw.sqlite
	engine = create_engine("sqlite:///hawaii_hw.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	measurement = Base.classes.hawaii_measurement

	session = Session(engine)

	prcp_data = session.query(measurement.date, measurement.rainfall).filter(measurement.date > '2016-08-18').all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in prcp_data]
	prcp = [x[1] for x in prcp_data]

	prcp_date = pd.DataFrame({'date': Date, 'prcp': prcp})

	prcp_date_dict = prcp_date.to_dict(orient='record')

	return jsonify(prcp_date_dict)


# In[37]:

@app.route('/api/v1.0/stations')
def station():
	# Create an engine to connecting to hawaii_hw.sqlite
	engine = create_engine("sqlite:///hawaii_hw.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Station = Base.classes.hawaii_station

	# Create a session for the engine
	session = Session(engine)

	station_info = session.query(Station.station, Station.name, Station.latitude, Station.longitude, Station.elevation).all()

	station = [x[0] for x in station_info]
	name = [x[1] for x in station_info]
	lat = [x[2] for x in station_info]
	longitude = [x[3] for x in station_info]
	elevation = [x[4] for x in station_info]

	station_df = pd.DataFrame({'station': station, 'name': name, 'latitude': lat, 'longitude': longitude, 'elevation': elevation})

	station_dict = station_df.to_dict(orient='record')

	return jsonify(station_dict)


# In[38]:

@app.route('/api/v1.0/temp')
def temp():
	# Create an engine to connecting to hawaii_hw.sqlite
	engine = create_engine("sqlite:///hawaii_hw.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	temp_data = session.query(Measurement.date, Measurement.temp).filter(Measurement.date > '2016-08-18').all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in temp_data]
	temp = [x[1] for x in temp_data]

	temp_date = pd.DataFrame({'date': Date, 'temp': temp})

	temp_date_dict = temp_date.to_dict(orient='record')

	return jsonify(temp_date_dict)


# In[39]:

@app.route('/api/v1.0/start')
def start(start):
	# Create an engine to connecting to hawaii_hw.sqlite
	engine = create_engine("sqlite:///hawaii_hw.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	start_info = session.query(measurement.date, measurement.temp).filter(measurement.date >= start).all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in start_info]
	temp = [x[1] for x in start_info]

	start_data = pd.DataFrame({'temp': temp})

	temp_max = start_data.max()
	temp_min = start_data.min()
	temp_avg = start_data.mean()

	summary_df = pd.DataFrame({'Max. Temperature': temp_max, 'Min. Temperature': temp_min, 'Average Temperature': temp_avg})

	summary_dict = summary_df.to_dict(orient='record')

	return jsonify(summary_dict)



# In[43]:

if __name__ == "__main__":
    app.run(debug=True,port = 8002)


# In[ ]:




# In[ ]:



