import json
from collections import defaultdict, Counter

file_tasks = [
    {"id": "T-01", "assignee": "ana",   "status": "done",        "priority": "high",   "hours": 8},
    {"id": "T-02", "assignee": "boris", "status": "in_progress", "priority": "medium", "hours": 5},
    {"id": "T-03", "assignee": "ana",   "status": "done",        "priority": "low",    "hours": 2},
    {"id": "T-04", "assignee": "chen",  "status": "blocked",     "priority": "high",   "hours": 3},
    {"id": "T-05", "assignee": "boris", "status": "done",        "priority": "high",   "hours": 6},
    {"id": "T-06", "assignee": "ana",   "status": "blocked",     "priority": "medium", "hours": 1},
    {"id": "T-07", "assignee": "chen",  "status": "done",        "priority": "medium", "hours": 4},
    {"id": "T-08", "assignee": "boris", "status": "done",        "priority": "high",   "hours": 7},
    {"id": "T-09", "assignee": "chen",  "status": "in_progress", "priority": "low",    "hours": 2},
]

with open("tasks.json", "w") as f:
    json.dump(file_tasks, f, indent=2)

def load_tasks(filename):
    tasks_from_file = []
    try:
        with open(filename, "r") as file:
            tasks_from_file = json.load(file)
    except FileNotFoundError:
        tasks_from_file = []
    return tasks_from_file

def tasks_by_assignee(tasks):
    tasks_ass = defaultdict(list)
    for task in tasks:
        tasks_ass[task["assignee"]].append(task["id"])
    return dict(tasks_ass)

def count_by_status(tasks):
    return dict(Counter(task["status"] for task in tasks).most_common())

def blocked_tasks(tasks):
    return [task["id"] for task in tasks if task["status"] == "blocked"]

def total_hours_by_assignee(tasks):
    hours_list = defaultdict(list)
    result = {}
    for task in tasks:
        hours_list[task["assignee"]].append(task["hours"])

    for assignee, hours in hours_list.items():
        result[assignee] = sum(hours)
    return result

def busiest_person(tasks):
    # task_assignee = Counter(task["assignee"] for task in tasks if task["priority"] == "high")
    # name = max(task_assignee, key=lambda assignee: task_assignee[assignee])
    # return {name: task_assignee[name]}
    return dict(Counter(task["assignee"] for task in tasks if task["priority"] == "high").most_common(1))
def completion_rate_by_assignee(tasks):
    done = Counter(task["assignee"] for task in tasks if task["status"] == "done")
    total = Counter(task["assignee"] for task in tasks)

    return {a: round(done[a] / total[a] * 100, 1) for a in total}

def generate_report(tasks):
    report = {"tasks by assignee": tasks_by_assignee(tasks),
              "count by status": count_by_status(tasks),
              "blocked tasks": blocked_tasks(tasks),
              "total hours by assignee": total_hours_by_assignee(tasks),
              "busiest person": busiest_person(tasks),
              "completion rate by assignee": completion_rate_by_assignee(tasks)}
    # dict -> file
    with open("report2.json", "w") as report_file:
        json.dump(report, report_file)
    return report

def main():
    tasks = load_tasks("tasks.json")
    print(tasks_by_assignee(tasks))

    report = generate_report(tasks)
    print(report)

if __name__ == "__main__":
    main()