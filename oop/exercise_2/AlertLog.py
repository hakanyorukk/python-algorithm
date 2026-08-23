#from Alert import Alert
from collections import defaultdict, Counter
from logging import critical

from oop.exercise_2.Alert import Alert


class AlertLog:

    def __init__(self):
        self.alerts = []

    def add(self, alert):
        if alert not in self.alerts:
            self.alerts.append(alert)

    def __len__(self):
        return len(self.alerts)

    def __contains__(self, alert):
        if alert in self.alerts:
            return True
        return False

    def critical_alerts(self):
        alert_list = []
        for alert in self.alerts:
            if alert.is_critical():
                alert_list.append(alert)

        return alert_list

    def by_server(self):
        alert_dict = defaultdict(list)
        for alert in self.alerts:
            alert_dict[alert.server].append(alert.metric_name())
        return {server: sorted(metric) for server,metric in alert_dict.items()}

    def sorted_by_severity(self):
         return sorted(self.alerts, key=lambda a:(-a.severity(), a.server))

    def worst_offender(self):
        return Counter(alert.server for alert in self.alerts)

    def summary(self):
        return {"total": self.__len__(), "critical":self.critical_alerts(), "servers": self.by_server()}



