from collections import defaultdict, Counter

class AlertLog:

    def __init__(self):
        self.alerts = []

    def add(self, alert):
        if alert not in self.alerts:
            self.alerts.append(alert)

    def __len__(self):
        return len(self.alerts)

    def __contains__(self, alert):
        return alert in self.alerts

    def __iter__(self):
        return iter(self.alerts)
        # self.index = 0
        # return self

    # def __next__(self):
    #
    #     if self.index>=len(self.alerts):
    #         raise StopIteration
    #     alert = self.alerts[self.index]
    #     self.index+=1
    #     return alert

    def critical_alerts(self):
        alert_list = []
        for alert in self.alerts:
            if alert.is_critical():
                alert_list.append(alert)

        return alert_list

    def by_server(self):
        alert_dict = defaultdict(set)
        for alert in self.alerts:
            alert_dict[alert.server].add(alert.metric_name())
        return {server: sorted(metric) for server,metric in alert_dict.items()}

    def sorted_by_severity(self):
         return sorted(self.alerts, key=lambda a:(-a.severity(), a.server))

    def worst_offender(self):
        return Counter(alert.server for alert in self.alerts).most_common(1)[0]

    def summary(self):
        return {"total": self.__len__(), "critical":len(self.critical_alerts()), "servers": len({a.server for a in self.alerts})}



