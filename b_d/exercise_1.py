import json
from collections import defaultdict, Counter

incidents_file = [
    {"id": "INC-001", "service": "payments", "severity": "critical", "duration_min": 45, "resolved": True},
    {"id": "INC-002", "service": "auth", "severity": "high", "duration_min": 20, "resolved": True},
    {"id": "INC-003", "service": "payments", "severity": "medium", "duration_min": 10, "resolved": False},
    {"id": "INC-004", "service": "search", "severity": "low", "duration_min": 5, "resolved": True},
    {"id": "INC-005", "service": "auth", "severity": "critical", "duration_min": 90, "resolved": False},
    {"id": "INC-006", "service": "payments", "severity": "high", "duration_min": 30, "resolved": True},
    {"id": "INC-007", "service": "search", "severity": "medium", "duration_min": 15, "resolved": True},
    {"id": "INC-008", "service": "auth", "severity": "critical", "duration_min": 60, "resolved": True},
]
#python object -> File
with open("incidents.json", "w") as f:
    json.dump(incidents_file, f, indent=2)

def load_incidents(filename):
    # file -> list
    incidents_list = []
    try:
        with open(filename, "r") as file:
            incidents_list = json.load(file)
    except FileNotFoundError:
        incidents_list = []
    return incidents_list

def incidents_by_service(incidents):
    i_by_service = defaultdict(list)
    for i in incidents:
        i_by_service[i["service"]].append(i["id"])
    return dict(i_by_service)

def count_by_severity(incidents):
    return dict(Counter(i["severity"] for i in incidents).most_common())

def unresolved_incidents(incidents):
    return [i["id"] for i in incidents if not i["resolved"]]

def average_duration_by_service(incidents):
    durations = defaultdict(list)
    for i in incidents:
        if i["resolved"]:
            durations[i["service"]].append(i["duration_min"])
    result = {}
    for service, times in durations.items():
        result[service] = round(sum(times)/ len(times), 1)
    return result

def worst_service(incidents):
    return dict(Counter(i["service"] for i in incidents if i["severity"] == "critical").most_common(1))

def generate_report(incidents):

    # dict -> json.file
    # json.dump(data, f)
    report = {"incidents by service": incidents_by_service(incidents)
            ,"county by severity": count_by_severity(incidents)
            ,"unresolved incidents": unresolved_incidents(incidents)
            ,"average duration by service": average_duration_by_service(incidents)
            ,"worst service": worst_service(incidents)}

    with open("report.json", "w") as report_file:
        json.dump(report, report_file)
    return report

def main():
    incidents = load_incidents("incidents.json")

    print(incidents_by_service(incidents))          # list -> dict
    print(count_by_severity(incidents))
    print(unresolved_incidents(incidents))
    print(average_duration_by_service(incidents))
    print(worst_service(incidents))

    report = generate_report(incidents)
    print(report)

if __name__ == "__main__":
    main()
