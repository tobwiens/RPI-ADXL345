import json


class AccelerometerMeasurementBurst(object):

    accelerometer_measurement_list = []
    time_of_last_measurement = ''
    measurement_hz = 0

    def __init__(self, time_of_last_measurement, measurement_hz):
        self.time_of_last_measurement = time_of_last_measurement
        self.measurement_hz = measurement_hz
        self.accelerometer_measurement_list = list()

    def add_measurement(self, measurement):
        self.accelerometer_measurement_list.append(measurement)

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda o: o.__dict__)
