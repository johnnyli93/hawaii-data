# Create route /api/v1.0/<start>/<end>
@app.route('/api/v1.0/start/end')
def start(start, end):
	# Create an engine to connecting to hawaii.sqlite
	engine = create_engine("sqlite:///hawaii_hw.sqlite")

	# Reflect Database into ORM classes
	Base = automap_base()
	Base.prepare(engine, reflect=True)
	Base.classes.keys()

	Measurement = Base.classes.hawaii_measurement

	# Create a session for the engine
	session = Session(engine)

	start_end_info = session.query(measurement.date, measurement.temp).filter(measurement.date >= start).filter(measurement.date <= end).all()

	# Save the data into lists
	Date = [pd.to_datetime(x[0]) for x in start_end_info]
	temp = [x[1] for x in start_end_info]

	start_end = pd.DataFrame({'tobs': tobs})

	temp_max = start_end.max()
	temp_min = start_end.min()
	temp_avg = start_end.mean()

	summary_df = pd.DataFrame({'Max. Temperature': temp_max, 'Min. Temperature': temp_min, 'Average Temperature': temp_avg})

	summary_dict = summary_df.to_dict(orient='record')

	return jsonify(summary_dict)

if __name__ == "__main__":
    app.run(debug=True,port = 8002)
