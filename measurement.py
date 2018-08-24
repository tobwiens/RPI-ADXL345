import json


class AccelerometerMeasurement(object):
    x_axis = 0
    y_axis = 0
    z_axis = 0
    time = ''  # ISO-8601

    def __init__(self, x_axis: int = 0, y_axis: int = 0, z_axis: int = 0, time: str = ''):
        self.x_axis = x_axis
        self.y_axis = y_axis
        self.z_axis = z_axis
        self.time = time

    def toJSON(self) -> str:
        return json.dumps(self, default=lambda x: x.__dict__)
