from collections import defaultdict, Counter

raw_readings = [
    "2026-08-15T10:00 sensor-A temperature 22.5 celsius",
    "2026-08-15T10:05 sensor-B humidity 45.0 percent",
    "2026-08-15T10:10 sensor-A temperature 23.1 celsius",
    "2026-08-15T10:15 sensor-C pressure 1013.2 hpa",
    "malformed line here",
    "2026-08-15T10:20 sensor-B humidity 150.0 percent",
    "2026-08-15T10:25 sensor-A temperature -300.0 celsius",
    "2026-08-15T10:30 sensor-C pressure abc hpa",
    "2026-08-15T10:35 sensor-B humidity 48.5 percent",
    "2026-08-15T10:40 sensor-A temperature 21.8 celsius",
    "2026-08-15T10:45 sensor-D temperature 19.0 kelvin",
]

class ReadingError(Exception): pass
class ParseError(ReadingError): pass
class InvalidRangeError(ReadingError): pass
class InvalidUnitError(ReadingError): pass


class Reading:

    def __init__(self, timestamp, sensor_id, metric, value, unit):
        self.timestamp = timestamp
        self.sensor_id = sensor_id
        self.metric = metric
        self.value = value
        self.unit = unit

    @classmethod
    def from_line(cls, line):
        try:
            timestamp, sensor_id, metric, value_str, unit = line.split(" ", maxsplit=4)
            value = float(value_str)
        except (AttributeError, ValueError):
            raise ParseError("Invalid parsing")

        if metric == "temperature":
            if not -100 <= value <= 100:
                raise InvalidRangeError(f"temperature {value} out of range")
            if unit != "celsius":
                raise InvalidUnitError(f"temperature must be in celsius not {unit}")

        elif metric == "humidity":
            if not 0 <= value <= 100:
                raise InvalidRangeError(f"humidity {value} out of range")
            if unit != "percent":
                raise InvalidUnitError(f"humidity must be in percent not {unit}")

        elif metric == "pressure":
            if not 800 <= value <= 1200:
                raise InvalidRangeError(f"pressure {value} ouf of range")
            if unit != "hpa":
                raise InvalidUnitError(f"pressure must be in hpa not {unit}")

        else:
            raise InvalidUnitError(f"Unrecognized unit {unit}")
        return cls(timestamp, sensor_id, metric, value, unit)

    def __str__(self):
        return (f"Timestamp: {self.timestamp}\n"
                f"Sensor id: {self.sensor_id}\n"
                f"Metric: {self.metric}\n"
                f"Value: {self.value}\n"
                f"Unit: {self.unit}")

    @property
    def date(self):
        date, time = self.timestamp.split("T")
        return date

class ReadingSet:

    def __init__(self):
        self.readings = []
        self.rejections = []

    def add(self, reading):
        self.readings.append(reading)

    def add_rejection(self, rejection):
        self.rejections.append(rejection)

    def average_by_metric(self):
        metric_dict = defaultdict(list)
        result = {}
        for reading in self.readings:
            metric_dict[reading.metric].append(reading.value)

        for metric, values in metric_dict.items():
            result[metric] = round(sum(values) / len(values), 1)
        return result

    def readings_in_range(self, metric, low, high):
        metric_list = [r for r in self.readings if r.metric == metric]
        return [r for r in metric_list if low < r.value < high]

    def sensor_metrics(self):
        sensor_dict = defaultdict(set)
        for reading in self.readings:
            sensor_dict[reading.sensor_id].add(reading.metric)
        return sensor_dict

    def most_active_sensor(self):
        return Counter(r.sensor_id for r in self.readings).most_common(1)

    def summary(self):
        return {"Total valid": {len(self.readings)}, "Total rejected": {len(self.rejections)},
                "Averages": self.average_by_metric()}

def main():
    reading_set = ReadingSet()
    for reading_line in raw_readings:
        try:
            valid_reading = Reading.from_line(reading_line)
            reading_set.add(valid_reading)
        except ReadingError as e:
            reading_set.add_rejection({"line": reading_line, "reason": str(e)})
    #print(f"{valid_count} valid readings, {len(rejected_readings)} rejected")
    print(reading_set.summary())

if __name__ == "__main__":
    main()