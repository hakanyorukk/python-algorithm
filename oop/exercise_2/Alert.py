from abc import ABC, abstractmethod


class Alert(ABC):
    def __init__(self, timestamp, server, value):
        self.timestamp = timestamp
        self.server = server
        self.value = value

    @abstractmethod
    def threshold(self):
        pass

    @abstractmethod
    def metric_name(self):
        pass

    def severity(self):
        return self.value - self.threshold()

    def is_critical(self):
        return self.severity() > 0

    def __str__(self):
        return f"{self.server} {self.metric_name()} {self.value} {"(CRITICAL)" if self.is_critical() else "(ok)"}"

    def __repr__(self):
        return f"{type(self).__name__}('{self.timestamp}', '{self.server}', {self.value})"

    def __eq__(self, other):
        if isinstance(other, Alert):
            if self.metric_name() == other.metric_name() and self.server == other.server and self.timestamp == other.timestamp:
                return True
        return False

    def __hash__(self):
        return hash((self.metric_name(), self.server, self.timestamp))

    @classmethod
    def from_line(cls, line):
        alert_types = {"cpu": CpuAlert, "memory": MemoryAlert, "disk": DiskAlert}
        try:
            timestamp, server, metric, value_str = line.split(" ")
            value = float(value_str)
        except ValueError:
            raise ValueError("Invalid value")
        if metric not in alert_types:
            raise ValueError(f"Unknown metric: {metric}")
        return alert_types[metric](timestamp, server, value)


class CpuAlert(Alert):

    def threshold(self):
        return 90

    def metric_name(self):
        return "cpu"

class MemoryAlert(Alert):
    def threshold(self):
        return 85

    def metric_name(self):
        return "memory"

class DiskAlert(Alert):
    def threshold(self):
        return 95

    def metric_name(self):
        return "disk"
